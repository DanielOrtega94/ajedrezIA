import math
import chess
import random
import copy

class Node:

    def __init__(self, move=None, parent=None, state=None, board=None):
        self.move = move  # the move that got us to this node - "None" for the root node
        self.parentNode = parent  # "None" for the root node
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = list(board.legal_moves)  # future child nodes
        # the only part of the state that the Node needs later
        self.playerJustMoved = board.turn

    def UCTSelectChild(self):
        """ Use the UCB1 formula to select a child node. Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * sqrt(2*log(self.visits)/c.visits to vary the amount of
            exploration versus exploitation.
        """
        s = sorted(self.childNodes, key = lambda c: c.wins/c.visits + math.sqrt(2*math.log(self.visits)/c.visits))[-1]
        return s
    
    
    def AddChild(self, m, s,board):
        """ Remove m from untriedMoves and add a new child node for this move.
            Return the added child node
        """
        n = Node(move = m, parent = self, state = s,board=board)
        self.untriedMoves.remove(m)
        self.childNodes.append(n)
        return n
    
    def Update(self, result):
        """ Update this node - one additional visit and result additional wins. result must be from the viewpoint of playerJustmoved.
        """
        self.visits += 1
        self.wins += result

#
    def __repr__(self):
        return "[M:" + str(self.move) + " W/V:" + str(self.wins) + "/" + str(self.visits) + " U:" + str(self.untriedMoves) + "]"

    def TreeToString(self, indent):
        s = self.IndentString(indent) + str(self)
        for c in self.childNodes:
             s += c.TreeToString(indent+1)
        return s

    def IndentString(self,indent):
        s = "\n"
        for i in range (1,indent+1):
            s += "| "
        return s

    def ChildrenToString(self):
        s = ""
        for c in self.childNodes:
             s += str(c) + "\n"
        return s


def choice(movs):
    nmovs=movs.count()
    stop=random.randint(0,nmovs )
   # print(stop)
    contador=0
    #print(movs)
    for i in movs:
        if(contador == stop):
            return i
        contador+=1    



def UCT(rootstate, itermax,board, verbose = False):
    """ Conduct a UCT search for itermax iterations starting from rootstate.
        Return the best move from the rootstate.
        Assumes 2 alternating players (player 1 starts), with game results in the range [0.0, 1.0]."""

    rootnode = Node(state = rootstate,board=board)

    for i in range(itermax):
        node = rootnode
        state = copy.deepcopy(rootstate)
        #state = rootstate.Clone()
        
       # print("Select")
        # Select
        while node.untriedMoves == [] and node.childNodes != []: # node is fully expanded and non-terminal
            node = node.UCTSelectChild()
            state.push(node.move)
        #print("expand")
        # Expand
        if node.untriedMoves != []: # if we can expand (i.e. state/node is non-terminal)
            m = random.choice(node.untriedMoves)
           # print(m) 
            state.push(m)
            node = node.AddChild(m,state,board) # add child and descend tree
        #print("rollout")    
        # Rollout - this can often be made orders of magnitude quicker using a state.GetRandomMove() function
        while not state.is_game_over() and list(state.legal_moves)  != []: # while state is non-terminal
            state.push(random.choice(list(state.legal_moves)))
         #   print(state)
          #  print("")

        #print("backpropagate")    
        # Backpropagate
        while node != None: # backpropagate from the expanded node and work back to the root node
            #print(state.result())
            node.Update(resultados(state)) # state is terminal. Update node with result from POV of node.playerJustMoved
            node = node.parentNode

    # Output some information about the tree - can be omitted
    if (verbose): 
        print(rootnode.TreeToString(0))
    else: 
        print(rootnode.ChildrenToString())

    return sorted(rootnode.childNodes, key = lambda c: c.visits)[-1].move # return the move that was most visited        
    
def resultados(board):
    if(board.result=="1/2-1/2"):
        return 0.0
    elif (board.result=="1-0"):
        return 0
    elif  (board.result=="0-1"): 
        return 1    
    return False