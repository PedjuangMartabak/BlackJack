

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
        if choice == '1':
            while True:
                print("orang gila")
                #masukkan cuy tambahkan nama,instansi,waktu,tempat,tentang
                sub_choice = input("Apakah Anda ingin menambahkan meeting lagi? (y/n): ")
                if sub_choice.lower() == 'n':
                    break
        elif choice == '2':
            while True:
                #masukkan cuy ubah tanggal meeting
                sub_choice = input("Apakah Anda ingin mengubah Jadwal meeting lagi? (y/n): ")
                if sub_choice.lower() == 'n':
                    break
        elif choice == '3':
            while True:
                #hapus jadwal meeting
                sub_choice = input("Apakah Anda ingin menghapus meeting lagi? (y/n): ")
                if sub_choice.lower() == 'n':
                    break
        elif choice == '4':
            while True:
                #tampilkan semua jadwal meeting
                callData()
                sub_choice = input("Apakah Anda ingin kembali ke menu? (y/n): ")
                if sub_choice.lower() == 'n':
                    break
        elif choice == '5':
            while True:
                print("EXIT")
                exit()
        else:
            print("invalid syntax")

def callData(): # show data

    nama = input("Masukkan nama yang ingin dicari: ").strip().lower()

    data_ditemukan = False

    with open("data.txt", "r") as file:
        print(f"{'Nama':<10} {'Instansi':<10} {'Waktu':<10} {'Tempat':<10} {'Tujuan':<10} {'Status':<10}")
        print("=" * 61)  # Garis pemisah

        for line in file:
            data = line.strip().split(", ")
            if data[0].lower() == nama:
                print(f"{data[0]:<10} {data[1]:<10} {data[2]:<10} {data[3]:<10} {data[4]:<10} {data[5]:<10}")
                data_ditemukan = True     

if __name__ == '__main__':
    main()
