from graphePondere import Graphe_D

def Dijkstra(graph : Graphe_D, node : any, end : any, paths : dict = {}, visited : list = []) -> dict:
    """
    Dijkstra algorithm made by our fellow classmate Aaron.
    Apply a recursive dijkstra algorithm to a given graph.

    :param graph: The graph to search distances on
    :type graphe: Graphe_D
    :param node: The starting node
    :type node: any
    :param end: The end point of the distance
    :type end: any
    :param paths: Stores all the current pathes of nodes
    :type paths: dict
    :param visited: the list of already visited nodes
    :type visited: list

    :return: A dictionary of the shortest distance from the starting node to eevryno of the graph.
    :rtype: dict
    """
    visited.append(node)
    
    if node not in paths.keys():
        paths[node] = (node, 0)
    if node not in graph.getNodes():
        return "This starting point doesn't exist"
    elif end not in graph.getNodes():
        return "This end point doesn't exist"
    elif end in visited:
        return paths
    
    for sommet in graph.getNodes():
        if sommet in graph.getNeighbors(node).keys():
            if sommet not in paths.keys() or paths[node][1] + graph.getNeighbors(node)[sommet] < paths[sommet][1]:
                paths[sommet] = (node, paths[node][1] + graph.getNeighbors(node)[sommet])
        else:
            if sommet not in paths.keys():
                paths[sommet] = (None, float("inf"))

    mini : float = float('inf')

    for element in paths.keys():
        if not element in visited:
            if paths[element][1] < mini:
                mini = paths[element][1]

    for element in paths.keys():
        if element not in visited:
            if paths[element][1] == mini:
                return Dijkstra(graph, element, end, paths, visited)
    return None

def getPath(graph : Graphe_D, start : any, end : any) -> tuple:
    """
    Give the full optimal path from a node to another on a given graph.

    :param graph: The graph to search distances on
    :type graph: Graphe_D
    :param start: The starting node
    :type start: any
    :param end: The end point of the distance
    :type end: any

    :return: A 2-uplet, the first element is the distance of the path (integer) the second is the path (list)
    :rtype: tuple
    """
    distances : dict = Dijkstra(graph, start, end)
    optimalPathLenght = distances[end][1]

    path : list = []
    path.append(end)

    while start != end:
        path.append(distances[end][0])
        end = distances[end][0]

    path.reverse()
    return optimalPathLenght, path