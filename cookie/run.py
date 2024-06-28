# 运行不成功

from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'password':
            response=make_response('Logged in successfully!', 200)
            response.set_cookie('username', username)
            return response

    return render_template('login.html')

@app.route('/')
def index():
    if request.cookies.get('username'):
        return '登陆成功'
    else:
        return '请先登陆'
    
@app.route('/logout')
def logout():
    response = make_response('Logged out successfully!', 200)
    response.set_cookie('username', '', expires=0)
    response.delete_cookie('username')
    return response

if __name__ == '__main__':
    app.run(debug=True)