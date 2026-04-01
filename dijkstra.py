from graphePondere import Graphe_D

def Dijkstra(graphe, d, a, chemins = {}, utiliser =[]):
    utiliser.append(d)
    if d not in chemins.keys():
        chemins[d] = (d, 0)
    if d not in graphe.sommets():
        return "Le depart n'existe pas"
    if a not in graphe.sommets():
        return "L'arrivé n'existe pas"
    if a in utiliser:
        return chemins
    for sommet in graphe.sommets():
        if sommet in graphe.voisins(d).keys():
            if sommet not in chemins.keys() or chemins[d][1] + graphe.voisins(d)[sommet] < chemins[sommet][1]:
                chemins[sommet] = (d, chemins[d][1] + graphe.voisins(d)[sommet])
        else:
            if sommet not in chemins.keys():
                chemins[sommet] = (None, float("inf"))
    mini = None
    for element in chemins.keys():
        if not element in utiliser:
            if mini == None:
                mini = chemins[element][1]
            if chemins[element][1] < mini:
                mini = chemins[element][1]
    for element in chemins.keys():
        if element not in utiliser:
            if chemins[element][1] == mini:
                return Dijkstra(graphe, element, a, chemins, utiliser)

def getChemin(graphe, depart : any, fin : any) -> tuple:
    res = Dijkstra(graphe, depart, fin)
    taille = res[fin][1]
    chemin = []
    chemin.append(fin)

    while depart != fin:
        chemin.append(res[fin][0])
        fin = res[fin][0]
    chemin.reverse()
    return taille, chemin