import chess
import os
import heuristicas as h
import node as no
import time


def escribir_fichero(texto):
    F = open("salida.txt", "a")
    F.write(texto)
    F.write("\n")
    F.close()


def marcador(board):
    blancas, negras = h.piezas_comidas(board)
    print("capturadas x negras", blancas)
    print("capturadas x blancas", negras)


def validar(mov):
    return 'a' <= mov[0] <= 'h' and '1' <= mov[1] <= '8' and 'a' <= mov[2] <= 'h' and '1' <= mov[3] <= '8'


def juego(board):
    # and not board.is_variant_end()
    while(not board.is_game_over()):
       # print(board.is_game_over())
        print("turno numero: " + str(board.fullmove_number))
        turno_jugador(board)
        # if not board.is_game_over() and not board.is_variant_end():
        if not board.is_game_over():
            turno_ia(board)
        else:
            break
    print(board.result)
    # agregar para definir quien es el jugador ganador


# problema con el turno del jugador si el string no es de tam 4
def turno_jugador(board):
    print("Turno jugador....")
    marcador(board)
    print(board)
    entrada = input()
    while(entrada):

        if entrada == 'v':
            print(board)

        elif entrada == 'r':
            print("Reiniciando Juego")
            os.system('cls')
            board.reset()

        elif entrada == 'h' or entrada == 'H':
            print("Mov disponibles" + str(board.legal_moves.count()))
            for i in board.legal_moves:
                print(str(board.piece_at(i.from_square)) + ' : ' + board.uci(i))

        elif(len(entrada) == 4 and validar(entrada)):
            mov = chess.Move.from_uci(entrada)
            if mov in board.legal_moves:
                board.push(mov)
                break
            print("movimiento invalido intente nuevamente")
        entrada = input()
    return False


def mensaje_impreso(a1, a2, board):
    porcentaje = a1 / a2 * 100
    palabra1 = "Se han recorrido " + \
        str(a1) + " de Nodos con alpha-beta en turno " + \
        str(board.fullmove_number)
    palabra2 = "Se han recorrido " + \
        str(a2) + " de Nodos minimax en turno " + str(board.fullmove_number)
    palabra3 = "Se ha reducido en un " + \
        str(porcentaje) + "%" + " la busqueda del mov"

    palabra = palabra1 + "\n" + palabra2 + "\n" + palabra3
    escribir_fichero(palabra)
#


def turno_ia(board, llamadas=0, llam=0):
    print("Turno Computador....")

    '''
    inicio = time.time()
    mov = mejor_movimiento_(board)
    final = time.time()
    tiempo = final - inicio
    print("tiempo tomado ", tiempo)
    '''

    '''
    inicio = time.time()
    valor, mov, llam = minimax(board, llam)
    valor, mov, llamadas = ab_minimax(board, llamadas)
    print(mov)
    mensaje_impreso(llamadas, llam,board)
    final = time.time()
    tiempo = final - inicio
    print("tiempo tomado ", tiempo)
    '''

    inicio = time.time()
    mov = no.UCT(rootstate=board, itermax=500, verbose=False, board=board)
   # mov = no.UCT(rootstate=board, itermax=700, verbose=False, board=board)
    print(mov)
    final = time.time()
    tiempo = final - inicio
    print("tiempo tomado ", tiempo)

    board.push(mov)


# emula w*h+w*h.....
def valor_heuristicas(board):
    total_points = 0
    total_points += h.material(board, 50)
    total_points += h.pawn_structure(board, 10)
    total_points += h.jaque(board, 50)
    total_points += h.piece_moves(board, 50)
    return total_points

##########################################################################


def greedy(board):
    mejor_movimiento = 0
    mejor_valor = -999
    for i in board.legal_moves:
        print("Movimiento pusheado: " + str(i) +
              " : " + str(board.piece_at(i.from_square)))
        board.push(i)
        # print(board.is_capture(i))
        valores = valor_heuristicas(board, i)
        print(valores)

        if valores > mejor_valor:
            mejor_movimiento = i
            mejor_valor = valores

        board.pop()
    return mejor_movimiento

