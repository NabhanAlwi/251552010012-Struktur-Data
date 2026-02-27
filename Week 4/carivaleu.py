nama = {"lutfi": "08976792773", "jrul": "0892653621", "hafidz": "0892653621"}
print("no kontak: ", list(nama.values()))

cari_nama = input("masukan nama yang ingin dicari: ")
if cari_nama in nama:
    print("nomor kontak:", nama[cari_nama])
else:
    print("nama tidak ditemukan")
