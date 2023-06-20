from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256

client = MongoClient('mongodb+srv://test:sparta@cluster0.arnmzf6.mongodb.net/?retryWrites=true&w=majority')
db = client['Final_project']
users_collection = db['admin']

def create_admin():
    name = input("Masukkan nama admin: ")
    email = input("Masukkan email admin: ")
    password = input("Masukkan password admin: ")

    hashed_password = pbkdf2_sha256.hash(password)

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
