from pprint import pprint
import os
import chess
import algoritmos as algo
import mcts as no
import heuristicas as h
import nodo as n
import time

# para poder ordenar los diccionarios al imprimir


class SortedDisplayDict(dict):

    def __str__(self):
        return "{" + ", ".join("%r: %r" % (key, self[key]) for key in sorted(self)) + "}"

###########varibales globales################
#totales = []
piezas_comidas_blancas, piezas_actuales_negras = {}, {}

###########################funciones####################


def escribir_fichero(texto, archivo):
    F = open(archivo, "a")
    F.write(texto)
    F.write("\n")
    F.close()


def piezas_comidas(board):
    piezas_actuales_blancas, piezas_actuales_negras = h.contar_piezas(board)
    piezas_comidas_blancas = {key: h.totales_blancas[
        key] - piezas_actuales_blancas.get(key, 0) for key in h.totales_blancas}
    piezas_comidas_negras = {key: h.totales_negras[
        key] - piezas_actuales_negras.get(key, 0) for key in h.totales_negras}
    return (piezas_comidas_blancas, piezas_comidas_negras)


def marcador(board):
    blancas, negras = piezas_comidas(board)
    # blancas=sorted(blancas)
    # negras=sorted(negras)
    blancas = SortedDisplayDict(blancas)
    negras = SortedDisplayDict(negras)
    print("capturadas x negras ", blancas)
    print("capturadas x blancas", negras)


def validar(mov):
    return 'a' <= mov[0] <= 'h' and '1' <= mov[1] <= '8' and 'a' <= mov[2] <= 'h' and '1' <= mov[3] <= '8'


def mensaje_impreso(a1, a2, board, prueba=False):
    if prueba:
        porcentaje = a1 / a2 * 100
        palabra1 = "Se han recorrido " + \
            str(a1) + " de Nodos con alpha-beta en turno " + \
            str(board.fullmove_number)
        palabra2 = "Se han recorrido " + \
            str(a2) + " de Nodos minimax en turno " + \
            str(board.fullmove_number)
        palabra3 = "Se ha reducido en un " + \
            str(porcentaje) + "%" + " la busqueda del mov"
        palabra = palabra1 + "\n" + palabra2 + "\n" + palabra3
        escribir_fichero(palabra, "salida.txt")


def juego(board, algoritmo, prueba=False):

    while(not board.is_game_over()):
        turno_jugador(board, prueba)
        if not board.is_game_over():
            turno_ia(board, algoritmo, prueba)
        else:
            break
    print(board.result)


# problema con el turno del jugador si el string no es de tam 4
def turno_jugador(board, prueba):
    os.system('cls')
    print("turno numero: " + str(board.fullmove_number))
    print("Turno jugador....")
    if prueba:
        board.push(algo.greedy(board))
        return
    marcador(board)
    print(board)
    entrada = input()
    while(entrada):

        if entrada == 'v':
            print(board)

        elif entrada == 'h' or entrada == 'H':
            print("Mov disponibles " + str(board.legal_moves.count()))
            for i in board.legal_moves:
                print(str(board.piece_at(i.from_square)) + ' : ' + board.uci(i))

        elif(len(entrada) == 4 and validar(entrada)):
            mov = chess.Move.from_uci(entrada)
            if mov in board.legal_moves:
                board.push(mov)
                del mov
                break
            print("movimiento invalido intente nuevamente")
        entrada = input()
    return False


