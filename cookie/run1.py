# 运行不成功
from flask import Flask, render_template, request, redirect, url_for,session

app=Flask(__name__)
app.secret_key='your_secret_key'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    if session.get('logged_in'):
        return 'Logged in'
    else:
        return 'log in again'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))
