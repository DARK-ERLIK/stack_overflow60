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
        # Проверка на анонимность - если поля email и password пусты, используем "аноним"
        if not form.email.data and not form.password.data:
            session['username'] = "аноним"  # Псевдоним для анонимного пользователя
        else:
            # Логика для зарегистрированных пользователей, если это нужно
            session['email'] = form.email.data  # Сохраняем email в сессии
            session['username'] = form.email.data.split('@')[0]  # Имя по email (можно изменить)
        # я не согласен с добавлением анонимности, это противоречит политике безопасности и соблюдения законов
        # возможно, это только требование спикера, но в реале обычно везде требуется верификация пользователя
        # и это правильно! потому что некоторые "люди" пользуясь анонимностью вредят другим людям или же
        # репутации/работе людей КОТОРЫЕ РАБОТАЮТ!
        # я нехотя выполнил задание, так как считаю что фидбек должен быть адресным в обе стороны,
        # чтобы все несли равную ответственность как за свои слова, так и за свои дела
        # сорян за коменты, но задание было "бесячим" - морально
        flash('Вы успешно вошли в систему!', 'success')
        return redirect(url_for("questions.questions_home"))
    return render_template('login.html', form=form)

@users_bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('Вы успешно вышли из системы', 'info')
    return redirect(url_for('users.login'))
