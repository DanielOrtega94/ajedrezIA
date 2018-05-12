import chess


class Nodo(object):
    '''def __init__(self, movimiento=None,valor=None,hijos=None,padre=None):
                    self.padre=padre
                    self.movimiento = movimiento
                    self.valor = valor
                    self.hijos = []
                    self.profundidad=0
                    if padre:
                        self.profundidad = padre.profundidad + 1'''

    def __init__(self, movimiento=None, valor=None, tablero=None):
        self.tablero = tablero
        self.movimiento = movimiento
        self.valor = valor


# board.fen()

def imprime_hijos(nodo):
    for n in nodo.hijos:
        print(str(n.padre.movimiento) + " " + str(n.movimiento) +
              " " + str(n.valor) + " " + str(n.profundidad))

# necesito hacerlo recursivo


def poblar_hijos(lista, padre):
    tam = len(padre.hijos)
    for h in padre.hijos:
        lista.push(h.movimiento)
#		print(h.movimiento)
        anade_hijo(lista, h)
        print(len(h.hijos))
        poblar_hijos(lista, h)
        lista.pop()
