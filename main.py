def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def displayMenu():
    print("\n********Menu**********")
    print("1. Tambah Jadwal Meeting")
    print("2. Ubah Jadwal Meeting")
    print("3. Hapus Jadwal Meeting")
    print("4. Tampilkan Semua Jadwal Meeting")
    print("5. Keluar")

    