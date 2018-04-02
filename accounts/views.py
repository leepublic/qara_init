from flask import render_template, request, redirect, url_for, abort, session
from flask.views import View, MethodView
from common.aesutil import AESCipher
from common.db import db_session as conn


from accounts.models import User


class AccountView(View):
    def dispatch_request(self):
        rows = User.query.all()[:10]
        return render_template('account_list.html', rows=rows)


class AccountAddView(MethodView):

    def get(self):
        return render_template('account_add.html')

    def post(self):
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if username and password:
            enc_password = AESCipher().encrypt(password)
            set_account = User(username, enc_password)
            conn.add(set_account)
            conn.commit()
            return redirect(url_for('Accounts.accounts'))

class AccountLoginView(MethodView):

    def get(self):
        return render_template('login.html')

    def post(self):
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if username and password:
            enc_password = AESCipher().encrypt(password)
            count = User.query.filter(User.username == username, User.password == enc_password).count()

            if count > 0:
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('Accounts.accounts'))
            else:
                abort(404)
        abort('401')

def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('Accounts.accounts'))
