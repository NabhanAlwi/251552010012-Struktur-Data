class node: 
    def __init__(self, data):
        self.data= data
        self.next= None

a = node('ghos')
b = node('soal')
c = node('jambu')

c.next = b
b.next = a

current = c
while current:
    print(current.data)
    current = current.next
    