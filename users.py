from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from forms import RegisterForm, LoginForm

users_bp = Blueprint('users', __name__, url_prefix='/user')

@users_bp.route('/')
def users_home():
    return "Юзеры"

@users_bp.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        session['username'] = form.name.data
        flash('Вы успешно зарегистрированы!', 'success')
        return redirect(url_for("questions.questions_home"))
    return render_template('register.html', form=form)

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.name.data
        flash('Вы успешно вошли в систему!', 'success')
        return redirect(url_for("questions.questions_home"))
    return render_template('login.html', form=form)

@users_bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('Вы успешно вышли из системы', 'info')
    return redirect(url_for('users.login'))
