from flask import render_template
from flask.views import View


class BasicSocketView(View):

    def dispatch_request(self):
        return render_template('basic_socket.html')


class ChatView(View):
    def dispatch_request(self):
        return render_template('chat.html')


class WsView(View):
	def dispatch_request(self):
		return render_template('ws-basic.html')