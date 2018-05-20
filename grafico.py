import matplotlib.pyplot as plt


def escribir_fichero(texto):
    F = open("tiempos.txt", "w")
    F.write(texto)
    F.close()


def array_fichero(array):
    texto=""
    for i in array:
        texto+=str(i) + " "
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

def asintotico(greedy,minimax,abminimax):
    array_fichero(greedy)
    array_fichero(minimax)
    array_fichero(abminimax)
    plt.plot(array)
    #S1.plot(style='k--',kind="bar" )
    plt.xlabel('Turno')
    plt.ylabel('Porcentaje Poda')
    plt.title('Poda')
    plt.grid()
    plt.legend(loc='best')
    plt.show()
    plt.savefig('tiempoasintotico.png')
