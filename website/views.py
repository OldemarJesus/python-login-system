from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('profile', methods=['GET'])
@login_required
def profile():
    return render_template("profile.html", user=current_user)