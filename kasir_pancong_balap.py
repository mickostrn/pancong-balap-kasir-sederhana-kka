from datetime import datetime

menu = [
    {
        "nama": "Pancong Original",
        "harga": 10000,
        "kategori": "Makanan"
    },
    {
        "nama": "Pancong Coklat",
        "harga": 12000,
        "kategori": "Makanan"
    },
    {
        "nama": "Pancong Keju",
        "harga": 13000,
        "kategori": "Makanan"
    },
    {
        "nama": "Pancong Oreo",
        "harga": 14000,
        "kategori": "Makanan"
    },
    {
        "nama": "Pancong Matcha",
        "harga": 15000,
        "kategori": "Makanan"
    },

    {
        "nama": "Teh",
        "harga": 5000,
        "kategori": "Minuman"
    },
    {
        "nama": "Jeruk",
        "harga": 7000,
        "kategori": "Minuman"
    },
    {
        "nama": "Kopi Susu",
        "harga": 10000,
        "kategori": "Minuman"
    },
    {
        "nama": "Air Mineral",
        "harga": 4000,
        "kategori": "Minuman"
    },
    {
        "nama": "Matcha",
        "harga": 12000,
        "kategori": "Minuman"
    }
]

keranjang = []

def menu_utama() :
    print("=" * 7 + " Menu Pemesanan Pancong Balap " + "=" * 7)
    print("1. Lihat Menu")
    print("2. Tambah Pesanan")
    print("3. Lihat Keranjang")
    print("4. Hapus Pesanan")
    print("5. Bayar")
    print("6. Keluar")



def tampilkan_menu(data_menu):
    for i, produk in enumerate(data_menu, start=1):
        print(
            f"{i}. {produk['nama']} "
            f"- Rp{produk['harga']:,}"
        )



def lihat_menu():
    while True :
        print()
        print("=" * 5 + "Lihat Menu" + "=" * 5)
        print("1. Semua Menu")
        print("2. Makanan")
        print("3. Minuman")
        print("4. Pergi Ke Menu Utama")
    
        try:
            pilihan = int(input("Pilih: "))
        except ValueError:
            print("Input harus angka")
            continue
    
        if pilihan == 1 :
            urutan = 1
            print("=" * 5 + " Menu Hidangan" + "=" * 5)
    
            for product in menu :

                print(f"{urutan}. {product["nama"]} - Rp{product["harga"]}")
                urutan += 1
            print()
    
        elif pilihan == 2 :
            urutan = 1
            print("=" * 5 + " Menu Makanan" + "=" * 5)
    
            for product in menu :

                if product["kategori"] == "Makanan":
                    print(f"{urutan}. {product["nama"]} - Rp{product["harga"]}")
                    urutan += 1
            print()
    
        elif pilihan == 3 :
            urutan = 1
            print("=" * 5 + " Menu Minuman" + "=" * 5)
    
            for product in menu :

                if product["kategori"] == "Minuman":
                    print(f"{urutan}. {product["nama"]} - Rp{product["harga"]}")
                    urutan += 1
            print()
    
        elif pilihan == 4 :
            break
    
        else :
            print("Pilihan Tidak Valid")
    print()



def tambah_pesanan():
    while True :
        print()
        print("=" * 5 + " Tambah Pesanan " + "=" * 5)

        tampilkan_menu(menu)
        print(f"{len(menu)+1}. Kembali")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka")
            continue

        if pilihan == len(menu) + 1 :
            print()

        if pilihan == len(menu) + 1:
            break

        if not 1 <= pilihan <= len(menu):
            print("Menu tidak tersedia")
            continue

        produk = menu[pilihan - 1]

        try:
            jumlah = int(input("Jumlah: "))
        except ValueError:
            print("Input harus angka")
            continue

        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            continue

        variasi = "-"

        if produk["kategori"] == "Minuman":
            print()
            print("Pilih Variasi:")
            print("1. Dingin")
            print("2. Normal")
            print("3. Hangat")

            try:
                pilih_variasi = int(input("Pilih: "))
            except ValueError:
                print("Input tidak valid")
                continue

            if pilih_variasi == 1:
                variasi = "Dingin"
            elif pilih_variasi == 2:
                variasi = "Normal"
            elif pilih_variasi == 3:
                variasi = "Hangat"
            else:
                print("Variasi tidak valid")
                continue

        ditemukan = False

        for item in keranjang:
            if (
                item["nama"] == produk["nama"]
                and item["variasi"] == variasi
            ):
                item["jumlah"] += jumlah
                ditemukan = True
                break

        if not ditemukan:
            keranjang.append({
                "nama": produk["nama"],
                "kategori": produk["kategori"],
                "variasi": variasi,
                "harga": produk["harga"],
                "jumlah": jumlah
            })

        print("Pesanan berhasil ditambahkan")
        print()




