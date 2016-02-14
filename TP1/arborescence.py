#!/usr/bin/python

import sys
import getopt
import re
from smallestenclosingcircle import make_circle

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
    voisins = []
    'Notre abstraction d\'un Etat'
    def __init__(self, antennes, ptsRestants):
        self.antennes = antennes
        self.ptsRestants = ptsRestants

    def coutTotal(self, K, C):
        return sum([antenne.cout(K, C) for antenne in self.antennes])

    def etatsVoisins(self):

        # les etats voisin seront a une difference de l'etat orginale

        #on enleve un point de chaque antenne
        k = 0
        for position in self.antennes.positions:
            # We need to take out a point from the antenna and make a new state with it
            ptsSansPos = self.antennes.positions[:k] + self.antennes.positions[(k + 1):]
            #print ptsSansPos
            nvCercle = make_circle(ptsSansPos) # O(n) en complexite
            nvAntenne = Antenne(nvCercle, ptsSansPos) #antenne avec les points couverts

            print nvAntenne
            k += 1






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
    etatInitial = Etat(a, [])

    etatInitial.etatsVoisins()

    #print a.cout(K, C)



if __name__ == "__main__":
    main()


