class Graph:
    def __init__(self):
        self.Graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.Graph:
            self.Graph[vertex] = []
    
    def print_graph(self):
        print(self.Graph)
        
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.print_graph()