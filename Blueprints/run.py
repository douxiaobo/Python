from flask import Flask
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app = Flask(__name__)
app.register_blueprint(home_blueprint, url_prefix='/home')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)


# Last login: Mon Jun  3 18:47:38 on ttys000
# douxiaobo@192 Blueprints % code .
# douxiaobo@192 Blueprints % python3 run.py
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/Blueprints/run.py", line 1, in <module>
#     from flask import Flask
# ModuleNotFoundError: No module named 'flask'
# douxiaobo@192 Blueprints % python3 -m venv flask
# douxiaobo@192 Blueprints % source flask/bin/activate
# (flask) douxiaobo@192 Blueprints % pip3 install flask
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
# (flask) douxiaobo@192 Blueprints % python3 run.py           
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/Blueprints/run.py", line 2, in <module>
#     from app.home import home as home_blueprint
# ModuleNotFoundError: No module named 'app'
# (flask) douxiaobo@192 Blueprints % python3 run.py
#  * Serving Flask app 'run'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 839-196-592
# 127.0.0.1 - - [03/Jun/2024 21:02:19] "GET / HTTP/1.1" 404 -
# 127.0.0.1 - - [03/Jun/2024 21:02:23] "GET /login HTTP/1.1" 404 -
# 127.0.0.1 - - [03/Jun/2024 21:02:23] "GET /favicon.ico HTTP/1.1" 404 -
# 127.0.0.1 - - [03/Jun/2024 21:02:32] "GET /admin HTTP/1.1" 308 -
# 127.0.0.1 - - [03/Jun/2024 21:02:32] "GET /admin/ HTTP/1.1" 200 -
# 127.0.0.1 - - [03/Jun/2024 21:02:38] "GET /home HTTP/1.1" 308 -
# 127.0.0.1 - - [03/Jun/2024 21:02:38] "GET /home/ HTTP/1.1" 200 -
# ^C%                                                                             
# (flask) douxiaobo@192 Blueprints % 


# The error message ModuleNotFoundError: 
# No module named 'app' suggests that Python cannot find the app module, which should contain the blueprints home and admin. 
# The issue might be due to one of the following reasons:

# Directory structure: 
# Make sure your directory structure is organized correctly. 
# If your run.py file and the app folder with the home.py and admin.py files are not in the same level, you need to adjust the import statement.

# If your directory looks like this:
#    Blueprint/
#      ├── run.py
#      └── app/
#          ├── home.py
#          └── admin.py