from flask import Flask

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template("home.html")

@app.route('/menu')
def render_homepage():
    return render_template("menu.html")

@app.route('/contact')
def render_homepage():
    return render_template("contact.html")

app.run(host="0.0.0.0")
