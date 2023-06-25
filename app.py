from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.secret_key = "sparta"

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
users_collection = db['users']
admin_collection = db['admin']  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        admin_user = admin_collection.find_one({'email': email})
        if admin_user and pbkdf2_sha256.verify(password, admin_user['password']):
            session['user_id'] = str(admin_user['_id'])
            return redirect('/admin_dashboard')

        user = users_collection.find_one({'email': email})
        if user and pbkdf2_sha256.verify(password, user['password']):
            session['user_id'] = str(user['_id'])
            return redirect('/user_dashboard')

        error_message = "Email atau kata sandi salah. Silakan coba lagi."
        return render_template('login.html', error_message=error_message)

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        hashed_password = pbkdf2_sha256.hash(password)
        user = {
            'name': name,
            'email': email,
            'password': hashed_password
        }
        user_id = users_collection.insert_one(user).inserted_id

        session['user_id'] = str(user_id)
        return redirect('/courses')

    return render_template('signup.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_dashboard.html', user=user) 

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/courses')
def courses():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('courses.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/user_dashboard')
def user_dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('user_dashboard.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/about')
def about():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('about.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/admin_courses')
def admin_courses():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id})

    if user:
       return render_template('/admin_courses.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_about')
def admin_about():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_about.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course0')
def admin_course0():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course0.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course1')
def admin_course1():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course1.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course2')
def admin_course2():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course2.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course3')
def admin_course3():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course3.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course4')
def admin_course4():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course4.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course5')
def admin_course5():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course5.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course6')
def admin_course6():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course6.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course7')
def admin_course7():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course7.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course8')
def admin_course8():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course8.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin_course9')
def admin_course9():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin_course9.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/course0')
def course0():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course0.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/course1')
def course1():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course1.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/course2')
def course2():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course2.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/course3')
def course3():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course3.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/course4')
def course4():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course4.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/course5')
def course5():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course5.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/course6')
def course6():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course6.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/course7')
def course7():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course7.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/course8')
def course8():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course8.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/course9')
def course9():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course9.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return render_template ('login.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
