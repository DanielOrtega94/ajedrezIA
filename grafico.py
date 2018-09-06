import ast
import matplotlib.pyplot as plt
import numpy as np

greedy = []
minimax = []
ab_minimax = []
minimax_a = []
porcentaje = []


def escribir_fichero(texto):
    F = open("tiempos.txt", "w")
    F.write(texto)
    F.close()


def array_fichero(array):
    texto = ""
    for i in array:
        texto += str(i) + " "
        escribir_fichero(texto)
    escribir_fichero("\n")


def porcentaje(array):
    array_fichero(array)
    plt.plot(array)
    #S1.plot(style='k--',kind="bar" )
    plt.xlabel('Turno')
    plt.ylabel('Porcentaje Poda')
    plt.title('Poda')
    plt.grid()
    plt.legend(loc='best')
    plt.show()
    plt.savefig('porcentajepoda.png')


def asintotico(greedy, minimax, abminimax):
    array_fichero(greedy)
    array_fichero(minimax)
    array_fichero(abminimax)
    plt.plot(array)
    plt.xlabel('Turno')
    plt.ylabel('Porcentaje Poda')
    plt.title('Poda')
    plt.grid()
    plt.legend(loc='best')
    plt.show()
    plt.savefig('tiempoasintotico.png')


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


def graficar():
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
'''
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
'''


def profundidades_mini():
    cuatro = 2.118420124053955
    cinco = 49.9095823764801
    seis = 1210.511376619339
    mini = [cuatro, cinco, seis]
    # siete=
    posiciones = [0, 1, 2]
    plt.bar(posiciones[0], cuatro)
    plt.bar(posiciones[1], cinco)
    plt.bar(posiciones[2], seis)
    plt.text(posiciones[0], cuatro, str(round(cuatro, 1)), fontsize=6)
    plt.text(posiciones[1], cinco, str(round(cinco, 1)), fontsize=6)
    plt.text(posiciones[2], seis, str(round(seis, 1)), fontsize=6)
    plt.plot(mini, marker='x', linestyle=':', color='b', label="minimax")
    #plt.plot(cuatro, marker='x', linestyle=':', color='b', label="cuatro")
    #plt.plot(cinco,  marker='*', linestyle='-', color='r', label="cinco")
    #plt.plot(seis,  marker='*', linestyle='-', color='g', label="seis")
    #plt.plot(siete,  marker='*', linestyle='-', color='g', label="siete")
    plt.xlabel('Profundidades')
    plt.xticks(posiciones, ["4", "5", "6"], rotation=45)
    plt.ylabel('segundos')
    plt.title('Tiempos Profundidades Minimax')
    plt.grid()

    plt.show()


def profundidades_ab():
    cuatro = 1.8808352947235107
    cinco = 47.39628863334656
    seis = 1117.0138058662415
    mini = [cuatro, cinco, seis]
    # siete=
    posiciones = [0, 1, 2]
    plt.bar(posiciones[0], cuatro)
    plt.bar(posiciones[1], cinco)
    plt.bar(posiciones[2], seis)
    plt.text(posiciones[0], cuatro, str(round(cuatro, 1)), fontsize=6)
    plt.text(posiciones[1], cinco, str(round(cinco, 1)), fontsize=6)
    plt.text(posiciones[2], seis, str(round(seis, 1)), fontsize=6)
    plt.plot(mini, marker='x', linestyle=':', color='b', label="minimax")

    #plt.plot(cuatro, marker='x', linestyle=':', color='b', label="cuatro")
    #plt.plot(cinco,  marker='*', linestyle='-', color='r', label="cinco")
    #plt.plot(seis,  marker='*', linestyle='-', color='g', label="seis")
    #plt.plot(siete,  marker='*', linestyle='-', color='g', label="siete")
    plt.xlabel('Profundidades')
    plt.xticks(posiciones, ["4", "5", "6"], rotation=45)
    plt.ylabel('segundos')
    plt.title('Tiempos Profundidades Minimax_AB')
    plt.grid()

    plt.show()


