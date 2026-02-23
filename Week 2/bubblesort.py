angka = [5,2,9,1,5]

for i in range (len(angka)):
    for j in range(len(angka)-1):
        if angka[j] > angka[j+1]:
            [angka[j], angka[j+1]] = [angka[j+1], angka[j]]
            
print("hasil sorting", angka)
