import chess
import funciones as f
import juego as j
import heuristicas as h


#instancia el tablero
board = chess.Board()
'''
movimiento=0
print("turno jugador ",board.turn)
for i in board.pseudo_legal_moves:
	print(board.is_capture(i))
	movimiento=i
board.push(i)
print("turno maquina ",board.turn)
for i in board.pseudo_legal_moves:
	print(board.is_capture(i))
	movimiento=i	
'''
#muestra los cuadros atacados por la pieza actual
#print(board.attacks(6))
#print(type(board.attacks(6))

#print(f.piezas_comidas(board))
#print("movimientos legales")
#print(board.legal_moves.count())
#print(board.legal_moves)
#print("movimientos pseudo legales")
#print(board.pseudo_legal_moves.count())
#print(board.pseudo_legal_moves)			
#hace que se generen juegos aleatoriamente


f.juego(board)



#print(f.minimax(board,3,board.turn))

#mapita=board.piece_map() 
#cuenta= f.contar_piezas(mapita)
#bla = f.valorizar_piezas(cuenta)