def lihat_keranjang():
    print()
    print("=" * 5 + " Isi Keranjang" + "=" * 5)
    urutan = 1

    if not keranjang:
        print("Keranjang kosong")
        print()
        return

    for i, item in enumerate(keranjang, start=1):
        subtotal = item["harga"] * item["jumlah"]

        print(
            f"{i}. {item['nama']} "
            f"({item['variasi']}) "
            f"x{item['jumlah']} "
            f"Rp{item['harga']:,} "
            f"= Rp{subtotal:,}"
            )

    print()
    print(f"Total : Rp{hitung_total():,}")




def hapus_pesanan():
    if not keranjang:
        print("Keranjang kosong")
        return

    lihat_keranjang()

    try:
        pilihan = int(input("Nomor yang ingin dihapus: "))
    except ValueError:
        print("Input harus angka")
        print()
        return

    if not 1 <= pilihan <= len(keranjang):
        print("Nomor tidak valid")
        print()
        return

    item = keranjang[pilihan - 1]

    try:
        jumlah = int(input("Jumlah yang dihapus: "))
    except ValueError:
        print("Input harus angka")
        print()
        return

    if jumlah <= 0:
        print("Jumlah tidak valid")
        print()
        return

    if jumlah < item["jumlah"]:
        item["jumlah"] -= jumlah
        print("Pesanan berhasil diperbarui")
        print()

    elif jumlah == item["jumlah"]:
        keranjang.pop(pilihan - 1)
        print("Pesanan berhasil dihapus")
        print()

    else:
        print("Jumlah melebihi pesanan")
        print()




def hitung_total():
    total = 0

    for produk in keranjang:
        total += produk["harga"] * produk["jumlah"]

    return total



def hitung_diskon(total):
    if total >= 50000:
        diskon = total * 0.05

    return 0



def bayar():
    while True :
        if not keranjang:
            print("Keranjang Anda kosong")
            print()
            return

        total = hitung_total()

        diskon = hitung_diskon(total)

        total_bayar = total - diskon

        print()
        print("=" * 5 + " Pembayaran " + "=" * 5)

        urutan = 1

        for product in keranjang:
            subtotal = product["harga"] * product["jumlah"]

            print(
                f"{urutan}. {product['nama']} x{product['jumlah']} = Rp{subtotal}"
            )


        print()
        print(f"Total Harga : Rp{total}")
        print(f"Diskon      : Rp{diskon}")
        print(f"Total Bayar : Rp{total_bayar}")

        try :
            uang = int(input("Masukkan Uang : "))
        except ValueError:
            print("Input harus angka")
            print()
            break

        if uang >= total_bayar:
            kembalian = uang - total_bayar

            cetak_struk(
                total,
                diskon,
                total_bayar,
                uang,
                kembalian
            )

            keranjang.clear()

        else:
            print("Uang tidak cukup")
            print()



def cetak_struk(total, diskon, total_akhir, uang, kembalian):
    print()
    print("=" * 10)
    print("Pancong Balap")
    print("=" * 10)

    waktu = datetime.now()

    print(
        waktu.strftime("%d-%m-%Y %H:%M:%S")
    )

    print("-" * 35)

    for item in keranjang:
        subtotal = item["harga"] * item["jumlah"]

        print(item["nama"])

        if item["variasi"] != "-":
            print(f"Variasi : {item['variasi']}")

        print(
            f"{item['jumlah']} x "
            f"Rp{item['harga']:,} "
            f"= Rp{subtotal:,}"
        )

        print()

    print("-" * 35)

    print(f"Total       : Rp{total:,}")
    print(f"Diskon      : Rp{diskon:,}")
    print(f"Total Akhir : Rp{total_akhir:,}")
    print(f"Bayar       : Rp{uang:,}")
    print(f"Kembalian   : Rp{kembalian:,}")

    print("-" * 35)
    print("Terima Kasih")
    print()


while True :
    menu_utama()

    try:
        pilihan = int(input("Pilih: "))
    except ValueError:
        print("Input harus angka")
        print()
        continue

    if pilihan == 1:
        lihat_menu()
    elif pilihan == 2:
        tambah_pesanan()
    elif pilihan == 3:
        lihat_keranjang()
    elif pilihan == 4:
        hapus_pesanan()
    elif pilihan == 5:
        bayar()
    elif pilihan == 6:
        print("Terima Kasih Telah Menggunakan Kasir Pancong Balap")
        break
    else:
        print("Pilihan Tidak Valid")

