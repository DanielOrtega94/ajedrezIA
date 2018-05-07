import chess
import heuristicas as h


# ejecuta el juego hasta que se termine
#funcion principal
def juego(board):
	while(not board.is_game_over()):
		turno_jugador(board)
		turno_ia(board)



#va en juego.py

def turno_jugador(board):
	print("Turno jugador.... Esperando movida jugador, aprete h para mostrar disponibles")
	print(board)
	entrada =  input()
	if entrada == 'h' or entrada == 'H':
		print("Actualmente tienes disponibles " + str(board.legal_moves.count())+ ' mov disponibles' )
		for i in board.legal_moves:			
			print(board.uci(i) + ' : ' + str(board.piece_at(i.from_square)))
		entrada =  input()
	if(len(entrada) ==4):
		mov = chess.Move.from_uci(entrada)
		if(mov in board.legal_moves):
			board.push(mov)
		else:	
			print("Ingrese nuevamente un movimiento valido")

def turno_ia(board):
	print("Turno Computador....")
	#for i in board.legal_moves:
	#	board.push(i)
	#	break
	board.push(mejor_movimiento_(board))
	#print(board)

#emula w*h+w*h.....
def valor_heuristicas(board):
    total_points = 0
    total_points += h.material(board, 100)
    total_points += h.piece_moves(board, 50)
    #total_points += h.in_check(board, 1)
    #total_points += h.pawn_structure(board, 1)
    return total_points


#revisa si el movimiento es valido, si lo es, lo ingresa, sino solicita otro movimiento
def ingresar_mov(board,entrada):
	mov = chess.Move.from_uci(entrada)
	if(mov in board.legal_moves):
		board.push(mov)
		#print(board)



				
def mejor_movimiento_(board):
	mejor_movimiento = 0
	mejor_valor = -999 
	for i in board.legal_moves:
		board.push(i)
		valores = valor_heuristicas(board)
		#print(valores[1])
		if valores>mejor_valor:
			mejor_movimiento=i
			mejor_valor =valores
		board.pop()	
	return mejor_movimiento	



def minimax(board,profundidad,turno):
	
	if profundidad == 0:
		valores = valor_heuristicas(board)
		return valores

	if(board.turn):
		print("blancas", profundidad)
		mejor_movimiento=-999
		mov=0
		for i in board.legal_moves:
			board.push(i)
			valores = valor_heuristicas(board)
			mejor_movimiento=max(valores,minimax(board,profundidad-1,board.turn))
			print(board)
			board.pop()	
		return mejor_movimiento
	
	else:
		print("negras",profundidad)			
		mejor_movimiento=999
		for i in board.legal_moves:
			board.push(i)
			valores = valor_heuristicas(board)
			mejor_movimiento=min(valores,minimax(board,profundidad-1,board.turn))
			board.pop()	
		return mejor_movimiento
			

# entregar marcador de valores de piezas actuales
#mal implementado
def marcador(mapa):
	claves = mapa.keys()
	for i in claves:
		print(i)


#dice si quedan o no movimientos disponibles para la situacion actual	
#no es necesario implementar porque hay una funcuon en la liberia que lo hace	
def quedan_movimientos():
	return False

'''

def minimax(board, heuristic, next_moves, current_depth=0, max_depth=4):
    current_depth += 1
    if current_depth == max_depth:
        # get heuristic of each node
        return next(heuristic)
    if current_depth % 2 == 0:
        # min player's turn
        return min([minimax(node, heuristic, current_depth, max_depth) for node in next_moves()])
    else:
        # max player's turn
        return max([minimax(node, heuristic, current_depth, max_depth) for node in next_moves()])

'''