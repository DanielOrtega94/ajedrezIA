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

#esta heuritisica se basa en los movimientos futuos
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

#######################################DE AQUI HACIA ABAJO FALTA ARREGLAR


#peso=01
def pawn_structure(board_state, weight):
    black_points = 0
    board_state, current_player = [segment for segment in board_state.split()[:2]]
    board_state = board_state.split("/")

    # convert fen into matrix:
    board_state_arr = []
    for row in board_state:
    	row_arr = []
    	for char in row:
    		if char.isdigit():
    			for i in range(int(char)):
    				row_arr.append(" ")
    		else:
    			row_arr.append(char)
    	board_state_arr.append(row_arr)

    # determine pawn to search for based on whose turn it is
    for i, row in enumerate(board_state_arr):
        for j in range(len(row)):
            if board_state_arr[i][j] == "p":
                tl = i-1, j-1
                tr = i-1, j+1
                if tl[0] >= 0 and tl[0] <= 7 and tl[1] >= 0 and tl[1] <= 7:
                    if board_state_arr[tl[0]][tl[1]] == "p":
                        black_points += 1
                if tr[0] >= 0 and tr[0] <= 7 and tr[1] >= 0 and tr[1] <= 7:
                    if board_state_arr[tr[0]][tr[1]] == "p":
                        black_points += 1
    return black_points * weight

#peso=01
def in_check(game, weight):
    black_points = 0
    current_status = game.status
    # Turn should be 'w' or 'b'
    turn = str(game).split(" ")[1]
    # Check or Checkmate situations
    if turn == "w":
        if current_status == 1:
            black_points += 1 * weight
        elif current_status == 2:
            black_points += float("inf")
    else:
        if current_status == 1:
            black_points -= 1 * weight
        elif current_status == 2:
            black_points += float("-inf")
    return black_points

