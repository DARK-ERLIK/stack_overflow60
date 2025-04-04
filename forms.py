from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    name = StringField(
        label="Имя пользователя",
        validators=[DataRequired("Поле 'Имя' обязательно для заполнения"),
                    Length(min=2, max=15, message="Имя должно быть от 2 до 15 символов")],
        render_kw={"placeholder": "Введите ваше имя"}
    )
    email = EmailField(
        label="Электронная почта",
        validators=[DataRequired("Поле 'Email' обязательно для заполнения")],
        render_kw={"placeholder": "example@mail.com"}
    )
    password1 = PasswordField(
        label="Пароль",
        validators=[DataRequired("Придумайте пароль"),
                    Length(min=6, message="Пароль должен быть не менее 6 символов")],
        render_kw={"placeholder": "Не менее 6 символов"}
    )
    password2 = PasswordField(
        label="Подтверждение пароля",
        validators=[DataRequired("Повторите пароль"),
                    EqualTo('password1', message="Пароли должны совпадать")],
        render_kw={"placeholder": "Повторите ваш пароль"}
    )
    button = SubmitField(label="Зарегистрироваться")

class LoginForm(FlaskForm):
    name = StringField(
        label="Имя пользователя",
        validators=[Optional("Введите ваше имя")],
        render_kw={"placeholder": "Ваше имя"}
    )
    password = PasswordField(
        label="Пароль",
        validators=[Optional("Введите пароль")],
        render_kw={"placeholder": "Ваш пароль"}
    )
    email = EmailField(
        label="Электронная почта",
        validators=[Optional(), Email(message="Некорректный формат email")],
        render_kw={"placeholder": "example@mail.com"}
    )
    button = SubmitField(label="Войти")

class QuestionForm(FlaskForm):
    title = StringField(
        label="Заголовок вопроса",
        validators=[DataRequired("Заголовок не может быть пустым"),
                    Length(max=100, message="Заголовок слишком длинный")],
        render_kw={"placeholder": "Краткий заголовок вопроса"}
    )
    text = TextAreaField(
        label="Подробное описание",
        validators=[DataRequired("Опишите ваш вопрос подробнее"),
                    Length(min=10, message="Описание должно быть не менее 10 символов")],
        render_kw={"placeholder": "Опишите проблему подробно...", "rows": 5}
    )
    button = SubmitField(label="Опубликовать вопрос")

class AnswerForm(FlaskForm):
    text = TextAreaField(
        label="Ваш ответ",
        validators=[DataRequired("Ответ не может быть пустым"),
                    Length(min=10, message="Ответ должен быть не менее 10 символов")],
        render_kw={"placeholder": "Напишите развернутый ответ...", "rows": 5}
    )
    button = SubmitField(label="Отправить ответ")
