#!/usr/bin/python

import sys
import getopt
import re
import Queue
import time
from smallestenclosingcircle import make_circle




class Antenne:
    'Notre abstraction d\'une antenne'

    def __init__(self, coordinates, positions):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.r = coordinates[2]
        self.positions = positions


    def cout(self, K, C):
        return K + C * self.r ** 2

    def __str__(self):
        coordinates = [self.x, self.y, self.r]
        ret = "Coordinates : " + (str(coordinates)) + "\n"
        ret += "Positions : " + str(self.positions) + "\n"
        return ret



class Etat:
    neighbours = []
    'Notre abstraction d\'un Etat'
    def __init__(self, antennes, ptsRestants):
        self.antennes = antennes
        self.ptsRestants = ptsRestants

    def __str__(self):
        ret = "Antennes :\n"
        ret += str(self.antennes[1])

        return ret

    def coutTotal(self, K, C):
        return sum([antenne.cout(K, C) for antenne in self.antennes])


    def etatsVoisins(self):

        # les etats voisin seront a une difference de l'etat orginale

        #on enleve un point de chaque antenne
        antIndex = 0

        for antenne in self.antennes:
            noAntenne = self.antennes[:antIndex] + self.antennes[(antIndex + 1):]
            posIndex = 0
            for position in antenne.positions:
                # We need to take out a point from the antenna and make a new state with it
                ptsSansPos = antenne.positions[:posIndex] + antenne.positions[(posIndex + 1):]
                #print ptsSansPos
                nvCercle = make_circle(ptsSansPos) # O(n) en complexite
                nvAntenne = Antenne(nvCercle, ptsSansPos) #antenne avec les points couverts

                #print nvAntenne

                # We now creates neighbouring states with the new antennas
                etat = Etat([noAntenne, nvAntenne], position)
                self.neighbours.append(etat)
                posIndex += 1

            antIndex += 1

            # We add a new point to the antenna
            ptIndex = 0
            for ptRestant in self.ptsRestants:
                nvPtsRestants = self.ptsRestants[:ptIndex] + self.ptsRestants[(ptIndex + 1):] #nouvelles listes des points
                nvPositions = [antenne.positions, ptRestant] #new antenna with an unsigned point
                nvCercle = make_circle(nvPositions)
                nvAntenne = Antenne(nvCercle, nvPositions)

                print nvAntenne

                etat = Etat([noAntenne, nvAntenne], nvPtsRestants)
                self.neighbours.append(etat)
                ptIndex += 1


        #new Atennas with remaining pts
        ptIndex = 0
        for ptRestant in self.ptsRestants:
            nvPtsRestants = self.ptsRestants[:ptIndex] + self.ptsRestants[(ptIndex + 1):] #nouvelles listes des points
            nvAntenne = Antenne(make_circle(ptRestant), [ptRestant])
            etat = Etat([self.antennes, nvAntenne], nvPtsRestants)
            self.neighbours.append(etat)
            ptIndex += 1






def search(Positions, K, C):

    K = float(K)
    C = float(C)

    posAntInitiale = make_circle(Positions)

    #Strategie : Notre etat initiale sera une antenne couvrant tous les points.
    #            Ainsi, ces voisins chercherons a minimiser le cout en trouvant
    #            des antennes de plus petits rayons et ainsi rrduire le cout.
    #            Nous assumons qu'un cout d'un etat est sa valeur de hashage.
    #print posAntInitiale

    a = Antenne(posAntInitiale, Positions)
    etatInitial = Etat([a], [])

    sortedQueue = Queue.PriorityQueue()
    sortedQueue.put_nowait((etatInitial.coutTotal(K, C), etatInitial))


    #etatInitial.etatsVoisins()

    while sortedQueue:
		state = sortedQueue.get_nowait()[1]

		if not state.unassigned:
			return [a.info() for a in state.antennas]
		else:
			state.etatsVoisins()
			for c in state.children:
				sortedQueue.put_nowait((c.cost(K,C), c))


    print etatInitial.neighbours[0]


def main(argv = None):
    #input = sys.stdin.read()
    input = "([(30,0),(10,10),(20,20),(30,40),(50,40)],200,1)"

    list1 = input.split("]")
    list2 = list1[1].strip(")").split(",");
    K = list2[1]
    C = list2[2]

    list1 = list1[0].split("[")
    list1 = list1[1]
    string = ''.join(list1)
    Positions = []

    for i in re.findall(r"\(((?:'[^']*'|[^()])*)\)", string):
        Positions.append(i.split(","))



    search(Positions, K, C)

if __name__ == "__main__":
    main()


