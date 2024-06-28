from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
import uuid

# Initialize Flask App
app = Flask(__name__)

# Configure upload folder (example)
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Define allowed extensions

# Route to upload file
@app.route('/upload', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        avatar=request.files['avatar']
        if avatar and allowed_file(avatar.filename):
            filename=random_file(avatar.filename)
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def random_file(filename):
    ext=os.path.splitext(filename)[1]
    new_filename=uuid.uuid4()+ext
    return new_filename

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
    app.run(debug=True)

# douxiaobo@192 file_update % code .
# douxiaobo@192 file_update % python3 -m venv flask
# douxiaobo@192 file_update % source ./flask/bin/activate
# (flask) douxiaobo@192 file_update % pip3 install flask
# Collecting flask
#   Using cached flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)
# Collecting Werkzeug>=3.0.0 (from flask)
#   Using cached werkzeug-3.0.3-py3-none-any.whl.metadata (3.7 kB)
# Collecting Jinja2>=3.1.2 (from flask)
#   Using cached jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
# Collecting itsdangerous>=2.1.2 (from flask)
#   Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
# Collecting click>=8.1.3 (from flask)
#   Using cached click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
# Collecting blinker>=1.6.2 (from flask)
#   Using cached blinker-1.8.2-py3-none-any.whl.metadata (1.6 kB)
# Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask)
#   Using cached MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl.metadata (3.0 kB)
# Using cached flask-3.0.3-py3-none-any.whl (101 kB)
# Using cached blinker-1.8.2-py3-none-any.whl (9.5 kB)
# Using cached click-8.1.7-py3-none-any.whl (97 kB)
# Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
# Using cached jinja2-3.1.4-py3-none-any.whl (133 kB)
# Using cached werkzeug-3.0.3-py3-none-any.whl (227 kB)
# Using cached MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl (18 kB)
# Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, flask
# Successfully installed Jinja2-3.1.4 MarkupSafe-2.1.5 Werkzeug-3.0.3 blinker-1.8.2 click-8.1.7 flask-3.0.3 itsdangerous-2.2.0

# (flask) douxiaobo@192 file_update % python3 run.py
#  * Serving Flask app 'run'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 726-941-901
# 127.0.0.1 - - [15/Jun/2024 19:22:06] "GET /updated HTTP/1.1" 404 -
# 127.0.0.1 - - [15/Jun/2024 19:22:40] "GET /upload HTTP/1.1" 200 -
#  * Detected change in '/Users/douxiaobo/Documents/Practice in Coding/Python/file_update/run.py', reloading
#  * Restarting with stat
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/file_update/run.py", line 40
#     http://127.0.0.1:5000/upload
#          ^^
# SyntaxError: invalid syntax


# http://127.0.0.1:5000/upload