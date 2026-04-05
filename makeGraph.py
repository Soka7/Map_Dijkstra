from graphePondere import Graphe_D
from dijkstra import getPath

import csv 

def loadGraphe(filePath : str) -> Graphe_D:
    """
    Make a graph based on a csv file.

    :param filePath: The relative path to the file
    :type filePath: str

    :return: A graph with all the informations of the file
    :rtype: Graphe_D
    """
    graph : Graphe_D = Graphe_D()

    fileContent : list = []

    with open(filePath, newline = '') as csvfile:
        file = csv.reader(csvfile, delimiter = ',')
        for entry in file:
            if entry[0][0] == ' ':
                entry[0] = entry[0][1:]
            if entry[1][0] == ' ':
                entry[1] = entry[1][1:]
            if entry[2][0] == ' ':
                entry[2] = entry[2][1:]
            fileContent.append(entry)

    for link in fileContent:
        graph.addLink(link[0], link[1], int(link[2]))

    return graph

g = loadGraphe("arrets.csv")
print(getPath(g, "Le Cardo", "Roche Maurice"))

# :BUG: IT DOESN'T WORK FOR NAME THAT AREN'T IN THE ASCII TABLES like é,è,ë