class Node:
    def __init__ (self, value):
        self.value = value
        self.childern = []
        
    def add_child(self, child_node):
        self.childern.append(child_node)
        
    def print_tree(self, level=0):
        print(" " * level + f"- {self.value}")
        for child in self.childern:
            child.print_tree(level + 1)
            
    def get_degree(self):
        return len(self.childern)
    
    def get_height(self):
        if not self.childern:
            return 1
        return 1 + max(child.get_height() for child in self.childern)
    
root = Node("A")
node_b = Node("B") 
node_c = Node("C") 
node_d = Node("D") 
node_e = Node("E") 
node_f = Node("F") 
node_g = Node("G") 

root.add_child(node_b)
root.add_child(node_c)

node_b.add_child(node_d)
node_b.add_child(node_e)

node_c.add_child(node_f)
node_f.add_child(node_g)

print("tree struktur;")
root.print_tree()

print(f"\nderajat node A: {root.get_degree()}")
print(f"derajat node B: {node_b.get_degree()}")
print(f"derajat node F: {node_c.get_degree()}")
print(f"derajat node G: {node_g.get_degree()}")

print(f"\nTinggi root A: {root.get_height()}")      
