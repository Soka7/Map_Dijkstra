class Graphe_D:
    '''Graphe représenté par un dictionnaire d'adjacence'''
    def __init__(self):
        self.adj = {}
    
    def affiche(self):
        for k in self.adj:
            print (k, self.adj[k])
    
    def ajouter_sommet(self, s):
        if s not in self.adj:
            self.adj[s] = {}
   
    def ajouter_arc(self, s1, s2, p):
        if not s1 in self.adj:            
            self.ajouter_sommet(s1)
        if not s2 in self.adj[s1]:
            self.adj[s1][s2] = p
        return self.adj
    
    def arc(self,s1,s2):
        return s2 in self.adj[s1]
    
    def sommets(self):
        s = []
        for k in self.adj:
            s.append(k)
            for element in self.voisins(k):
                if element not in s:
                    s.append(element)
        
        return s
    
    def voisins(self, s):
        return self.adj[s]