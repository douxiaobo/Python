from flask import Flask, url_for, redirect,render_template

app = Flask(__name__)

@app.route('/')
def index():
    name="Microsoft"    #Jinja2
    message="Hello World!"
    return render_template('index.html',name=name,message=message)

if __name__ == '__main__':
    app.run(debug=True)

# douxiaobo@192 render_template_flask % python 3 -m venv flask
# zsh: command not found: python
# douxiaobo@192 render_template_flask % python3 -m venv flask
# douxiaobo@192 render_template_flask % source flask/bin/activate
# (flask) douxiaobo@192 render_template_flask % pip3 install flask
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
# (flask) douxiaobo@192 render_template_flask % 