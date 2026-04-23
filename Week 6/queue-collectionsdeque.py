from collections import deque

queue = deque()

queue.append('A')
queue.append('B')
queue.append('C')
print('Queue: ', queue)

front = queue[0]
print('Front: ', front)

keluar = queue.popleft ()
print('dequeue: ', keluar)
print('queue: ', queue)

print( 'kosong? ', len(queue) ==0)
print('ukuran: ', len(queue))