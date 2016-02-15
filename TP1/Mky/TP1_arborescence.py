from astar_search import *
from bestfirst_search import *
from state import *
from node import *
import time


class AntennaState(State):
    def __init__(self, Positions, K, C):
        self.positions = Positions
        self.K = K
        self.C = C
        self.dimensions = self._getSizeGrid(Positions)
        self.grid = self._initializeGrid(self.dimensions)
        self.antennaRay = 1
        self.counter = 1
        self.antennas = []
        
    def equals(self,state):
        return self.grid == state.grid

    def show(self):
        for row in self.grid:
            for cell in row:
                print '{:2}'.format(cell),
            print

    def executeAction(self, action):
        self.counter += 1
        (dimX, dimY) = self.dimensions
        for i in range(dimX):
            for j in range(dimY):
                position = (i,j)
                positionAntenna = (action[0], action[1])
                distance = self.getDistance(position, positionAntenna)
                if (distance <= action[2] and self.grid[i][j] == '*'):
                    self.grid[i][j] = self.counter
        self.positions.remove(action[3])
        self.antennas.append((action[0], action[1], action[2]))

    def possibleActions(self):
        actions = []
        (dimX, dimY) = self.dimensions
        for i in range(dimX):
            for j in range(dimY):
                positionAntenna = (i,j)
                for position in self.positions:
                    distance = self.getDistance(position, positionAntenna)
                    antennaRay = self.findAntennaRay(positionAntenna)
                    if(distance <= self.antennaRay and self.grid == '*'):
                        actions.append((i, j, self.antennaRay, position))
        return actions

    def findAntennaRay(self, positionAntenna):
        antennaRay = 1
        trouve = False
        while not trouve:
            for position in self.positions:
                distance = self.getDistance(position, positionAntenna)
                if distance <= antennaRay:
                    trouve = True
            antennaRay += 1
        return antennaRay

    def isSuperposing(self, position):
        (dimX, dimY) = self.dimensions
        for i in range(dimX):
            for j in range(dimY):
                distance = self.getDistance((i,j), position)
                if distance <= self.antennaRay and self.grid[i][j] != '*':
                    return True
        return False

    def getDistance(self, position, positionAntenna):
        distance = math.sqrt(math.pow(position[0] - positionAntenna[0], 2) + math.pow(position[1] - positionAntenna[1], 2))
        return distance

    def cost(self,action):
        return self.K + self.C * math.pow(action[2], 2)
    
    def isGoal(self):
        return len(self.positions) == 0

    def heuristic(self):
        return self.K + self.C * math.pow(self.antennaRay, 2) / self.counter

    def _initializeGrid(self, dimensions):
        (dimX,dimY) = dimensions
        grid = [[0 for y in range(dimY)] for x in range(dimX)]
        for i in range(dimX):
            for j in range(dimY):
                grid[i][j] = '*'
        return grid

    def _getSizeGrid(self, Positions):
        (x,y) = (-1, -1)
        for position in Positions:
            if position[0] > x:
                x = position[0]
            if position[1] > y:
                y = position[1]
        return (x,y)

def search(Positions, K, C):
    solution = bestfirst_search(AntennaState(Positions, K, C))


Positions = [(30,0),(10,10),(20,20),(30,40),(50,40)]
K = 200
C = 1

## Lancement ##
start = time.time()
search(Positions, K, C)
end = time.time()
print '{} seconds'.format(end-start)