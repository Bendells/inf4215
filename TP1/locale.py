#!/usr/bin/python

import sys
import getopt
import math
import random
import copy
import re
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



    def coutTotal(self, K, C):
        #print self
        #for antenne in self.antennes:
            #print antenne

        #print self.ptsRestants
        #print self.antennes

        return sum([antenne.cout(K, C) for antenne in self.antennes])


    def etatValide(self):
        if not self.ptsRestants:
            return True
        else:
            return False


def solVoisine(etat):
    #Strategy : We randomly take out a point from an antenna and give it randomly to another antenna
    #           if the deprived antenna has 0 points left, then we take it out of the state list
    #           we also need to make sure that the new solution is valid, such as every position is covered

    if len(etat.antennes) <= 1:
        return etat

    #The first antenna is gonna give a position to the second

    etatVoisin = copy.deepcopy(etat)

    antennes = random.sample(etatVoisin.antennes, 2)
    antToDeprive = antennes[0]
    antToGive = antennes[1]

    if(len(antToDeprive.positions) == 1):
        print "Only one antenna"
    #print antToDeprive
    #print antToGive










    return etat


#SolInitial, chaque point est une antenne
def solInitiale(Positions):

    antennes = [];
    for position in Positions:

        antennes.append(Antenne(make_circle([tuple(position)]), [position]))

    etat = Etat(antennes, [])

    return etat

def cout(pointsAntenne, K, C):

    sum = None

    for i in pointsAntenne :
        sum += i[2]

    return sum

def critereMetropolis(delta, temp):
    if delta > 0:
        return True

    random.seed()

    print temp
    return math.exp(delta/temp) >= random.random()

def search(Positions, K, C):

    tmpInitial = 1000
    coeff = 0.003
    pasMax = 200
    palier = 40

    K = float(K)
    C = float(C)

    sol = solInitiale(Positions)
    meilleurSol = sol
    delta = 0

    print sol.coutTotal(K, C)
    tmp = tmpInitial
    for k in range(1, pasMax+1):
        for j in range(1, palier + 1):

            tmpSolution = solVoisine(sol)

            delta = sol.coutTotal(K,C) - tmpSolution.coutTotal(K,C)

            #critere metropolis
            if critereMetropolis(delta, tmp):
                sol = tmpSolution
                if sol.coutTotal(K,C) < meilleurSol.coutTotal(K,C):
                    meilleurSol = sol


        tmp *= coeff



    return meilleurSol



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


