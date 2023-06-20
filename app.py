from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.secret_key = "sparta"

client = MongoClient('mongodb+srv://test:sparta@cluster0.arnmzf6.mongodb.net/?retryWrites=true&w=majority')
db = client['Final_project']  
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
            return redirect('/courses')

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

@app.route('/about')
def about():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('about.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/admin')
def admin():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id})

    if user:
       return render_template('/admin.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/admin2')
def admin2():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = admin_collection.find_one({'_id': user_id}) 

    if user:
       return render_template('/admin2.html', user=user)

    return "Akses ditolak. Silakan login sebagai admin."

@app.route('/course_details')
def course_details():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = ObjectId(session['user_id'])
    user = users_collection.find_one({'_id': user_id})

    if user:
        return render_template('course_details.html', user=user)

    return "Akses ditolak. Silakan login sebagai pengguna."

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
