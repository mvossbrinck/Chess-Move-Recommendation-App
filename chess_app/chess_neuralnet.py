import chess
from keras.models import Sequential, load_model, model_from_json


def make_matrix(board):
    pgn = board.epd()
    foo = []
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('.')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo

def translate(matrix,chess_dict):
    rows = []
    for row in matrix:
        terms = []
        for term in row:
            terms.append(chess_dict[term])
        rows.append(terms)
    return rows

chess_dict = {
    'p' : [1,0,0,0,0,0,0,0,0,0,0,0],
    'P' : [0,0,0,0,0,0,1,0,0,0,0,0],
    'n' : [0,1,0,0,0,0,0,0,0,0,0,0],
    'N' : [0,0,0,0,0,0,0,1,0,0,0,0],
    'b' : [0,0,1,0,0,0,0,0,0,0,0,0],
    'B' : [0,0,0,0,0,0,0,0,1,0,0,0],
    'r' : [0,0,0,1,0,0,0,0,0,0,0,0],
    'R' : [0,0,0,0,0,0,0,0,0,1,0,0],
    'q' : [0,0,0,0,1,0,0,0,0,0,0,0],
    'Q' : [0,0,0,0,0,0,0,0,0,0,1,0],
    'k' : [0,0,0,0,0,1,0,0,0,0,0,0],
    'K' : [0,0,0,0,0,0,0,0,0,0,0,1],
    '.' : [0,0,0,0,0,0,0,0,0,0,0,0],
}

def evaluate(fen):
    loaded_model = load_model('models/chessb4.14-0.27.hdf5')
    lst = []
    board = chess.Board(fen)
    for move in board.legal_moves:
            board.push(move)
            matrix = make_matrix(board)
            board.pop()
            rows = translate(matrix,chess_dict)
            value = (loaded_model.predict([rows])).item()
            move_san = board.san(move)
            item = [move_san, value]
            lst.append(item)
    return lst

def get_NN_move(fen):
    evaluation = evaluate(fen)
    maximum = -1
    best_move = None
    for term in evaluation:
        if term[1] > maximum:
            maximum = term[1]
            best_move = term[0]
    return best_move
