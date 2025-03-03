import sys
total = []
nama_barang = []  # Menyimpan nama barang yang dibeli
jumlah_barang = []  # Menyimpan jumlah barang yang dibeli

print("--------------------------")
print("KASIR AA")
print("-------------------------------")

def daftar_barang():
    print(" No | Nama Barang  | Harga")
    print("-------------------------------")
    print(" 1  | Downy        | 15000")
    print(" 2  | Baygon       | 24000")
    print(" 3  | Rinso        | 23000")
    print(" 4  | Kecap Bangau | 10000")
    print(" 5  | Beras        | 56000")
    print(" 6  | Popok Sweety | 21000")
    print(" 7  | Bimoli       | 24500")
    print(" 8  | Saos ABC     | 13000")
    print(" 9  | Gula         | 13000")
    print(" 10 | Susu Bayi    | 38000")
    print("-------------------------------")
    kode = int(input("Masukkan angka barang  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 15000 * jumlah1
        total.append(total1)
        nama_barang.append("Downy")
        jumlah_barang.append(jumlah1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 24000 * jumlah2
        total.append(total2)
        nama_barang.append("Baygon")
        jumlah_barang.append(jumlah2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 23000 * jumlah3
        total.append(total3)
        nama_barang.append("Rinso")
        jumlah_barang.append(jumlah3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 10000 * jumlah4
        total.append(total4)
        nama_barang.append("Kecap Bangau")
        jumlah_barang.append(jumlah4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Masukkan jumlah barang : "))
        total5 = 56000 * jumlah5
        total.append(total5)
        nama_barang.append("Beras")
        jumlah_barang.append(jumlah5)
        tanya()
    elif kode == 6:
        jumlah6 = int(input("Masukkan jumlah barang : "))
        total6 = 21000 * jumlah6
        total.append(total6)
        nama_barang.append("Popok Sweety")
        jumlah_barang.append(jumlah6)
        tanya()
    elif kode == 7:
        jumlah7 = int(input("Masukkan jumlah barang : "))
        total7 = 24500 * jumlah7
        total.append(total7)
        nama_barang.append("Bimoli")
        jumlah_barang.append(jumlah7)
        tanya()
    elif kode == 8:
        jumlah8 = int(input("Masukkan jumlah barang : "))
        total8 = 13000 * jumlah8
        total.append(total8)
        nama_barang.append("Saos ABC")
        jumlah_barang.append(jumlah8)
        tanya()
    elif kode == 9:
        jumlah9 = int(input("Masukkan jumlah barang : "))
        total9 = 13000 * jumlah9
        total.append(total9)
        nama_barang.append("Gula")
        jumlah_barang.append(jumlah9)
        tanya()
    elif kode == 10:
        jumlah10 = int(input("Masukkan jumlah barang : "))
        total10 = 38000 * jumlah10
        total.append(total10)
        nama_barang.append("Susu Bayi")
        jumlah_barang.append(jumlah10)
        tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    subtotal = sum(total)
    print("\n-------------------------------------------")
    print("             STRUK BELANJA             ")
    print("----------------------------------------------")
    print("No | Nama Barang  | Jumlah  | Harga  | Total")
    print("-----------------------------------------------")
    for i in range(len(nama_barang)):
        print(f"{i+1}  | {nama_barang[i]:<12} | {jumlah_barang[i]:<7} | {total[i]//jumlah_barang[i]:<3}  | {total[i]}")
    print("-------------------------------")
    print(f"SubTotal         : {subtotal}")
    print("Potongan Harga   : 0")
    totalakhir = subtotal  # Tidak ada diskon, jadi total akhir sama dengan subtotal
    print(f"Total            : {totalakhir}")
    print("-------------------------------")
    bayar = int(input("Bayar            :  "))
    kembalian = bayar - totalakhir
    print(f"Kembalian        : {kembalian}")
    print("-------------------------------")
    print("          Terima Kasih         ")
    print("-------------------------------")

daftar_barang()
