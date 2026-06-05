class Node:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
        
root = Node("Agus")
root.left = Node("Budi")
root.right = Node("Cici")
root.left.right = Node("Dedi")
root.right.left = Node("Eka")

def bfs_level_order(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value, end='-- ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
print("BFS Level order: ")
bfs_level_order(root)