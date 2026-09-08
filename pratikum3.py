#Sistem Peminjaman Buku Perpustakaan Fakultas Teknik

daftar_buku = (
    "Dasar-Dasar Robotika",
    "Pemrograman Phython",
    "Administrasi Jaringan",
    "Rekayasa Perangkat Lunak",
    "Pemrograman Web",
)

# List untuk menyimpan buku yang dipinjam
peminjam = []

# Menampilkan daftar buku
print("=== Daftar Buku Perpustakaan FT ===")

for i, buku in enumerate(daftar_buku, start=1):
    print(f"{i}. {buku}")

# Perulangan Peminjaman
while True:
    print("\n=== PEMINJAMAN BUKU ===")
    print("1. Pinjam Buku")
    print("2. Hapus Peminjaman")
    print("3. Selesai")

    pilihan = input("Pilih menu (1/2/3): ")

    # Meminjam Buku
    if pilihan == "1":
        nomor = int(input("Masukan nomor buku yang ingin dipinjam: "))

        if 1 <= nomor <= len(daftar_buku):
            buku_dipilih = daftar_buku[nomor - 1]

            # Validasi apakah buku sudah dipinjam
            if buku_dipilih not in peminjam:
                peminjam.append(buku_dipilih)
                print("Buku berhasil dipinjam.")
            else:
                print("Buku sudah dipinjam.")
        else:
            print("Nomor buku tidak tersedia.")

    # Menghapus peminjaman
    elif pilihan == "2":
        if len(peminjam) == 0:
            print("Belum ada buku yang dipinjam")
        else:
            print("\n=== DAFTAR BUKU YANG DIPINJAM ===")

            for i, buku in enumerate(peminjam, start=1):
                print(f"{i}. {buku}")

            nomor_hapus = int(input("Masukan nomor buku yang ingin dihapus: "))

            if 1 <= nomor_hapus <= len(peminjam):
                buku_dihapus = peminjam.pop(nomor_hapus - 1)
                print(f"{buku_dihapus} berhasil dihapus dari peminjaman.")
            else:
                print("Nomor tidak tersedia.")

    # Selesai
    elif pilihan == "3":
        break

    else:
        print("Pilihan tidak valid.")

# Menampilkan seluruh buku yang dipinjam
print("\n=== SELURUH BUKU YANG DIPINJAM ===")

if len(peminjam) == 0:
    print("Tidak ada buku yang dipinjam.")
else:
    for i, buku in enumerate(peminjam, start=1):
        print(f"{i}. {buku}")

print("\nProgram selesai.")

                         