def turno_ia(board, algoritmo, llamadas=0, llam=0, prueba=False):
    print("Turno Computador....")

    if algoritmo == "greedy_p":
        print("greedy_p")
        inicio = time.time()
        mov = algo.greedy(board)
        final = time.time()
        tiempo = final - inicio
        escribir_fichero(str(tiempo), "tiempos.txt")
        # print("tiempo tomado ", tiempo)

        board.push(mov)
        del mov

    elif algoritmo == "greedy_o":
        print("greedy_o")
        inicio = time.time()
        mov = algo.hacer_movimiento_m(board)
        final = time.time()
        tiempo = final - inicio
        escribir_fichero(str(tiempo), "tiempos.txt")
        # print("tiempo tomado ", tiempo)

        board.push(mov)
        del mov

    elif algoritmo == "minimax_p":
        if not prueba:
            print("minimax_p")
            inicio = time.time()
            valor, mov, llam = algo.minimax(board, llam)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(tiempo), "tiempos.txt")

            board.push(mov)
            del mov
        else:
            print(prueba)
            print("minimax_p")
            inicio = time.time()
            valor, mov, llam = algo.minimax(board, llam)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(4) + ' ' + str(tiempo), "tiempos.txt")

            print("minimax_p")
            inicio = time.time()
            valor, mov, llam = algo.minimax(board, llam, max_depth=5)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(5) + ' ' + str(tiempo), "tiempos.txt")

            print("minimax_p")
            inicio = time.time()
            valor, mov, llam = algo.minimax(board, llam, max_depth=6)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(6) + ' ' + str(tiempo), "tiempos.txt")

            print("minimax_p")
            inicio = time.time()
            valor, mov, llam = algo.minimax(board, llam, max_depth=7)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(7) + ' ' + str(tiempo), "tiempos.txt")

            board.push(mov)
            del mov

    elif algoritmo == "ab_minimax_p":
        if not prueba:
            print("ab_minimax_p")
            inicio = time.time()
            valor, mov, llamadas = algo.ab_minimax(board, llamadas)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(tiempo), "tiempos.txt")
           # tiempo_mab.append(tiempo)
            mensaje_impreso(llamadas, llam, board)
            board.push(mov)
            del mov
        else:
            print(prueba)
            print("ab_minimax_p")
            inicio = time.time()
            valor, mov, llamadas = algo.minimax(board, llamadas)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(4) + ' ' + str(tiempo), "tiempos.txt")

            print("ab_minimax_p")
            inicio = time.time()
            valor, mov, llamadas = algo.minimax(board, llamadas, max_depth=5)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(5) + ' ' + str(tiempo), "tiempos.txt")

            print("ab_minimax_p")
            inicio = time.time()
            valor, mov, llamadas = algo.minimax(board, llamadas, max_depth=6)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(6) + ' ' + str(tiempo), "tiempos.txt")

            print("ab_minimax_p")
            inicio = time.time()
            valor, mov, llamadas = algo.minimax(board, llamadas, max_depth=6)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(7) + ' ' + str(tiempo), "tiempos.txt")

            board.push(mov)
            del mov

    elif algoritmo == "minimax_o":
        print("minimax_o")
        inicio = time.time()
        valor, mov, llam = algo.minimax_a_(board, llam)
        final = time.time()
        tiempo = final - inicio
        escribir_fichero(str(tiempo), "tiempos.txt")

        board.push(mov)
        del mov

    elif algoritmo == "mcts":
        if not prueba:
            print("mcts")
            inicio = time.time()
            mov = no.UCT(estadobase=board, itermax=700, board=board)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(tiempo), "tiempos.txt")
            print(tiempo)
            board.push(mov)
            del mov
        else:
            print("mcts")
            inicio = time.time()
            mov = no.UCT(estadobase=board, itermax=500, board=board)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(tiempo), "tiempos.txt")

            print("mcts")
            inicio = time.time()
            mov = no.UCT(estadobase=board, itermax=750, board=board)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(tiempo), "tiempos.txt")

            print("mcts")
            inicio = time.time()
            mov = no.UCT(estadobase=board, itermax=1000, board=board)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(tiempo), "tiempos.txt")

            print("mcts")
            inicio = time.time()
            mov = no.UCT(estadobase=board, itermax=1250, board=board)
            final = time.time()
            tiempo = final - inicio
            escribir_fichero(str(tiempo), "tiempos.txt")

    if algoritmo == "prueba":
        porcentajes = llamadas / llam * 100
        escribir_fichero(str(porcentajes), "tiempos.txt")
        # totales.append(porcentajes)
