from flask import Flask, render_template,jsonify, request, redirect, url_for, session
app = Flask(__name__)
#app.secret_key = 'your_secret_key'

# Dummy user database
users = {'username': 'password'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('\templates\login_v2.html', error='Invalid username or password')
    return render_template('\templates\login_v2.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)