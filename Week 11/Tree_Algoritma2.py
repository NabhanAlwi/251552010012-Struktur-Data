class BinaryNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
        
root = BinaryNode("M")
root.left = BinaryNode("B")
root.right = BinaryNode("C")
root.left.left = BinaryNode("D")
root.left.right = BinaryNode("E")
root.right.left = BinaryNode("G")
root.right.right = BinaryNode("F")


def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)
        
print(f"Binary Tree Preorder Traversal: ")
preorder(root)