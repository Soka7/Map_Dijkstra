from graphePondere import WeightedGraph
from dijkstra import GetPath

import csv

def LoadGraph(FilePath : str) -> WeightedGraph:
    """
    Make a graph based on a csv file.

    :param FilePath: The relative path to the file
    :type FilePath: str

    :return: A graph with all the informations of the file
    :rtype: WeightedGraph
    """
    Graph : WeightedGraph = WeightedGraph()

    FileContent : list = []

    with open(FilePath, newline = '', encoding = 'utf-8') as CsvFile:
        File = csv.reader(CsvFile, delimiter = ',')
        for Entry in File:
            if Entry[0][0] == ' ':
                Entry[0] = Entry[0][1:]
            if Entry[1][0] == ' ':
                Entry[1] = Entry[1][1:]
            if Entry[2][0] == ' ':
                Entry[2] = Entry[2][1:]
            FileContent.append(Entry)

    for Link in FileContent:
        Graph.AddLink(Link[0], Link[1], int(Link[2]))

    return Graph
