from graphePondere import Graphe_D
from dijkstra import getChemin
import csv 
g = Graphe_D()

file : list = []

with open('arrets.csv', newline='') as csvfile:
    entry = csv.reader(csvfile, delimiter=',')
    for i in entry:
        if i[0][0] == ' ':
            i[0] = i[0][1:]
        if i[1][0] == ' ':
            i[1] = i[1][1:]
        if i[2][0] == ' ':
            i[2] = i[2][1:]
        file.append(i)

for i in file:
    g.ajouter_sommet(i[0])
    g.ajouter_sommet(i[1])
    g.ajouter_arc(i[0], i[1], int(i[2]))

print(getChemin(g, 'Bouguenais centre', 'Neustrie'))

