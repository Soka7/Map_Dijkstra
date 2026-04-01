from ACT2_creation_graphe import Graphe_D
g = Graphe_D()
g.ajouter_arc('A', 'D', 2)
g.ajouter_arc('A', 'G', 2)
g.ajouter_arc('B', 'A', 1)
g.ajouter_arc('C', 'B', 1)
g.ajouter_arc('C', 'G', 3)
g.ajouter_arc('C', 'F', 2)
g.ajouter_arc('D', 'G', 4)
g.ajouter_arc('D', 'S', 7)
g.ajouter_arc('E', 'A', 5)
g.ajouter_arc('E', 'B', 3)
g.ajouter_arc('E', 'C', 2)
g.ajouter_arc('F', 'D', 1)
g.ajouter_arc('F', 'S', 6)
g.ajouter_arc('G', 'F', 4)


def Dijkstra(graphe, d, a, chemins={}, pred={}, utiliser=[]):
    utiliser.append(d)

    if d not in chemins:
        chemins[d] = 0

    if a in utiliser:
        chemin = []
        etape = a
        while etape != d_depart:
            chemin.append(etape)
            etape = pred[etape]
        chemin.append(d_depart)
        chemin.reverse()
        print(chemin, "coût :", chemins[a])
        return

    for sommet in graphe.sommets():
        if sommet in graphe.voisins(d):
            nouveau = chemins[d] + graphe.voisins(d)[sommet]
            if sommet not in chemins or nouveau < chemins[sommet]:
                chemins[sommet] = nouveau
                pred[sommet] = d
        elif sommet not in chemins:
            chemins[sommet] = float("inf")

    mini = min(chemins[e] for e in chemins if e not in utiliser)
    prochain = [e for e in chemins if e not in utiliser and chemins[e] == mini][0]
    Dijkstra(graphe, prochain, a, chemins, pred, utiliser)

d_depart = "E"
Dijkstra(g, d_depart, "S")