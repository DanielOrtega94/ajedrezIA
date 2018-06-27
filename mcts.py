import math
import chess
import random
import copy

class Node:

    def __init__(self, move=None, parent=None, state=None, board=None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = list(board.legal_moves)
        self.playerJustMoved = board.turn

    def UCTSelectChild(self):
        s = sorted(self.childNodes, key=lambda c: c.wins / c.visits +
                   math.sqrt(2 * math.log(self.visits) / c.visits))[-1]
        return s

    def AddChild(self, m, s, board):

        n = Node(move=m, parent=self, state=s, board=board)
        self.untriedMoves.remove(m)
        self.childNodes.append(n)
        return n

    def Update(self, result):
        self.visits += 1
        self.wins += result

    def __repr__(self):
        return "[M:" + str(self.move) + " W/V:" + str(self.wins) + "/" + str(self.visits) + " U:" + str(self.untriedMoves) + "]"


def choice(movs):
    nmovs = movs.count()
    stop = random.randint(0, nmovs)
    contador = 0
    for i in movs:
        if(contador == stop):
            return i
        contador += 1


def UCT(rootstate, itermax, board):
    rootnode = Node(state=rootstate, board=board)

    for i in range(itermax):
        node = rootnode
        state = copy.deepcopy(rootstate)

        # Select
        while node.untriedMoves == [] and node.childNodes != []:
            node = node.UCTSelectChild()
            state.push(node.move)

        # Expand
        if node.untriedMoves != []:
            m = random.choice(node.untriedMoves)
            state.push(m)
            node = node.AddChild(m, state, board)

        # rollout
        while not state.is_game_over()and list(state.legal_moves) != []:  # while state is non-terminal
            state.push(random.choice(list(state.legal_moves)))

        # Backpropagate
        while node != None:
            node.Update(resultados(state))
            node = node.parentNode

    #print(rootnode.ChildrenToString())
    return sorted(rootnode.childNodes, key=lambda c: c.visits)[-1].move


def resultados(board):
    var = str(board.result())
    if(var == "1/2-1/2"):
        return 1.1
    elif (var == "1-0"):
        return 0.0
    elif (var == "0-1"):
        return 2.0
    else:
        return 1.1
