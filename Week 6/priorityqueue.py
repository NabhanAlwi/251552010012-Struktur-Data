import heapq

pq = []

heapq.heappush(pq, (3, 'task C - Rendah'))
heapq.heappush(pq, (1, 'task A - Urgent'))
heapq.heappush(pq, (2, 'task B - Medium'))

print('Priority Queue: ', pq)
while pq:
    prioritas, task=heapq.heappop(pq)
    print(f'[prioritas{prioritas}] proses: {task}')