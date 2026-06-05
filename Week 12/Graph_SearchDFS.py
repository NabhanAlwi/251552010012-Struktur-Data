class Graph:
    def __init__(self):
        self.Graph = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "N"],
        }
            
    def search(self, start, target):
        visited = set()
        def dfs(v):
            if v == target:
                return True
            visited.add(v)
            for neighbor in self.Graph.get(v, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                    
            return True
        return dfs(start)
    
g = Graph()
print("A ke B:", g.search("A", "B"))
print("A ke D:", g.search("A", "D"))
print("A ke N:", g.search("A", "N"))