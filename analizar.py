import ast
import matplotlib.pyplot as plt
import numpy as np

greedy = []
minimax = []
ab_minimax = []
minimax_a = []

porcentaje = []


def grafico(array, mediana):
    texto = "mediana " + str(mediana) + "%"
    contador = 0
    # for i in array:
    #    plt.text(contador,i,str(i),fontsize=10)
    #    contador+=1

    plt.plot(array,  "-o")
    plt.xlabel('Turno')
    plt.ylabel('Porcentaje Poda')
    plt.title('Poda')
    plt.grid()
    plt.text(10, 40, texto, fontsize=12)
    plt.legend(loc='best')
    plt.show()
    plt.savefig('porcentajepoda.png')


def tiempo(greedy, mini, ab):
    plt.plot(greedy, marker='x', linestyle=':', color='b', label="greedy")
    plt.plot(mini,  marker='*', linestyle='-', color='g', label="minimax")
    plt.plot(ab,  marker='o', linestyle='--', color='r', label="ab_minimax")
    plt.xlabel('Turno')
    plt.ylabel('segundos')
    plt.title('tiempos')
    plt.grid()
    plt.legend(loc='best')
    plt.show()


def tiempo_1(mini, ab):
    plt.plot(mini, marker='x', linestyle=':', color='b', label="minimax")
    plt.plot(ab,  marker='*', linestyle='-', color='g', label="minimax_arbol")
    plt.xlabel('Turno')
    plt.ylabel('segundos')
    plt.title('tiempos')
    plt.grid()
    plt.legend(loc='best')
    plt.show()


f = open("tiempos.txt")

linea = f.readline()
flag = True

'''
while linea != "":
    try:
        greedy.append(float(linea))  # greedy
    except ValueError:
        break
    linea = f.readline()
    minimax.append(float(linea))  # minmax
    linea = f.readline()
    ab_minimax.append(float(linea))  # ab
    linea = f.readline()
    porcentaje.append(float(linea))  # %
    linea = f.readline()
'''

# print(len(porcentaje))
#media = np.median(porcentaje)
# print(media)
# grafico(porcentaje,media)
# tiempo(minimax,ab_minimax)


while linea != "":
    try:
        minimax.append(float(linea))  # greedy
    except ValueError:
        break
    linea = f.readline()
    minimax_a.append(float(linea))  # ab
    linea = f.readline()

f.close()

tiempo_1(minimax, minimax_a)


# print(greedy)
# print(minimax)
#print(porcentaje)
