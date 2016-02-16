#!/usr/bin/python

import sys
import getopt
import re
import Queue
import copy
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
        self.neighbours = list()
        self.antennes = antennes
        self.ptsRestants = ptsRestants
        # "Points Restand dans le constructeur : " + str(self.ptsRestants)

    def __str__(self):
        return str([antenne.ret() for antenne in self.antennes])


    def ret(self):
        return [antenne.ret() for antenne in self.antennes]
		
    def coutTotal(self, K, C):

        return sum([antenne.cout(K, C) for antenne in self.antennes])


    def etatValide(self):
        if not self.ptsRestants:
            return True
        else:
            return False

    def etatsVoisins(self):

        # les etats voisin seront a une difference de l'etat orginale
        #

        #on enleve un point de chaque antenne
        for position in self.ptsRestants:
            nvAntennePos = make_circle([position])
            nvAntenne = Antenne(nvAntennePos, [position])
            
            nvPtsRestantes = copy.deepcopy(self.ptsRestants)
            
            nvPtsRestantes.remove(position)
            
            nvListeAntennes = copy.deepcopy(self.antennes)
            nvListeAntennes.append(nvAntenne)
            nvEtat = Etat(nvListeAntennes, nvPtsRestantes)
            self.neighbours.append(nvEtat)

        indexAnt = 0 # necessaire pour garder la
        for antenne in self.antennes:
            for position in self.ptsRestants:
                nvListePos = copy.deepcopy(antenne.positions)
                nvListePos.append(position)
                nvAntennePos = make_circle(nvListePos)
                nvAntenne = Antenne(nvAntennePos, nvListePos)
                nvPtsRestantes = copy.deepcopy(self.ptsRestants)
                nvPtsRestantes.remove(position)
                nvListeAntennes = copy.deepcopy(self.antennes)

                del nvListeAntennes[indexAnt]
                nvListeAntennes.append(nvAntenne)
                nvEtat = Etat(nvListeAntennes, nvPtsRestantes)
                self.neighbours.append(nvEtat)
            indexAnt += 1

def solInitiale(Positions):

    antennes = [];

    position = Positions.pop(0)
    antennes.append(Antenne(make_circle([tuple(position)]), [position]))

    etat = Etat(antennes, Positions)

    return etat

def search(Positions, K, C):

    K = float(K)
    C = float(C)

    #Strategie : Notre etat initiale sera une antenne couvrant tous les points.
    #            Ainsi, ces voisins chercherons a minimiser le cout en trouvant
    #            des antennes de plus petits rayons et ainsi rrduire le cout.
    #            Nous assumons qu'un cout d'un etat est sa valeur de hashage.
    #print posAntInitiale


    #etatInitial = solInitiale(Positions)
    etatInitial = Etat([], Positions)




    #print etatInitial.coutTotal(K,C)
    frontiere = Queue.PriorityQueue()
    frontiere.put_nowait((etatInitial.coutTotal(K, C), etatInitial))

    visited = set() #visited costs, our hashin
    while frontiere:
        #print queue.empty()

        etat = frontiere.get_nowait()[1]
        #print len(etat.antennes) == len(Positions)
        if etat.etatValide():
            #print etat
            return etat.ret()
        else:
            etat.etatsVoisins()
            for c in etat.neighbours:

                coutTotal = c.coutTotal(K,C)
                #frontiere.put_nowait((coutTotal, c))
                #print coutTotal
                if coutTotal not in visited:
                    frontiere.put_nowait((coutTotal, c))
                    visited.add(coutTotal)





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

    print str(result)


if __name__ == '__main__':
    main()



