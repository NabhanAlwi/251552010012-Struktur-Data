class Graph:
    def __init__(self):
        self.Graph = {}
        
    def add_edge(self, u, v):
        if u not in self.Graph:
            self.Graph[u] = [v]
            
        if v not in self.Graph:
            self.Graph[v] = [u]
        self.Graph[u].append(v)
        self.Graph[v].append(u)
        
    def print_graph(self):
        print(self.Graph)
        
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('N', 'C')
g.print_graph()