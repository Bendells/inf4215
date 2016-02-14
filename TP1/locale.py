#!/usr/bin/python

import sys
import getopt
import re

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


    sys.stdout.write(K)
    search(Positions, K, C)




def solInitiale(Positions):
    minX = None
    maxX = None
    minY = None
    maxY = None

    pointsAntenne = []

    for point in Positions:
        pointsAntenne.append([point[0], point[1], 1])

    return pointsAntenne

def cout(pointsAntenne, K, C):

    sum = None

    for i in pointsAntenne :
        sum += i[2]

    return sum

def search(Positions, K, C):
    tmpInitial = 1000
    coeff = 0.003
    pasMax = 200
    palier = 40

    sol = solInitiale(Positions)

    for k in range(pasMax):
        for j in range(1, palier + 1):
            return 1



if __name__ == "__main__":
    main()


