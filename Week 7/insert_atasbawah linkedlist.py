class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def insert_at_beginning(head,data):
    new_node = node(data)
    new_node.next = head
    return new_node

head = node("apel")
head = node("tambah")
head = insert_at_beginning(head, "A")

def print_linked_list(head):
    while head:
        print(f"[{head.data}] -> ", end="")
        head = head.next
    print("NULL")
    
print_linked_list(head)

print("<<<<<<>>>>>>")

def __init__(self, data):
        self.data = data
        self.next = None
        
def insert_at_end(head, data):
    new_node = node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

head = node("A")
head = insert_at_end(head, "B")

def print_linked_list(head):
    while head:
        print(f"[{head.data}] ->", end="")
        head = head.next
    print("NULL")
        
print_linked_list(head)
