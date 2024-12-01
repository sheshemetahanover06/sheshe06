# Code Program Pengelolaan Daftar Nilai Mahasiswa TI.24.A.3

data_mahasiswa = []

def tambah():
    print("-" * 42)
    nama = input("1. Masukkan nama mahasiswa: ")
    nilai = float(input("2. Masukkan nilai mahasiswa: "))
    print("-" * 42)
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print("=" * 42)
    print("|    --- Data berhasil ditambahkan! ---  |")
    print("=" * 42)

def tampilkan():
    if not data_mahasiswa:
        print()
        print("=" * 34)
        print("--- Belum ada data mahasiswa ---")
        print("=" * 34)
    else:
        print()
        print("--- Daftar Nilai Mahasiswa A.3 ---")
        print("=" * 34)
        print("| NO |       NAMA       | NILAI |")
        print("-" * 33)
        for i, mahasiswa in enumerate(data_mahasiswa, 1):
            print(f"|{i:3}.| {mahasiswa['nama']:16} | {mahasiswa['nilai']:6}|")
        print("=" * 34)

def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [m for m in data_mahasiswa if m['nama'] != nama]
    print("=" * 65)
    print(f"--- Data mahasiswa dengan nama '{nama}' telah dihapus! ---")
    print("=" * 65)

def ubah(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = float(input(f"2. Masukkan nilai baru untuk {nama}: "))
            print("-" * 55)
            print("=" * 55)
            print("|            --- Data berhasil diubah! ---            |")
            print("=" * 55)
            return
    print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")

def menu():
    while True:
        print()
        print("=" * 20)
        print("|   --- MENU ---   |")
        print("=" * 20)
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        print()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            tampilkan()
        elif pilihan == "3":
            print()
            print("-" * 65)
            nama = input("1. Masukkan nama mahasiswa yang ingin dihapus: ")
            print("-" * 65)
            hapus(nama)
        elif pilihan == "4":
            print()
            print("-" * 55)
            nama = input("1. Masukkan nama mahasiswa yang ingin diubah: ")
            ubah(nama)
        elif pilihan == "5":
            print()
            print("=" * 42)
            print("| --- Program selesai. Terima kasih! --- |")
            print("=" * 42)
            print()
            break
        else:
            print()
            print("=" * 51)
            print("| --- Pilihan tidak valid. Silakan coba lagi! --- |")
            print("=" * 51)

menu()