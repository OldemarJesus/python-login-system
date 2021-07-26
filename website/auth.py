from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Sessão iniciada com sucesso!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('notes.start'))
            else:
                flash('Senha incorreta, por favor tente novamente!', category='error')
        else:
            flash('Não conseguimos achar esta conta!', category='error')

    return render_template("login.html", user=current_user)

@auth.route("logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("sign-up", methods=['GET', 'POST'])
def signup():
    # set default values
    email = ''
    name = ''
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        passwordConf = request.form.get('passwordConf')

        user = User.query.filter_by(email=email).first()

        if len(email) < 4:
            flash('Email tem de conter mais de 4 caracteres.', category='error')
        else:
            if user:
                flash('Esta conta já existe!', category='error')
            elif len(name) < 3:
                flash('O nome deve conter mais de 3 caracteres.', category='error')
            elif password != passwordConf:
                flash('A senha não coicidem.', category='error')
            elif len(password) < 7:
                    flash('A senha deve conter mais de 7 caracteres.', category='error')
            else:
                # add user to database
                new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Conta criada!', category='success')
                return redirect(url_for('notes.start'))

    return render_template("sign_up.html", user=current_user, email = email, name = name)