"""Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) 
con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
la maquina responde con su movimiento y se verifica el estado del juego;
no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

Requerimientos
Implementa las siguientes características:
el tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos 
(la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis
cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro (dicho cuadro se considera como libre)
la apariencia de tablero debe de ser igual a la presentada en el ejemplo.
implementa las funciones definidas para ti en el editor."""

from random import randrange

def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def make_list_of_free_fields(board):
	libres = []
	for row in range (3):
		for colum in range (3):
			if board[row][colum] not in ['O','X']:
				libres.append((row,colum))
	return libres

# Interacion 1: row[1,2,3] J = 0 / i = 1,2,3 
# Interacion 2: row[4,5,6] J = 1 / i = 1,2,3 
# Interacion 3: row[7,8,9] J = 2 / i = 1,2,3 

board = [[3 * j + i + 1 for i in range (3)] for j in range (3)]
board[1][1] = 'X'
libres = make_list_of_free_fields(board)
human_turn = True
while len(libres):
	display_board(board)
