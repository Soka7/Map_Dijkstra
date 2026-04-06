class WeightedGraph:
    '''Weighted graph, can be oriented or not.'''
    def __init__(self):
        """
        Init the attribute to an empty dictionary

        :return: None
        """
        self.Adj : dict = {}
        return None
    
    def Show(self):
        """
        Print each each node and its neighbors.

        :return: None
        """
        for Node in self.Adj:
            print (Node, self.Adj[Node])
    
    def AddNode(self, Node : any):
        """
        Add a node to the graph, orientedly.

        :param Node: Node name
        :type Node: any

        :return None

        :NOTE: Doesn't add the node if it already exists.
        """
        if Node not in self.Adj:
            self.Adj[Node] = {}
        return None
   
    def AddLink(self, Node1 : any, Node2 : any, Weight : float) -> None:
        """
        Add a link between 2 nodes with a wanted weight.\n

        :param Node1: The starting node
        :type Node1: any
        :param Node2: The ending node
        :type Node2: any
        :param Weight: The weight of the link between the 2 nodes
        :type Weight: float

        :return None:

        :NOTE: If the nodes don't exist, they'll be created.
        :NOTE: It doesn't add the link if it already exists.
        """
        if not Node1 in self.Adj:            
            self.AddNode(Node1)
        if not Node2 in self.Adj:
            self.AddNode(Node2)
        if not Node2 in self.Adj[Node1]:
            self.Adj[Node1][Node2] = Weight
        return None
    
    def IsLinked(self, Node1 : any, Node2 : any) -> bool:
        """
        Verify if 2 nodes are linked. \n

        :param Node1: The starting node
        :type Node1: any
        :param Node2: The ending node
        :type Node2: any

        :return: Whether or not they are linked
        :rtype: bool
        """
        return Node2 in self.Adj[Node1]
    
    def GetNodes(self) -> list:
        """
        Get all the nodes of the graph.
        
        :return: A list containing all the nodes of the graph
        :rtype: list
        """
        Nodes : list = []
        for Node in self.Adj:
            Nodes.append(Node)
            for Neighbor in self.GetNeighbors(Node):
                if Neighbor not in Nodes:
                    Nodes.append(Neighbor)
        
        return Nodes
    
    def GetNeighbors(self, Node : any) -> list:
        """
        Return the neighbors of a node.

        :param Node: The node to get neighbors from
        :type Node: any
        :return: The list of neighbors
        :rtype: list
        """
        return self.Adj[Node]