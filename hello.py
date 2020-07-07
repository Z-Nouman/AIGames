from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/connect4')
def connect4():
    return render_template("Connect4.html")

@app.route('/othello')
def othello():
    return render_template("Othello.html")

@app.route('/tictactoe')
def tictactoe():
    return render_template("TicTacToe.html")
