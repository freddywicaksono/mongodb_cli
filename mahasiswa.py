from db import *

collection = db["mahasiswa"]

def create_mahasiswa(data):
    collection.insert_one(data)
    print("Mahasiswa data created successfully.")

def display_all_mahasiswa():
    mahasiswa_list = collection.find()
    document_count = collection.estimated_document_count()
    if document_count == 0:
        print("\nAll Mahasiswa data:")
        print("================================================================")
        print("      NIM      |      Nama      | Jenis Kelamin | Program Studi")
        print("================================================================")
        print("No Mahasiswa data found.")
    else:
        print("\nAll Mahasiswa data:")
        print("================================================================")
        print("      NIM      |      Nama      | Jenis Kelamin | Program Studi")
        print("================================================================")
        
        for index, mahasiswa in enumerate(mahasiswa_list, start=1):
            student_info = (
                f"{mahasiswa['nim']:14} | {mahasiswa['nama']:14} | {mahasiswa['jk']:13} | {mahasiswa['prodi']}"
            )
            print(student_info)
        
def get_mahasiswa(nim):
    mahasiswa = collection.find_one({"nim": nim})
    if mahasiswa:
        print("Mahasiswa data:")
        print(mahasiswa)
    else:
        print("Mahasiswa not found.")

def update_mahasiswa(nim, new_data):
    result = collection.update_one({"nim": nim}, {"$set": new_data})
    if result.modified_count > 0:
        print("Mahasiswa data updated successfully.")
    else:
        print("Mahasiswa not found.")

def delete_mahasiswa(nim):
    result = collection.delete_one({"nim": nim})
    if result.deleted_count > 0:
        print("Mahasiswa data deleted successfully.")
    else:
        print("Mahasiswa not found.")