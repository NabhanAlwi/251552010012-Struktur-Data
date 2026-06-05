class node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        
def insert_at_beginning(head, data):
    new_node = node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data):
    new_node = node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_after_node(prev_node,data):
    if not prev_node:
        print("node sebelumnya tidak boleh none")
        return
    new_node = node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    
head = node("Bayu")
head = insert_at_end(head, "Adel")
insert_after_node(head, "Cina")

def print_linked_list(head):
    while head:
        print(f"[{head.data}] ->", end="")
        head = head.next
    print("NULL")
    
current = head
while current and current.data != "Bayu":
    current = current.next
insert_after_node(current, "X")

print_linked_list(head)