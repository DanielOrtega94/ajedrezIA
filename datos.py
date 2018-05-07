import chess



maxi = chess.WHITE
mini = chess.BLACK

#instancia un tablero
board = chess.Board()

#limpia el tablero  
board.clear_board()

#lista de movimientos legales para hacer
print(board.legal_moves)

#cuenta los movimientos legales
print(board.legal_moves.count())

#dice a quien le toca mover true blancos false negros
print(board.turn)

#generamos un movimiento y lo realizamos
Nf3 = chess.Move.from_uci("h2h3") 
board.push(Nf3)