import chess

mayusculas = 'PNBRQK'
minusculas = 'pnbrqk'
#retornar siempre primero blancas y despues negras

valores_piezas={'P':1,'N':3,'B':3,'R':5,'Q':9,'K':0,
				'p':1,'b':3,'n':3,'r':5,'q':9,'k': 0}
square_values = {28: 1, 36: 1, 27: 1, 35: 1, 42: 0.5, 42: 0.5, 44: 0.5, 45: 0.5,
                    18: 0.5, 19: 0.5, 20: 0.5, 21: 0.5, 26: 0.5, 34: 0.5, 29: 0.5, 37: 0.5}



def contar_piezas(board):
	mapita=board.piece_map() 
	countw={}
	countb={}
	for i in chess.SQUARES:
		if i in mapita:
			if mapita[i].symbol() in countw:
				countw[mapita[i].symbol()] += 1
			elif mapita[i].symbol() in countb:
				countb[mapita[i].symbol()] += 1
			else:
				if mapita[i].symbol() in mayusculas:
					countw[mapita[i].symbol()] = 1
				else:
					countb[mapita[i].symbol()] = 1
	return (countw,countb)


################################funciones de las heuristicas como tal

#peso=100
def material(board,peso):
    tupla=contar_piezas(board)
    mapa=tupla[0]
    total=0
    for a in mayusculas:
        try:
            total = total + mapa[a]*valores_piezas[a]
        except KeyError as error:
            continue    
    mapa=tupla[1]
    for a in minusculas:
        try:
            total = total + mapa[a]*-valores_piezas[a] 
        except KeyError as error:
            continue    
    return total*peso



#peso=50
#esta heuritisica se basa en los movimientos futuros, da ptos si los cuadros estan disponibles para usarse
def piece_moves(board, peso):
    black_points = 0
    for i in board.legal_moves:
        if board.turn:
            if i.to_square in square_values:
                black_points += square_values[i.to_square]
        else:
            if i.to_square in square_values:
                black_points -= square_values[i.to_square]
    return black_points*peso   


#peso=01
#cuenta si el jugador esta en jaque o nop|
def in_check(board, peso):
    black_points = 0

    if board.turn:
        if not board.is_check():
            black_points += 1 * peso
        else:
            black_points += float("inf")
    else:
        if not board.is_check():
            black_points -= 1 * peso
        else:
            black_points += float("-inf")
    return black_points





#peso=01
def pawn_structure(board, peso):
    black_points = 0
    turno=board.turn
    #valora defender a los peones
    numero=0
    contador=1
    for i in range(8):
        for j in range(8):

            numero=contador*(i)+ (j)
            if(board.piece_type_at(numero) == chess.PAWN):
                tl = i-1, j-1 #defensar izq
                tr = i-1, j+1   #defensar der
                if tl[0] >= 0 and tl[0] <= 7 and tl[1] >= 0 and tl[1] <= 7:
                    numero=contador*(i)+ (j)
                    if board.piece_type_at(numero) == chess.PAWN:
                        black_points += 1
        contador+=1 
    return black_points * peso
#######################################DE AQUI HACIA ABAJO FALTA ARREGLAR

