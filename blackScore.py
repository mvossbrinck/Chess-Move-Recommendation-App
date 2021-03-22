import chess

def blackScore(fen_input):
    piece_values = {
        chess.PAWN: 100,
        chess.ROOK: 563,
        chess.KNIGHT: 305,
        chess.BISHOP: 333,
        chess.QUEEN: 950,
        chess.KING: 20000
        }

    board = chess.Board(fen_input)
    black_score = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        if piece.color == chess.BLACK:
            black_score += piece_values[piece.piece_type]

    return black_score
