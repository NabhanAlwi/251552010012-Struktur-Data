class node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = node('apelll')
b = node('mangga')
c = node('pisang')

b.next = a
a.next = c

current = b
while current:
    print(f'node @{id(current)} | data: {current.data} | next: {id(current.next)} if current.next else None')
    current = current.next
    