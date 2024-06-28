from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    print('视图函数执行')
    return 'index page'

#在第一次请求之前运行
@app.before_first_request
def before_first_request():
    print('before_first_request')

#在第一次请求前都会执行
@app.before_request
def before_request():
    print('before_request')

#在请求之后运行
@app.after_request
def after_request(response):
    print('after_request')
    return response

#无论视图函数是否出现异常，第一次请求之后都会调用，会接受一个参数
@app.teardown_request
def teardown_request(error):
    print('teardown_request: error %s' % error)

if __name__=='__main__':
    app.run(debug=True)


# douxiaobo@192 hook % python3 -m venv flask
# douxiaobo@192 hook % source ./flask/bin/activate
# (flask) douxiaobo@192 hook % pip3 install flask
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
# (flask) douxiaobo@192 hook % python3 hook.py
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/hook/hook.py", line 11, in <module>
#     @app.before_first_request
#      ^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'Flask' object has no attribute 'before_first_request'. Did you mean: '_got_first_request'?
# (flask) douxiaobo@192 hook % code .
# (flask) douxiaobo@192 hook % pip show flask
# Name: Flask
# Version: 3.0.3
# Summary: A simple framework for building complex web applications.
# Home-page:
# Author:
# Author-email:
# License:
# Location: /Users/douxiaobo/Documents/Practice in Coding/Python/hook/flask/lib/python3.12/site-packages
# Requires: blinker, click, itsdangerous, Jinja2, Werkzeug
# Required-by:
# (flask) douxiaobo@192 hook % python3 hook.py
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/hook/hook.py", line 11, in <module>
#     @app.before_first_request
#      ^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'Flask' object has no attribute 'before_first_request'. Did you mean: '_got_first_request'?
# (flask) douxiaobo@192 hook %
