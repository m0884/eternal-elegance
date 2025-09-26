from flask import Flask 
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index ():
    return"Главная страница" 

@app.route('/about')
def about():
    return"о нас"

@app.route('/catalog')
def catalog ():
    return"каталог"

@app.route('/account')
def account ():
    return"аккаунт"

@app.route('/shop now')
def shop_now ():
    return"shop now"

@app.route('/contact')
def contact():
    return"contact" 

@app.route('/user/<username>')
def user_profile(username):
    return render_template("hello.html", name = username)




if __name__ == 'main':  #точка входа нашей программы
    print("привет, мир")
    app.run (debug=True)
    from flask import Flask 
from flask import render_template
import sqlite3
from flask import request

