print("======Kasir Indah ===========")
pembeli = input(" Nama Pembeli :")
print("Nama Pembeli : ", pembeli)

print("\n =======MENU MAKANAN==========")
print("1. Menu Hemat")
print("2. Makanan")
print("3. Minuman")
print("4. Snack")
list_menu = int(input("Masukkan Pilihan : "))

# Menampilkan Menu Hemat
def menuhemat():
    global totalmakanan, porsi, makan
    print("")
    print(" No | Menu Hemat                    | Harga")
    print("--------------------------------------------")
    print(" 1  | Nasi Goreng + Ice Tea         | 18000")
    print(" 2  | Ayam Geprek + Nasi + Aqua     | 15000")
    print(" 3  | Mi Aceh + Lemon Tea           | 16000")
    print(" 4  | Indomie Kuah + Aqua           | 13500")
    print(" 5  | Kentang Goreng + Ayam Geprek  | 17000")
    print("---------------------------------------------")
    nomor = int(input("Masukkan Pilihan : "))
    porsi = int(input("Mau Berapa Porsi ?: "))

    if nomor == 1:
        totalmakanan = porsi * 18000
        makan = ("Nasi Goreng + Ice Tea")
    elif nomor == 2:
        totalmakanan = porsi * 15000
        makan = ("Ayam Geprek + Nasi + Aqu")
    elif nomor == 3:
        totalmakanan = porsi * 16000
        makan = ("Mi Aceh + Lemon Tea  ")
    elif nomor == 4:
        totalmakanan = porsi * 13500
        makan = ("Indomie Kuah + Aqua")
    elif nomor == 5:
        totalmakanan = porsi * 17000
        makan = (" Indomie Kuah + Aqua Kentang Goreng + Ayam Geprek ")
    else:
        print("Pilihan tidak ada, silahkan masukkan lagi!!")
        menuhemat()

def menumakanan():
    global totalmkn, porsi, mkn
    print("")
    print(" No | Menu Makanan         | Harga")
    print("--------------------------------------------")
    print(" 1  | Nasi Goreng          | 14000")
    print(" 2  | Ayam Geprek          | 13000")
    print(" 3  | Mi Aceh              | 14000")
    print(" 4  | Indomie Kuah         | 11500")
    print(" 5  | Kentang Goreng       | 10000")
    print("---------------------------------------------")
    nomor = int(input("Masukkan Pilihan: "))
    porsi = int(input("Berapa Porsi ?: "))

    if nomor == 1:
        totalmkn = porsi * 14000
        mkn = "Nasi Goreng"
    elif nomor == 2:
        totalmkn = porsi * 13000
        mkn = "Ayam Geprek"
    elif nomor == 3:
        totalmkn = porsi * 11000
        mkn = "Mie Aceh"
    elif nomor == 4:
        totalmkn = porsi * 11000
        mkn = "Indomie Kuah"
    elif nomor == 5:
        totalmkn = porsi * 11000
        mkn = "Kentang Goreng"
    else:
        print("Pilihan tidak ada, silahkan masukkan lagi!!")
        menumakanan()

def menuminuman():
    global totalmnm, porsi, mnm
    print("")
    print(" No | Menu Mainuman        | Harga")
    print("--------------------------------------------")
    print(" 1  | Teh Manis Dingin     | 5000")
    print(" 2  | Lemon Tea Dingin     | 8000")
    print(" 3  | Es Kosong            | 3000")
    print(" 4  | Kopi Panas           | 7000")
    print(" 5  | Kopi Dingin          | 10000")
    print("---------------------------------------------")
    nomor = int(input("Masukkan Pilihan: "))
    porsi = int(input("Berapa Porsi ?: "))

    if nomor == 1:
        totalmnm = porsi * 5000
        mnm = "Teh Manis Dingin"
    elif nomor == 2:
        totalmnm = porsi * 8000
        mnm = "Lemon Tea Dingin"
    elif nomor == 3:
        totalmnm = porsi * 3000
        mnm = "Es Kosong"
    elif nomor == 4:
        totalmnm = porsi * 7000
        mnm = "Kopi Panas"
    elif nomor == 5:
        totalmnm = porsi * 10000
        mnm = "Kopi Dingin"
    else:
        print("Pilihan tidak ada, silahkan masukkan lagi!!")
        menuminuman()

# Menentukan Pilihan
if list_menu == 1:
    menuhemat()
    mnm = 0
    mkn = 0
    totalsemua = totalmakanan
elif list_menu == 2:
    menumakanan()
    mnm = 0
    makan = 0
    totalsemua = totalmkn
elif list_menu == 3:
    menuminuman()
    mkn = 0
    makan = 0
    totalsemua = totalmnm
else:
    print("Pilihan menu tidak valid!")
    exit()

print("\nTotal harus Dibayar: Rp", totalsemua)
uang = int(input("Uang Tunai Pembeli: Rp "))
kembalian = uang - totalsemua
print("Kembalian: Rp", kembalian)

print("\n==========================================")
print("============ STRUK PEMBELIAN =============")
print("==========================================")
print("Nama\t\t:", pembeli)
if 'totalmakanan' in globals() and totalmakanan > 0:
    print("Beli\t\t:", makan, "( Rp", totalmakanan, ")")
if 'totalmkn' in globals() and totalmkn > 0:
    print("Beli\t\t:", mkn, "( Rp", totalmkn, ")")
if 'totalmnm' in globals() and totalmnm > 0:
    print("Beli\t\t:", mnm, "( Rp", totalmnm, ")")

print("Tagihan\t\t: Rp", totalsemua)
print("Dibayar\t\t: Rp", uang)
print("Kembalian\t: Rp", kembalian)
print("==========================================")
print("       Terimakasih Sudah Berkunjung \n    ")
print("            Selamat Menikmati             ")
print("==========================================")
