from flask import render_template
from app import create_app
from accounts.routes import bp_account
from common.db import db_session 

app = create_app()

@app.route("/")
def index():
    return render_template('index.html')


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
