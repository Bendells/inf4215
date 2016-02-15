# Recursive Depth-first Search for CSP
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *

def csp_depthfirst_search(initialState):
    return csp_df_search(Node(initialState))

def csp_df_search(node):
    node.state.show()
    print '-----------------------------'
    if node.state.isGoal():
        node.state.show()
        return node
    else:
        for n in node.expand():
            if n.state.consistent():
                result = csp_df_search(n)
                if result != None:
                    return result
        return None
        
