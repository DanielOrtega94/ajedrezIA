import chess

class motor_juego():

	def __init__(self):
		self.tablero=chess.Board()
		self.turno=1
		

	def prompt_user(self):
		return

	#blancos =1
	#negros =0 		
	def actualizar_turno():
		if(self.tablero.turn):
			self.turno=1
		else:
			self.turno=0 	


	def turno_jugador():
		print("Turno jugador.... Esperando movida jugador, aprete h para mostrar disponibles")
		entrada =  input()
		if entrada == h or entrada == H:
			print(board.legal_moves)

		

			