class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(node):
    while node:
        next_id = id(node.next) if node.next else None
        print(f"[{node.data}| {next_id}]")
        node = node.next
    print("null")

a = Node("jrull")
b = Node ("mangga")
c = Node ("pisang")

b.next = a
a.next = c

print_linked_list(b)
    