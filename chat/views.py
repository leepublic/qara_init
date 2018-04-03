from flask import render_template
from flask.views import View


class BasicSocketView(View):

    def dispatch_request(self):
        return render_template('basic_soc.html')


class ChatView(View):
    def dispatch_request(self):
        return render_template('chat.html')