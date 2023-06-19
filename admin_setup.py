from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256

# Koneksi ke MongoDB Atlas
client = MongoClient('mongodb+srv://test:sparta@cluster0.arnmzf6.mongodb.net/?retryWrites=true&w=majority')
db = client['Final_project']  # Ganti dengan nama database Anda
users_collection = db['admin']

def create_admin():
    name = input("Masukkan nama admin: ")
    email = input("Masukkan email admin: ")
    password = input("Masukkan password admin: ")

    # Hash kata sandi menggunakan passlib
    hashed_password = pbkdf2_sha256.hash(password)

    # Simpan data admin ke database
    admin = {
        'name': name,
        'email': email,
        'password': hashed_password,
        'is_admin': True
    }
    users_collection.insert_one(admin)
    print("Akun admin berhasil ditambahkan.")

if __name__ == '__main__':
    create_admin()
