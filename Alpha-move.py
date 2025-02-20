import chess
import requests

board = chess.Board()

board.legal_moves
print(board.legal_moves)


class engine():

    def alpha_move():
        moves =[]
        moves= board.legal_moves
        if len(moves) % 2 == 0:
            half = len(moves) / 2
            alpha = board.legal_moves[half]
        else:
            half = (len(moves) + 1) / 2
            alpha = board.legal_moves[half]

        return alpha

        def player_move():
            return board.legal_moves[0]




