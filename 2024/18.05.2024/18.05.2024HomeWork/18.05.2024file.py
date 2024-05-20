from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': 'froms'},
    {'name': 'О нас', 'url': 'then'},
    {'name': 'Обратная связь', 'url': 'contact'}

]


@app.route("/")
@app.route("/froms")
def froms():
    return render_template('froms.html', title="Main", menu=menu)


@app.route("/then")
def then():
    return render_template('then.html', title="About", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)