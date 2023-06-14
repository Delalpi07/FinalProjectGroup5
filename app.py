from flask import Flask, render_template 
app = Flask(__name__)

# untuk rute user 
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/courses')
def courses_page():
    return render_template('courses.html')

@app.route('/courses-details')
def coursesdetails_page():
    return render_template('courses-details.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/events')
def event_page():
    return render_template('events.html')

# untuk rute admin
@app.route('/admin/login')
def login_pageadmin():
    return render_template('admin/login.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
