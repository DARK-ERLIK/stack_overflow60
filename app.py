from flask import Flask, redirect, url_for, session
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Импортируем и регистрируем blueprints
from questions import questions_bp
from users import users_bp

app.register_blueprint(questions_bp)
app.register_blueprint(users_bp)

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for("questions.questions_home"))
    return redirect(url_for("users.login"))


app.run(debug=False, port=4444)
