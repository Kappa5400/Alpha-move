import chess
import requests

board = chess.Board()


class engine():
    def alpha_move():
        moves =[]
        moves= list(board.legal_moves)
        if len(moves) % 2 == 0:
            alpha = len(moves) / 2
            
        else:
            moveandone = (len(moves) + 1)
            alpha = moveandone / 2

        alpha = int(alpha)
        print("Alpha:{move[alpha]}")
        board.push_san(f"{moves[alpha]}")
       

        return

    def player_move():
        p_move = input("What is your move?: ")
        moves = []
        moves = list(board.legal_moves)
        print(moves[0])
        board.push_san(f"{moves[0]}")
        
        return 

        

while board.is_game_over() == 0:
    engine.player_move()
    print(board)
    engine.alpha_move()
    print(board)
    
        


