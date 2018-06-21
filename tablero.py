import chess
import funciones as f

algoritmos={
	1:"greedy_p",
	2:"greedy_o",
	3:"minimax_p",
	4:"ab_minimax_p",
	5:"minimax_o",
	6:"mcts",
}

print("seleecione un algortimo para ejecutar la IA")
for element in algoritmos:
	print(element,algoritmos[element])


clave= int(input())
board = chess.Board()
print(algoritmos[clave])
f.juego(board,algoritmos[clave])
