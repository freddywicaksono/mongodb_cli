import os
from mahasiswa import *

def main():
    while True:
        os.system('cls')
        display_all_mahasiswa()
        print("================================================================")
        print("1 - Create | 2- Update | 3 - Delete | 4 - Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            data = {
                "nim": input("NIM: "),
                "nama": input("Nama: "),
                "jk": input("Jenis Kelamin: "),
                "prodi": input("Program Studi: ")
            }
            create_mahasiswa(data)
        elif choice == "2":
            nim = input("Enter NIM to update: ")
            get_mahasiswa(nim)
            new_data = {
                "nama": input("Nama (new): "),
                "jk": input("Jenis Kelamin (new): "),
                "prodi": input("Program Studi (new): ")
            }
            update_mahasiswa(nim, new_data)
        elif choice == "3":
            nim = input("Enter NIM to delete: ")
            delete_mahasiswa(nim)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()