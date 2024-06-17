from flask import Flask, render_template, url_for, request, flash, redirect, session

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title='Про Flack')


@app.route("/about")
def about():
    return render_template("about.html", title='О сайте')


if __name__ == '__main__':
    app.run(debug=True)
