from flask import Blueprint, render_template

bp = Blueprint('bp', __name__)

@bp.route('/')
def home():
    return "<h1>Hello, Flask!</h1>"

@bp.route('/login/<nome>')
def login(nome=None):
    return '<center><h1>Ola, '+nome+' <br /> Faça seu login!</h1></center>'

@bp.route('/aula2')
def carrega():
    return render_template('index.html')