from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from forms import QuestionForm, AnswerForm
from config import Config

questions_bp = Blueprint("questions", __name__, url_prefix="/questions")


@questions_bp.route("/")
def questions_home():
    if 'username' not in session:
        flash('Для просмотра вопросов необходимо войти в систему', 'warning')
        return redirect(url_for("users.login"))

    return render_template("questions.html",
                           questions=Config.DATABASE,
                           username=session.get('username'))

@questions_bp.route("/add-question", methods=["GET", "POST"])
def add_question():
    if 'username' not in session:
        flash('Для добавления вопроса необходимо войти в систему', 'warning')
        return redirect(url_for("users.login"))

    form = QuestionForm()
    if form.validate_on_submit():
        question = {
            "id": len(Config.DATABASE),
            "title": form.title.data,
            "text": form.text.data,
            "author": session['username'],
            "answers": []
        }
        Config.DATABASE.append(question)
        flash('Ваш вопрос успешно добавлен!', 'success')
        return redirect(url_for("questions.questions_home"))
    return render_template("add_question.html", form=form)


@questions_bp.route("/<int:question_id>", methods=["GET", "POST"])
def show_question(question_id):
    if question_id >= len(Config.DATABASE):
        flash('Вопрос не найден', 'error')
        return redirect(url_for("questions.questions_home"))

    form = AnswerForm()
    if form.validate_on_submit():
        answer = {
            "text": form.text.data,
            "author": session.get('username', 'Аноним')
        }
        Config.DATABASE[question_id]["answers"].append(answer)
        flash('Ваш ответ успешно добавлен!', 'success')
        return redirect(url_for("questions.show_question", question_id=question_id))

    return render_template("question.html",
                           question=Config.DATABASE[question_id],
                           question_id=question_id,
                           form=form,
                           username=session.get('username'))
