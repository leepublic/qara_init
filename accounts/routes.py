from flask import Blueprint
from .views import AccountView, AccountAddView, AccountLoginView, logout

bp_account = Blueprint('Accounts', __name__)

bp_account.add_url_rule('/accounts/', view_func=AccountView.as_view('accounts'))
bp_account.add_url_rule('/accounts/add/', view_func=AccountAddView.as_view('account_add'))
bp_account.add_url_rule('/login/', view_func=AccountLoginView.as_view('login'))
bp_account.add_url_rule('/logout/', view_func=logout)
