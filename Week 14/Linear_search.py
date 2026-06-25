def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        return -1
    
data = [7, 3, 9, 5, 2]
print("Array saat ini: ", data)

cari = int(input("Masukan angka yang ingin dicari: "))

hasil = linear_search(data, cari)

if hasil != -1:
    print("Angka ditemukan pada indeks: ", hasil)
else:
    print("Angka tidak ditemukan dalam array.")