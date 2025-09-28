# Nama : Jihan Shafira Rahmah
# NIM : 2509116073
# Kelas : B'25

from prettytable import PrettyTable

catatan = []

akun = {"admin": "admin000", "mahasiswa": "mahasiswa000"}

# fungsi untuk menampilkan kegiatan menggunakan PrettyTable
def tampil_kegiatan():
    if not catatan:
        print("belum ada kegiatan")
    else:
        tabel = PrettyTable(["Judul", "Tanggal Kegiatan", "Lokasi"])
        for keg in catatan:
            tabel.add_row(keg)
        print(tabel)

# menu untuk mahasiswa
def menu_mahasiswa():
    while True:
        print("\nMenu Mahasiswa")
        print("1. Tambah Kegiatan")
        print("2. Hapus Kegiatan")
        print("3. Lihat Semua Kegiatan")
        print("4. Keluar")

        try:
            pilihan = input("Pilih Menu (1/2/3/4): ")
            if pilihan not in ["1", "2", "3", "4"]:
                print("Pilihan Tidak Valid")
                continue
        
            if pilihan == "1":
                judul = input("Masukkan Judul Kegiatan: ")
                tanggal = input("Masukkan Tanggal Kegiatan: ")
                lokasi = input("Masukkan Lokasi Kegiatan: ")
                catatan.append((judul, tanggal, lokasi))
                print("Kegiatan berhasil ditambahkan")

            elif pilihan == "2":
                hapus = input("Masukkan Judul Kegiatan yang Ingin Dihapus: ")
                ditemukan = False
                for keg in list(catatan):
                    if keg[0] == hapus:
                        catatan.remove(keg)
                        print("Kegiatan berhasil dihapus")
                        ditemukan = True
                        break
                if not ditemukan:
                    print("Kegiatan tidak ditemukan")

            elif pilihan == "3":
                tampil_kegiatan()

            elif pilihan == "4":
                print("Keluar dari menu mahasiswa")
                break  

        except KeyboardInterrupt:
            print("\nHarap tidak menekan tombol CTRL+C")
            break
        except Exception as e:
            print("Harap tidak menekan tombol CTRL+Z", e)
        
        
# menu untuk admin
def menu_admin():
    while True:
        print("\nMenu Admin")
        print("1. Lihat Data Kegiatan")
        print("2. Lihat Akun Pengguna")
        print("3. Keluar")

        try:
            pilihan = input("Pilih Menu (1/2/3): ")
            if pilihan not in ["1", "2", "3"]:
                print("Pilihan Tidak Valid")
                continue
        
            if pilihan == "1":
                print("\n--- Data Kegiatan ---")
                tampil_kegiatan()

            elif pilihan == "2":
                print("\nLihat Akun Pengguna")
                print("Daftar akun:", akun)

            elif pilihan == "3":
                print("Keluar dari menu admin")
                break  

        except KeyboardInterrupt:
            print("\nHarap tidak menekan tombol CTRL+C")
            break
        except Exception as e:
            print("Harap tidak menekan tombol CTRL+Z", e)
        

print("=== Sistem Catatan Kegiatan Sosial Mahasiswa ===")

while True:
    try:
        username = input("\nMasukkan Username: ").strip()
        password = input("Masukkan Password: ")

        if username in akun and akun[username] == password:
            print("Login berhasil")

            if username == "admin":
                menu_admin()
            else:
                menu_mahasiswa()
        else:
            print("Username atau password salah")

    except KeyboardInterrupt:
        print("\nHarap tidak menekan tombol CTRL+C.")
        break
    except Exception as e:
        print("Harap tidak menekan tombol CTRL+Z", e)
    
        
    