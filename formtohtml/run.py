from flask import Flask, url_for, redirect, render_template
from models import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        username=form.name.data
        password=form.password.data
        if username=='admin' and password=='password':
            return redirect(url_for('success'))
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return 'Login Success!'

if __name__ == '__main__':
    app.run(debug=True)


# douxiaobo@192 formtohtml % python3 -m venv flask
# douxiaobo@192 formtohtml % source flask/bin/activate
# (flask) douxiaobo@192 formtohtml % pip3 install flask
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
# (flask) douxiaobo@192 formtohtml % pip3 install flask-wtf
# Collecting flask-wtf
#   Downloading flask_wtf-1.2.1-py3-none-any.whl.metadata (3.4 kB)
# Requirement already satisfied: flask in ./flask/lib/python3.12/site-packages (from flask-wtf) (3.0.3)
# Requirement already satisfied: itsdangerous in ./flask/lib/python3.12/site-packages (from flask-wtf) (2.2.0)
# Collecting wtforms (from flask-wtf)
#   Downloading wtforms-3.1.2-py3-none-any.whl.metadata (5.3 kB)
# Requirement already satisfied: Werkzeug>=3.0.0 in ./flask/lib/python3.12/site-packages (from flask->flask-wtf) (3.0.3)
# Requirement already satisfied: Jinja2>=3.1.2 in ./flask/lib/python3.12/site-packages (from flask->flask-wtf) (3.1.4)
# Requirement already satisfied: click>=8.1.3 in ./flask/lib/python3.12/site-packages (from flask->flask-wtf) (8.1.7)
# Requirement already satisfied: blinker>=1.6.2 in ./flask/lib/python3.12/site-packages (from flask->flask-wtf) (1.8.2)
# Requirement already satisfied: markupsafe in ./flask/lib/python3.12/site-packages (from wtforms->flask-wtf) (2.1.5)
# Downloading flask_wtf-1.2.1-py3-none-any.whl (12 kB)
# Downloading wtforms-3.1.2-py3-none-any.whl (145 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 146.0/146.0 kB 863.0 kB/s eta 0:00:00
# Installing collected packages: wtforms, flask-wtf
# Successfully installed flask-wtf-1.2.1 wtforms-3.1.2
# (flask) douxiaobo@192 formtohtml % 


# TemplateNotFound jinja2.exceptions.TemplateNotFound: login.html
# 办法是：在同一个文件夹里要创建Templates文件夹，然后在Templates文件夹里创建login.html文件。