def balik_string(teks):
    stack = []

    for char in teks: 
        stack.append(char)

    hasil = '' 
    while stack: 
        
        hasil += stack.pop()
        
    return hasil