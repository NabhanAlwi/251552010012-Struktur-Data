class Graph:
    def __init__(self):
        self.Graph = {
            "A": ["B", "C"],
            "B": ["A"],
            "C": ["N"],
            "D": ["B"]
        }

    def remove_vertex(self, vertex):
        if vertex in self.Graph:
            self.Graph.pop(vertex)
            for v in self.Graph:
                if vertex in self.Graph[v]:
                    self.Graph[v].remove(vertex)
                    
    def print_Graph(self):
        print(self.Graph)
        
g = Graph() 
g.remove_vertex("B")
g.print_Graph()
 