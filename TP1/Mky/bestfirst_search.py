# Best-first Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *

def bestfirst_search(initialState):
    step = 0
    frontier = [Node(initialState)]
    while frontier:
        node = frontier.pop(0)
        step += 1
        # node.state.show()
        # print '----------------'
        if node.state.isGoal():
            node.state.show()
            print 'Cost:', node.g
            print 'Steps:', step
            return node
        elif node.isRepeated():
            continue
        else:
            frontier = frontier + node.expand()
            frontier.sort(cmp = lambda n1,n2: -1 if n1.h < n2.h else (1 if n1.h > n2.h else 0))
    return None