##########################################################################


def minimax(board, llamadas, current_depth=0, max_depth=4):
    current_depth += 1
    llamadas += 1

    if current_depth == max_depth:
        # valor heuristico
        valor = valor_heuristicas(board)
        return valor, None, llamadas

    if current_depth % 2 == 0:
        # Turno jugador minimo
        best = float('inf')
        mejor_mov = None
        for i in board.legal_moves:
            board.push(i)
            algo, algo2, llamadas = minimax(
                board, llamadas, current_depth, max_depth)
            board.pop()
            if algo < best:
                best = algo
                mejor_mov = i

        return best, mejor_mov, llamadas
    else:
        # Turno jugador maximo
        best = float('-inf')
        mejor_mov = None
        for i in board.legal_moves:
            board.push(i)
            algo, algo2, llamadas = minimax(
                board, llamadas, current_depth, max_depth)
            board.pop()
            if algo > best:
                best = algo
                mejor_mov = i
        return best, mejor_mov, llamadas


def ab_minimax(board, llamadas, current_depth=0, max_depth=4, alpha=float("-inf"), beta=float("inf")):
    current_depth += 1
    llamadas += 1

    if current_depth == max_depth:
        # Obtiene valor heuristicas
        valor = valor_heuristicas(board)
        return valor, None, llamadas

    if current_depth % 2 == 0:
        # Turno jugador minimo
        best = float('inf')
        best_move = None
        for i in board.legal_moves:
            board.push(i)
            algo, algo2, llamadas = ab_minimax(
                board, llamadas, current_depth, max_depth, alpha, beta)
            board.pop()
            beta = min(beta, algo)
            if algo < best:
                best = algo
                best_move = i
            if best < alpha:
                break
        return best, best_move, llamadas
    else:
         # Turno jugador maximo
        best = float('-inf')
        best_move = None
        for i in board.legal_moves:
            board.push(i)
            algo, algo2, llamadas = ab_minimax(
                board, llamadas, current_depth, max_depth, alpha, beta)
            board.pop()
            alpha = max(alpha, algo)
            if algo > best:
                best = algo
                best_move = i
            if best > beta:
                break
        return (best, best_move, llamadas)


##########################################################################

'''
def hacer_movimiento(board):
    posibles = genera_hijo(board)
    for mov in posibles:
        mov.valor = minimax(mov, board)
    mejor_mov = posibles[0]
    for mov in posibles:
        if mov.valor > mejor_mov.valor:
            mejor_mov = mov
    return mejor_mov.movimiento'''

# board.fen()
# board.set_fen()

'''
def minimax(node, board, current_depth=0, max_depth=3):
    current_depth += 1
    if current_depth == max_depth:
        # get heuristic of each node
        node.valor = valor_heuristicas(board)
        return node.valor

    if current_depth % 2 == 0:
        # min player's turn
        #self.is_turn = False
        return min([minimax(child_node,board, current_depth) for child_node in genera_hijo(board)])

    else:
        # max player's turn
        #self.is_turn = True
        return max([minimax(child_node, board,current_depth) for child_node in genera_hijo(board)])

'''
'''def minimax(board, profundidad, turno):

    if profundidad == 0:
        valores = valor_heuristicas(board)
        return valores
    if(board.turn):
        print("blancas", profundidad)
        mejor_movimiento = -999
        mov = 0
        for i in board.legal_moves:
            board.push(i)
            valores = valor_heuristicas(board)
            mejor_movimiento = max(valores, minimax(
                board, profundidad - 1, board.turn))
            print(board)
            board.pop()
        return mejor_movimiento

    else:
        print("negras", profundidad)
        mejor_movimiento = 999
        for i in board.legal_moves:
            board.push(i)
            valores = valor_heuristicas(board)
            mejor_movimiento = min(valores, minimax(
                board, profundidad - 1, board.turn))
            board.pop()
        return mejor_movimiento'''
