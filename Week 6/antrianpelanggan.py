from collections import deque

queue = deque()
queue.append('LUTFI')
queue.append('FAJRUL')
queue.append('HAFIDZ')
queue.append('SUDESS')
deque(('LUTFI', 'FAJRUL', 'HAFIDZ', 'SUDESS'))

print('antrian awal:', list(queue))
print('yang pertama dilayani: ', queue[0])
print('---mulai melayani---')

nomor = 1
while queue:
    pelanggan = queue.popleft()
    print(f'[{nomor}] melayani: {pelanggan}')
    if queue: 
        print(f' antrian: {list(queue)}')
    nomor += 1
    
print('semua pelanggan sudah dilayani!')