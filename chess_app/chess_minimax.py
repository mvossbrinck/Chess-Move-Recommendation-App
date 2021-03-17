import chess
import numpy as np
from whiteScore import whiteScore
from blackScore import blackScore


def evaluate(fen_input, maximizing_color):
    if maximizing_color == WHITE:
        return whiteScore(fen_input) - blackScore(fen_input)
    else:
        return blackScore(fen_input) - whiteScore(fen_input)



def get_minimax_move(fen_input,  maximizing_player, depth = 4, maximizing_color):
    board = chess.Board(fen_input)


    def minimax(self, depth, move, maximiser):
        if depth == 0:
            return move, self.material_eval()
            #return move, self.position_eval()

        if maximiser:
            best_move = None
            best_score = -9999

            moves = list(self.board.legal_moves)

            for move in moves:
                self.leaves_reached += 1
                self.board.push(move)
                new_move, new_score = self.minimax(depth - 1, move, False)
                if new_score > best_score:
                    best_score, best_move = new_score, move
                self.board.pop()

            return best_move, best_score

        if not maximiser:
            best_move = None
            best_score = 9999

            moves = list(self.board.legal_moves)

            for move in moves:
                self.leaves_reached += 1
                self.board.push(move)
                new_move, new_score = self.minimax(depth - 1, move, True)
                if new_score < best_score:
                    best_score, best_move = new_score, move
                self.board.pop()

            return best_move, best_score
