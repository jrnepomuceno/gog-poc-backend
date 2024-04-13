from flask import Flask, request
from flask_cors import CORS, cross_origin
from core.game import Game

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
myGame = Game(is_demo=True)

@app.route("/")
@cross_origin()
def server():
    return "<p>Hello World!</p>"


@app.route('/printboard', methods = ['GET'])
@cross_origin()
def printBoard():
    if request.method == 'GET':
        #myGame.display_board()
        return myGame.board_to_json()

if __name__=='__main__':
    app.run(debug=True)