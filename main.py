

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

def main():
    while True :
        displayMenu()
        choice = input("Pilih menu: ")
        if choice == 1:
            while True:
                #masukkan cuy tambahkan nama,instansi,waktu,tempat,tentang
                sub_choice = input("Apakah Anda ingin menambahkan meeting lagi? (y/n): ")
                if sub_choice.lower() != 'y':
                    break
        elif choice == 2:
            while True:
                #masukkan cuy ubah tanggal meeting
                sub_choice = input("Apakah Anda ingin mengubah Jadwal meeting lagi? (y/n): ")
                if sub_choice.lower() != 'y':
                    break
        elif choice == 3:
            while True:
                #hapus jadwal meeting
                sub_choice = input("Apakah Anda ingin menghapus meeting lagi? (y/n): ")
                if sub_choice.lower() != 'y':
                    break
        elif choice == 4:
            while True:
                #tampilkan semua jadwal meeting
                sub_choice = input("Apakah Anda ingin kembali ke menu? (y/n): ")
                if sub_choice.lower() != 'y':
                    break
        elif choice == 5:
            while True:
                print("EXIT")
                break





if __name__ == '__main__':
    main()