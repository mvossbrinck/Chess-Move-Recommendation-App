from flask import Flask, render_template, request
from chess_random import get_random_move
from chess_minimax2 import get_minimax_move
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chessboard.html')


@app.route('/nextmove', methods=['POST'])
def fen_output():
    request_data = request.get_json()
    if (request_data['algorithm'] == 'Random Move'):
        nextMove = get_random_move(request_data["currentBoardPosition"])
    else:
        nextMove = get_minimax_move(request_data["currentBoardPosition"])
    return {'nextMove': nextMove, 'algorithm': request_data['algorithm']}



app.config["TEMPLATES_AUTO_RELOAD"] = True


if __name__ == "__main__":
    app.run(debug=True)
