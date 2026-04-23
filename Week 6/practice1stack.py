stack = []

stack.append ('apa')
stack.append ('api')
stack.append ('apu')

top = stack[-1]
popped = stack.pop()
middel = stack[len(stack) // 2]

print ('awal : ', stack)
print ("top :", top)
print ("popped :", popped)
print ("middel :", middel)
print ('kosong?', len(stack)==0)
print('ukuran :', len(stack))