from graphePondere import WeightedGraph
from dijkstra import GetPath

import csv

A_ACCENTS = "àäâÂÄÀ"
E_ACCENTS = "êëéèÊËÉÈ"
I_ACCENTS = "ïîÏÎíÍ"
O_ACCENTS = "öôÖÔÓó"
U_ACCENTS = "ùûüÛÜÙ"

def ConvertStringToASCII(word : str) -> str:
    """
    Convert a string with common accent on a,e,i,o,u to a ASCII string.

    :param word: The string to convert
    :type word: str
    :return: An ASCII version of word
    :rtype: string
    """
    result : str = ""
    for letter in word:
        if letter in A_ACCENTS:
            result += "a"
        elif letter in E_ACCENTS:
            result += "e"
        elif letter in I_ACCENTS:
            result += "i"
        elif letter in O_ACCENTS:
            result += "o"
        elif letter in U_ACCENTS:
            result += "u"
        else:
            result += letter
    return result

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
        Graph.AddLink(ConvertStringToASCII(Link[0]), ConvertStringToASCII(Link[1]), int(Link[2])) # https://docs.python.org/3/library/unicodedata.html

    return Graph