import redis
import pickle

from datetime import timedelta
from flask.sessions import SessionInterface, SessionMixin
from uuid import uuid4
from werkzeug.datastructures import CallbackDict


from accounts.models import FlaskSession


def generate_sid():
    return str(uuid4())


class RedisSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None, sid=None, new=False):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        self.new = new
        self.modified = False


class RedisSessionInterface(SessionInterface):
    serializer = pickle
    session_class = RedisSession

    def __init__(self, prefix='sessiion:'):
        self.store = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.prefix = prefix

    def get_redis_expiration_time(self, app, session):
        if session.permanent:
            return app.permanent_session_lifetime
        return timedelta(days=1)

    def open_session(self, app, request):
        sid = request.cookies.get(app.config['SESSION_COOKIE_NAME'])
        if not sid:
            sid = generate_sid()
            return self.session_class(sid=sid, new=True)
        val = self.store.get(self.prefix + sid)
        if val is not None:
            data =  self.serializer.loads(val)
            return self.session_class(data, sid=sid)
        return self.session_class(sid=sid, new=True)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)

        if not session:
            self.store.delete(self.prefix + session.sid)
            if session.modified:
                response.delete_cookie(app.config['SESSION_COOKIE_NAME'], domain=domain)
            return

        redis_exp = self.get_redis_expiration_time(app, session)

        val = self.serializer.dumps(dict(session))
        #self.store.setex(self.prefix + session.sid, val, int(redis_exp.total_seconds()))
        self.store.set(self.prefix + session.sid, val)
        self.store.expire(self.prefix + session.sid, int(redis_exp.total_seconds()))

        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        expires = self.get_expiration_time(app, session)

        response.set_cookie(
            app.config['SESSION_COOKIE_NAME'],
            session.sid,
            expires=expires,
            httponly=httponly,
            domain=domain,
            secure=secure
        )
