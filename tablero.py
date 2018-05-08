import chess
import funciones as f
import juego as j
import heuristicas as h


#instancia el tablero
board = chess.Board()




#print(f.piezas_comidas(board))
			
#hace que se generen juegos aleatoriamente
f.juego(board)

#print(f.minimax(board,3,board.turn))

#mapita=board.piece_map() 
#cuenta= f.contar_piezas(mapita)
#bla = f.valorizar_piezas(cuenta)





