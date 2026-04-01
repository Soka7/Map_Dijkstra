class Graphe_D:
    '''Weighted graph, can be oriented or not.'''
    def __init__(self):
        """
        Init the attribute to an empty dictionary

        :return: None
        """
        self.adj : dict = {}
        return None
    
    def affiche(self):
        """
        Print each each node and its neighbors.

        :return: None
        """
        for node in self.adj:
            print (node, self.adj[node])
    
    def addNode(self, node : any):
        """
        Add a node to the graph, orientedly.

        :param node: Node name
        :type node: any

        :return None

        :NOTE: Doesn't add the node if it already exists.
        """
        if node not in self.adj:
            self.adj[node] = {}
        return None
   
    def addLink(self, node1 : any, node2 : any, weight : float) -> None:
        """
        Add a link between 2 nodes with a wanted weight.

        :param node1 The starting node
        :type node1: any
        :param node2: The ending node
        :type node2: any
        :param weight: The weight of the link between the 2 nodes
        :type weight: float

        :return None:

        :NOTE: If the nodes don't exist, they'll be created.
        :NOTE: It doesn't add the link if it already exists.
        """
        if not node1 in self.adj:            
            self.addNode(node1)
        if not node2 in self.adj:
            self.addNode(node2)
        if not node2 in self.adj[node1]:
            self.adj[node1][node2] = weight
        return None
    
    def isLinked(self, node1 : any, node2 : any) -> bool:
        """
        Verify if 2 nodes are linked.

        :param node1 The starting node
        :type node1: any
        :param node2: The ending node
        :type node2: any

        :return: Whether or not they are linked
        :rtype: bool
        """
        return node2 in self.adj[node1]
    
    def getNodes(self) -> list:
        """
        Get all the nodes of the graph.
        
        :return: A list containing all the nodes of the graph
        :rtype: list
        """
        nodes : list = []
        for node in self.adj:
            nodes.append(node)
            for element in self.getNeighbors(node):
                if element not in nodes:
                    nodes.append(element)
        
        return nodes
    
    def getNeighbors(self, node : any) -> list:
        """
        Return the neighbors of a node.

        :param node: The node to get neighbors from
        :type node: any
        :return: The list of neighbors
        :rtype: list
        """
        return self.adj[node]