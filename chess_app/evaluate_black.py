import chess
import numpy as np
from whiteScore import whiteScore
from blackScore import blackScore

def evaluate_black(fen_input):
    return blackScore(fen_input) - whiteScore(fen_input)
