print('''
===================================
            WARUNG KC
        MAKANAN DAN MINUMAN
===================================
            MENU MAKANAN
---------------------------------------
| Kode |     Nama     |     Harga     |
---------------------------------------
|  NG  | Nasi Goreng  |RP. 13.000,00  |
|  NK  | Nasi Kuning  |RP. 12.000,00  |
|  NC  | Nasi Campur  |RP. 12.000,00  |
---------------------------------------

            MENU MINUMAN
---------------------------------------
| Kode |     Nama     |     Harga     |
---------------------------------------
|  ET  | Es Teh       |RP. 6.000,00   |
|  JJ  | Jus Jeruk    |RP. 7.000,00   |
|  TP  | Teh Panas    |RP. 5.500,00   |
|  KH  | Kopi Hitam   |RP. 5.000,00   |
---------------------------------------

        ---------------------
          SELAMAT MENIKMATI
        ---------------------
''')

while True:

    print("Mau Ki Pesan Apa ?\n\nJika Makanan Tekan 1\nJika Minuman  Tekan 2\n")
    opsi = int(input("1/2 : "))
    if opsi == 1 :
        kode = input("Masukkan Kode : ")
        n = int(input("Jumlah Pesan : "))
        if kode == "NG":
            print(f"Kode           = {kode}")
            print("Nama Makanan    = Nasi Goreng")
            print("Harga           = RP.13.000,00")
            print(f"Jumlah Pesanan = {n}")
            print(f"Total Harga    = RP.{n*13000},00")
            print("-------TERIMA KASIH-------")
        elif kode == "NK":
            print(f"Kode           = {kode}")
            print("Nama Makanan    = Nasi Kuning")
            print("Harga           = RP.12.000,00")
            print(f"Jumlah Pesanan = {n}")
            print(f"Total Harga    = RP.{n*12000},00")
            print("-------TERIMA KASIH-------")
        elif kode == "NC":
            print(f"Kode           = {kode}")
            print("Nama Makanan    = Nasi Campur")
            print("Harga           = RP.12.000,00")
            print(f"Jumlah Pesanan = {n}")
            print(f"Total Harga    = RP.{n*12000},00")
            print("-------TERIMA KASIH-------")
        else:
            print("Menu Tidak Tersedia")

    elif opsi == 2:
        kode = input("Masukkan Kode : ")
        n = int(input("Jumlah Pesan : "))
        if kode == "ET":
            print(f"\nKode         = {kode}")
            print("Nama Minuman    = Es Teh")
            print("Harga           = RP.6.000,00")
            print(f"Jumlah Pesanan = {n}")
            print(f"Total Harga    = RP.{n*6000},00")
            print("-------TERIMA KASIH-------")
        elif kode == "JJ":
            print(f"\nKode         = {kode}")
            print("Nama Minuman    = Juas Jeruk")
            print("Harga           = RP. 7.000,00")
            print(f"Jumlah Pesanan = {n}")
            print(f"Total Harga    = RP.{n*7000},00")
            print("-------TERIMA KASIH-------")
        elif kode == "TP":
            print(f"\nKode         = {kode}")
            print("Nama Minuman    = Teh Panas")
            print("Harga           = RP. 5.500,00")
            print(f"Jumlah Pesanan = {n}")
            print(f"Total Harga    = RP. {n*5500},00")
            print("-------TERIMA KASIH-------")
        elif kode == "KH":
            print(f"\nKode         = {kode}")
            print("Nama Minuman    = Kopi Hitam")
            print("Harga           = RP. 5.000,00")
            print(f"Jumlah Pesanan = {n}")
            print(f"Total Harga    = RP. {n*5000},00")
            print("-------TERIMA KASIH-------")
        else:
            print("Menu Tidak Tersedia")
    else:
        print("Hanya Ada Opsi 1 Dan 2")

    lagi = input("Mau Pesan Lagi (yes/no)?")
    if lagi == "no" or "NO":
        break
print("-------PROGRAM SELESAI-------")

