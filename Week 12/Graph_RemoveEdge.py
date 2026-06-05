class Graph:
    def __init__(self):
        self.Graph = {
            "A": ["B", "C"],
            "B": ["A"],
            "C": ["A"],
        }
        
    def remove_edge(self, u, v):
        if u in self.Graph and v in self.Graph[u]:
            self.Graph[u].remove(v)
        if v in self.Graph and u in self.Graph[v]:
            self.Graph[v].remove(u)
            
    def print_Graph(self):
        print(self.Graph)
        
g = Graph()
g.remove_edge("A", "B")
g.print_Graph()