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

    def ret(self):
        return self.x, self.y, self.r

    def __str__(self):
        coordinates = [self.x, self.y, self.r]
        ret = "Coordinates : " + (str(coordinates)) + "\n"
        ret += "Positions : " + str(self.positions) + "\n"
        return ret



class Etat:

    'Notre abstraction d\'un Etat'
    def __init__(self, antennes, ptsRestants):
        self.antennes = antennes
        self.ptsRestants = ptsRestants
        self.neighbours = list()

    def __str__(self):
        ret = "Antennes :\n"
        ret += str(self.antennes[1])

        return ret

    def coutTotal(self, K, C):
        #print self
        #for antenne in self.antennes:
            #print antenne

        #print self.ptsRestants
        #print self.antennes

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
                if not ptsSansPos:
                    continue
                nvCercle = make_circle(ptsSansPos) # O(n) en complexite

                nvAntenne = Antenne(nvCercle, ptsSansPos) #antenne avec les points couverts

                #print nvAntenne

                # We now creates neighbouring states with the new antennas
                #print "Position a mettre : " + str(position)
                if not noAntenne:
                    etat = Etat([nvAntenne], [position])
                else:
                    etat = Etat([noAntenne,nvAntenne], [position])

                self.neighbours.append(etat)
                posIndex += 1

            antIndex += 1

            # We add a new point to the antenna
            ptIndex = 0
            for ptRestant in self.ptsRestants:
                nvPtsRestants = self.ptsRestants[:ptIndex] + self.ptsRestants[(ptIndex + 1):] #nouvelles listes des points
                nvPositions = antenne.positions + [ptRestant] #new antenna with an unsigned point
                #print "Nv Positions Restantes: " + str(nvPtsRestants)
                #print "Nv Positions : " + str(nvPositions)
                nvCercle = make_circle(nvPositions)

                nvAntenne = Antenne(nvCercle, nvPositions)

                #print nvAntenne

                if not noAntenne:
                    etat = Etat([nvAntenne], nvPtsRestants)
                else:
                    etat = Etat([noAntenne, nvAntenne], nvPtsRestants)
                #etat = Etat([noAntenne, nvAntenne], nvPtsRestants)
                self.neighbours.append(etat)
                ptIndex += 1


        #new Atennas with remaining pts
        ptIndex = 0
        for ptRestant in self.ptsRestants:
            nvPtsRestants = self.ptsRestants[:ptIndex] + self.ptsRestants[(ptIndex + 1):] #nouvelles listes des points
            #print ptRestant
            nvCercle = make_circle([ptRestant])
            #print nvCercle
            nvAntenne = Antenne(nvCercle, [ptRestant])
            #etat = Etat([self.antennes, nvAntenne], nvPtsRestants)
            #self.neighbours.append(etat)
            ptIndex += 1

        #Sprint "les voisins " + str(self.neighbours)





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

    print etatInitial.coutTotal(K,C)
    sortedQueue = Queue.PriorityQueue()
    sortedQueue.put_nowait((etatInitial.coutTotal(K, C), etatInitial))


    #etatInitial.etatsVoisins()
    visited = set() #visited costs, our hashin
    while sortedQueue:
        etat = sortedQueue.get_nowait()[1]
        if len(etat.antennes) == len(Positions):
			return [a.ret() for a in etat.antennes]
        else:
            etat.etatsVoisins()
            for c in etat.neighbours:
                #print c
                coutTotal = c.coutTotal(K,C)
                if coutTotal not in visited:
                    sortedQueue.put_nowait((coutTotal, c))
                    visited.add(coutTotal)


    #print etatInitial.neighbours[0]


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



    result = search(Positions, K, C)

    print result

if __name__ == '__main__':
    main()