def profundidades_mcts():
    cuatro = 36.49257731437683
    cinco = 55.4264612197876
    seis = 69.9779794216156
    siete = 86.68532061576843
    mini = [cuatro, cinco, seis, siete]

    posiciones = [0, 1, 2, 3]
    plt.bar(posiciones[0], cuatro)
    plt.bar(posiciones[1], cinco)
    plt.bar(posiciones[2], seis)
    plt.bar(posiciones[3], siete)
    plt.text(posiciones[0], cuatro, str(round(cuatro, 1)), fontsize=6)
    plt.text(posiciones[1], cinco, str(round(cinco, 1)), fontsize=6)
    plt.text(posiciones[2], seis, str(round(seis, 1)), fontsize=6)
    plt.text(posiciones[3], siete, str(round(siete, 1)), fontsize=6)
    plt.plot(mini, marker='x', linestyle=':', color='b', label="cuatro")
    #plt.plot(cinco,  marker='*', linestyle='-', color='r', label="cinco")
    #plt.plot(seis,  marker='*', linestyle='-', color='g', label="seis")
    #plt.plot(siete,  marker='*', linestyle='-', color='g', label="siete")
    plt.xlabel('iteraciones')
    plt.xticks(posiciones, ["500", "750", "1000", "1250"], rotation=45)
    plt.ylabel('segundos')
    plt.title('Tiempos Profundidades MCTS')
    plt.grid()

    plt.show()


def comparativa():
    cuatro_a = 1.8808352947235107
    cinco_a = 45.39628863334656
    seis_a = 1110.0138058662415
    mini1 = [cuatro_a, cinco_a, seis_a]
    cuatro = 2.118420124053955
    cinco = 49.9095823764801
    seis = 1210.511376619339
    mini = [cuatro, cinco, seis]

    posiciones = [0, 1, 2]
    plt.bar(posiciones[0], cuatro)
    plt.bar(posiciones[1], cinco)
    plt.bar(posiciones[2], seis)
    plt.bar(posiciones[0], cuatro_a)
    plt.bar(posiciones[1], cinco_a)
    plt.bar(posiciones[2], seis_a)

    plt.plot(mini1, marker='x', linestyle=':', color='b', label="cuatro")
    plt.plot(mini,  marker='*', linestyle='-', color='r', label="cinco")
    #plt.plot(seis,  marker='*', linestyle='-', color='g', label="seis")
    #plt.plot(siete,  marker='*', linestyle='-', color='g', label="siete")
    plt.xlabel('Profundidades')
    plt.xticks(posiciones, ["4", "5", "6"], rotation=45)
    plt.ylabel('segundos')
    plt.title('Comparativa Tiempos y profundidades')
    plt.grid()

    plt.show()


def tiempo():
    greedy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mini = [2.4, 6.8, 6, 17, 17.5, 17, 7.5, 7.8,
            8.7, 14, 14.9, 14, 15, 13.5, 16, 11]
    ab = [0.3, 2.3, 1.7, 7.5, 8, 7.4, 4.7, 5.4,
          5.6, 10, 10.5, 10, 11.5, 10, 12, 8]
    mcts = [61.8, 64.8, 62, 62.8, 64, 61.5, 62.3, 63,
            62, 63.8, 61.9, 64, 62.5, 66, 62.8, 61]
    plt.plot(greedy, marker='x', linestyle=':', color='b', label="greedy")
    plt.plot(mini,  marker='*', linestyle='-', color='g', label="minimax")
    plt.plot(ab,  marker='o', linestyle='--', color='r', label="ab_minimax")
    plt.plot(mcts,  marker='x', linestyle=':', color='y', label="mcts")
    plt.xlabel('Turno')
    plt.ylabel('segundos')
    plt.title('tiempos')
    plt.grid()
    plt.legend(loc='best')
    plt.show()

# profundidades_mini()
# profundidades_ab()
# comparativa()
# profundidades_mcts()
tiempo()
