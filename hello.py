from flask import Flask
from flask import render_template, request, jsonify, make_response
from connect4 import *
from tictactoe import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/connect4')
def connect4():
    return render_template("Connect4.html")

@app.route('/connect4/AIResponse', methods=["POST"])
def connect4Bot():
    req = request.get_json()
    game = req['message']
    if game.count(0) == 42:
        answer = (18, False)
    else:
        print("The bot is thinking")
        answer = playConnect4(game)
    req = make_response(jsonify({"endGame": answer[1], "player": answer[0]}), 200)
    return req

@app.route('/othello')
def othello():
    return render_template("Othello.html")

@app.route('/tictactoe')
def tictactoe():
    return render_template("TicTacToe.html")

@app.route('/tictactoe/AIResponse', methods=["POST"])
def tictactoeBot():
    req = request.get_json()
    game = req['message']
    if game.count(0) == 9:
        answer = (0, False)
    else:
        answer = playGame(game)
    req = make_response(jsonify({"endGame": answer[1], "player": answer[0]}), 200)
    return req

if __name__ == "__main__":
    app.run()


    

        