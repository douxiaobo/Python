from flask import Flask, request

app=Flask(__name__)

@app.route('/')
def index():
    name=request.args.get('name')
    age=request.args.get('age')
    message=f"Hello {name}, you are {age} years old."
    return message

if __name__=='__main__':
    app.run(debug=True)




# Last login: Thu Jun  6 16:45:18 on ttys000
# douxiaobo@192 request_args_get % code .
# douxiaobo@192 request_args_get % python3 -m venv flask
# douxiaobo@192 request_args_get % source ./flask/bin/activate
# (flask) douxiaobo@192 request_args_get % pip insall flask
# ERROR: unknown command "insall" - maybe you meant "install"
# (flask) douxiaobo@192 request_args_get % pip3 install flask
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
# (flask) douxiaobo@192 request_args_get % python3 run.py
#  * Serving Flask app 'run'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 138-084-006
# 127.0.0.1 - - [06/Jun/2024 20:41:38] "GET /?name=andy&age=18 HTTP/1.1" 200 -



# http://127.0.0.1:5000/?name=andy&age=18
# Hello andy, you are 18 years old.