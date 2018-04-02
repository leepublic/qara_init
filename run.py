from flask import render_template
from app import create_app
from accounts.routes import bp_account

app = create_app()

@app.route("/")
def index():
    return render_template('index.html')


app.register_blueprint(bp_account)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
