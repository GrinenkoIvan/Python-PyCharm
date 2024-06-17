import sqlite3
import os
from flask import Flask, flash, g, redirect, render_template, request, session, url_for

from HM_DataBase import HM_DataBase

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = os.urandom(20).hex()

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'flsk.db'))


def connect_db():
    connection = sqlite3.connect(app.config['DATABASE'])
    connection.row_factory = sqlite3.Row
    return connection


def create_db():
    db = connect_db()
    with app.open_resource('home_site.sql', mode='r') as file:
        db.cursor().executescript(file.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
def index():
    db = get_db()
    dbase = HM_DataBase(db)
    return render_template(template_name_or_list='index_home.html',
                           menu=dbase.get_menu(),
                           posts=dbase.get_posts_annonce())


@app.route('/add_home', methods=['GET', 'POST',])
def add_home():
    db = get_db()
    dbase = HM_DataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_home(request.form['name'],
                                 request.form['post'],
                                 request.form['url'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья успешно добавлена', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')

    return render_template(template_name_or_list='add_home.html',
                           menu=dbase.get_menu(),
                           title='Добавление статьи')


@app.route('/post/<alias>')
def show_post(alias):
    db = get_db()
    dbase = HM_DataBase(db)
    title, post = dbase.get_post(alias)

    return render_template(template_name_or_list='post_home.html',
                           menu=dbase.get_menu(),
                           title=title,
                           post=post)


if __name__ == '__main__':
    app.run(debug=True)
