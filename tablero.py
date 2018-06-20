import chess
import funciones as f

print("seleecione un algortimo para ejecutar la IA")
print("greedy_p")
print("greedy_o")
print("minimax_p")
print("ab_minimax_p")
print("minimax_o")
print("mcts")

algoritmo= input()
board = chess.Board()
f.juego(board,algoritmo)


#debo realizar las prubeas para el mcts