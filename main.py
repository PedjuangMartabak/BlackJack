from os import system, name
import os

DATA_FILE = "data.txt"

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

def addMeeting():
    with open("data.txt", "a") as file:
        nama = input("Masukkan nama: ")
        instansi = input("Masukkan instansi: ")
        waktu = input("Masukkan waktu (YYYY-MM-DD HH:MM:SS): ")
        tempat = input("Masukkan tempat: ")
        tujuan = input("Masukkan tujuan: ")
        status = input("Masukkan status: ")
        file.write(f"{nama}, {instansi}, {waktu}, {tempat}, {tujuan}, {status}\n")
        print("Jadwal meeting berhasil ditambahkan.")

def editMeeting():
    """Mengedit jadwal meeting berdasarkan nama."""
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        print("Tidak ada jadwal meeting untuk diedit.")
        return

    nama_edit = input("Masukkan nama yang ingin diedit: ").strip().lower()
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    found = False
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for line in lines:
            data = line.strip().split(", ")
            if len(data) == 6 and data[0] == nama_edit:
                found = True
                print("Masukkan data baru (kosongkan untuk tidak mengubah):")
                new_instansi = input(f"Instansi ({data[1]}): ") or data[1]
                new_waktu = input(f"Waktu ({data[2]}): ") or data[2]
                new_tempat = input(f"Tempat ({data[3]}): ") or data[3]
                new_tujuan = input(f"Tujuan ({data[4]}): ") or data[4]
                new_status = input(f"Status ({data[5]}): ") or data[5]
                file.write(f"{nama_edit} | {new_instansi} | {new_waktu} | {new_tempat} | {new_tujuan} | {new_status}\n")
            else:
                file.write(line)
    
    if found:
        print(f" Jadwal meeting untuk '{nama_edit}' berhasil diedit.")
    else:
        print(f" Tidak ditemukan jadwal dengan nama '{nama_edit}'.")

def main():
    while True :
        displayMenu()
        choice = input("Pilih menu: ")
        if choice == '1':
            while True:
                addMeeting()
                sub_choice = input("Apakah Anda ingin menambahkan meeting lagi? (y/n): ")
                if sub_choice.lower() == 'n':
                    break
        elif choice == '2':
            while True:
                editMeeting()
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
    
