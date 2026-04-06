from graphePondere import WeightedGraph

def CalcDistances(Graph : WeightedGraph, Node : any, End : any, Paths : dict = {}, Visited : list = []) -> dict:
    """
    Dijkstra algorithm made by our fellow classmate Aaron.
    Apply a recursive dijkstra algorithm to a given graph.

    :param graph: The graph to search distances on
    :type Graph: WeightedGraph
    :param Node: The starting node
    :type Node: any
    :param End: The end point of the distance
    :type End: any
    :param Paths: Stores all the current pathes of nodes
    :type Paths: dict
    :param Visited: the list of already visited nodes
    :type Visited: list

    :return: A dictionary of the shortest distance from the starting node to every node of the graph.
    :rtype: dict
    """
    Visited.append(Node)
    
    if Node not in Paths.keys():
        Paths[Node] = (Node, 0)
    if Node not in Graph.GetNodes():
        return "This starting point doesn't exist"
    elif End not in Graph.GetNodes():
        return "This end point doesn't exist"
    elif End in Visited:
        return Paths
    
    for Edge in Graph.GetNodes():
        if Edge in Graph.GetNeighbors(Node).keys():
            if Edge not in Paths.keys() or Paths[Node][1] + Graph.GetNeighbors(Node)[Edge] < Paths[Edge][1]:
                Paths[Edge] = (Node, Paths[Node][1] + Graph.GetNeighbors(Node)[Edge])
        else:
            if Edge not in Paths.keys():
                Paths[Edge] = (None, float("inf"))

    Minimum : float = float('inf')

    for Edge in Paths.keys():
        if not Edge in Visited:
            if Paths[Edge][1] < Minimum:
                Minimum = Paths[Edge][1]

    for Edge in Paths.keys():
        if Edge not in Visited:
            if Paths[Edge][1] == Minimum:
                return CalcDistances(Graph, Edge, End, Paths, Visited)
    return None

def GetPath(Graph : WeightedGraph, Start : any, End : any) -> tuple:
    """
    Give the full optimal path from a node to another on a given graph.

    :param Graph: The graph to search distances on
    :type Graph: WeightedGraph
    :param Start: The starting node
    :type Start: any
    :param End: The end point of the distance
    :type End: any

    :return: A 2-uplet, the first element is the distance of the path (integer) the second is the path (list)
    :rtype: tuple
    """
    Distances : dict = CalcDistances(Graph, Start, End)
    OptimalPathLenght : float = Distances[End][1]

    Path : list = []
    Path.append(End)

    while Start != End:
        Path.append(Distances[End][0])
        End = Distances[End][0]

    Path.reverse()
    return OptimalPathLenght, Path