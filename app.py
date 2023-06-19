from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.secret_key = "sparta"  # Ganti dengan kunci rahasia yang kuat

# Koneksi ke MongoDB Atlas
client = MongoClient('mongodb+srv://test:sparta@cluster0.arnmzf6.mongodb.net/?retryWrites=true&w=majority')
db = client['Final_project']  # Ganti dengan nama database Anda
users_collection = db['users']
admin_collection = db['admin']  # Koleksi admin

# Route untuk halaman beranda
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk halaman login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Cari pengguna berdasarkan alamat email di koleksi admin
        admin_user = admin_collection.find_one({'email': email})
        if admin_user and pbkdf2_sha256.verify(password, admin_user['password']):
            session['user_id'] = str(admin_user['_id'])
            return redirect('/admin_dashboard')

        # Cari pengguna berdasarkan alamat email di koleksi users
        user = users_collection.find_one({'email': email})
        if user and pbkdf2_sha256.verify(password, user['password']):
            session['user_id'] = str(user['_id'])
            return redirect('/courses')

        # Jika login gagal, tampilkan pesan kesalahan
        error_message = "Email atau kata sandi salah. Silakan coba lagi."
        return render_template('login.html', error_message=error_message)

    return render_template('login.html')


# Route untuk halaman pendaftaran pengguna
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Hash kata sandi menggunakan passlib
        hashed_password = pbkdf2_sha256.hash(password)

        # Simpan pengguna baru ke koleksi users
        user = {
            'name': name,
            'email': email,
            'password': hashed_password
        }
        user_id = users_collection.insert_one(user).inserted_id

        # Login pengguna setelah pendaftaran berhasil
        session['user_id'] = str(user_id)
        return redirect('/courses')

    return render_template('signup.html')

# Route untuk halaman admin dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    # Periksa apakah pengguna memiliki akses admin
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id})  # Ubah dari users_collection ke admin_collection

    if user:
       return render_template('/admin_dashboard.html', user=user)  # Menyertakan data pengguna saat merender template

    return "Akses ditolak. Silakan login sebagai admin."

# Route untuk halaman dashboard pengguna
@app.route('/courses')
def courses():
    # Periksa apakah pengguna telah login
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('courses.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

# Route untuk halaman admin
@app.route('/admin')
def admin():
    # Periksa apakah pengguna memiliki akses admin
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id})  # Ubah dari users_collection ke admin_collection

    if user:
       return render_template('/admin.html', user=user)  # Menyertakan data pengguna saat merender template

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin2')
def admin2():
    # Periksa apakah pengguna memiliki akses admin
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id})  # Ubah dari users_collection ke admin_collection

    if user:
       return render_template('/admin2.html', user=user)  # Menyertakan data pengguna saat merender template

    return "Akses ditolak. Silakan login sebagai admin."

# Route untuk halaman user
@app.route('/user')
def user():
    # Periksa apakah pengguna telah login
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('user.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

# Route untuk logout
@app.route('/logout')
def logout():
    # Hapus ID pengguna dari sesi
    session.pop('user_id', None)
    return redirect('/')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
