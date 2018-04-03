from flask import Blueprint
from .views import BasicSocketView

bp_chat = Blueprint('Chat', __name__)

bp_chat.add_url_rule('/socket/', view_func=BasicSocketView.as_view('socket'))

