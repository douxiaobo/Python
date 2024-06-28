from flask import Flask, render_template, request, session, redirect, url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['username']=username
            session['logged_in']=True
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


# 运行失败。不掌握
# Last login: Fri Jun 28 20:31:01 on ttys001
# douxiaobo@192 render_template % code .
# douxiaobo@192 render_template % python3 -m venv flask
# douxiaobo@192 render_template % source flask/bin/activate
# (flask) douxiaobo@192 render_template % pip3 install flask
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

# [notice] A new release of pip is available: 24.0 -> 24.1.1
# [notice] To update, run: pip install --upgrade pip
# (flask) douxiaobo@192 render_template % python3 run.py
#  * Serving Flask app 'run'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 206-463-859
# 127.0.0.1 - - [28/Jun/2024 20:49:24] "GET /login HTTP/1.1" 500 -
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1498, in __call__
#     return self.wsgi_app(environ, start_response)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1476, in wsgi_app
#     response = self.handle_exception(e)
#                ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1473, in wsgi_app
#     response = self.full_dispatch_request()
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 882, in full_dispatch_request
#     rv = self.handle_user_exception(e)
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 880, in full_dispatch_request
#     rv = self.dispatch_request()
#          ^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 865, in dispatch_request
#     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/run.py", line 18, in login
#     return render_template('login.html')
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/templating.py", line 149, in render_template
#     template = app.jinja_env.get_or_select_template(template_name_or_list)
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/environment.py", line 1084, in get_or_select_template
#     return self.get_template(template_name_or_list, parent, globals)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/environment.py", line 1013, in get_template
#     return self._load_template(name, globals)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/environment.py", line 972, in _load_template
#     template = self.loader.load(self, name, self.make_globals(globals))
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/loaders.py", line 126, in load
#     source, filename, uptodate = self.get_source(environment, name)
#                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/templating.py", line 65, in get_source
#     return self._get_source_fast(environment, template)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/templating.py", line 99, in _get_source_fast
#     raise TemplateNotFound(template)
# jinja2.exceptions.TemplateNotFound: login.html
# 127.0.0.1 - - [28/Jun/2024 20:49:26] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [28/Jun/2024 20:49:26] "GET /favicon.ico HTTP/1.1" 404 -
# 127.0.0.1 - - [28/Jun/2024 20:51:01] "GET /login HTTP/1.1" 500 -
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1498, in __call__
#     return self.wsgi_app(environ, start_response)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1476, in wsgi_app
#     response = self.handle_exception(e)
#                ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1473, in wsgi_app
#     response = self.full_dispatch_request()
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 882, in full_dispatch_request
#     rv = self.handle_user_exception(e)
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 880, in full_dispatch_request
#     rv = self.dispatch_request()
#          ^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 865, in dispatch_request
#     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/run.py", line 18, in login
#     return render_template('login.html')
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/templating.py", line 149, in render_template
#     template = app.jinja_env.get_or_select_template(template_name_or_list)
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/environment.py", line 1084, in get_or_select_template
#     return self.get_template(template_name_or_list, parent, globals)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/environment.py", line 1013, in get_template
#     return self._load_template(name, globals)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/environment.py", line 972, in _load_template
#     template = self.loader.load(self, name, self.make_globals(globals))
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/loaders.py", line 126, in load
#     source, filename, uptodate = self.get_source(environment, name)
#                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/templating.py", line 65, in get_source
#     return self._get_source_fast(environment, template)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/templating.py", line 99, in _get_source_fast
#     raise TemplateNotFound(template)
# jinja2.exceptions.TemplateNotFound: login.html
# 127.0.0.1 - - [28/Jun/2024 20:51:02] "GET /login HTTP/1.1" 500 -
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1498, in __call__
#     return self.wsgi_app(environ, start_response)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1476, in wsgi_app
#     response = self.handle_exception(e)
#                ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1473, in wsgi_app
#     response = self.full_dispatch_request()
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 882, in full_dispatch_request
#     rv = self.handle_user_exception(e)
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 880, in full_dispatch_request
#     rv = self.dispatch_request()
#          ^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 865, in dispatch_request
#     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/run.py", line 18, in login
#     return render_template('login.html')
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/templating.py", line 149, in render_template
#     template = app.jinja_env.get_or_select_template(template_name_or_list)
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/environment.py", line 1084, in get_or_select_template
#     return self.get_template(template_name_or_list, parent, globals)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/environment.py", line 1013, in get_template
#     return self._load_template(name, globals)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/environment.py", line 972, in _load_template
#     template = self.loader.load(self, name, self.make_globals(globals))
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/jinja2/loaders.py", line 126, in load
#     source, filename, uptodate = self.get_source(environment, name)
#                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/templating.py", line 65, in get_source
#     return self._get_source_fast(environment, template)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/templating.py", line 99, in _get_source_fast
#     raise TemplateNotFound(template)
# jinja2.exceptions.TemplateNotFound: login.html
# 127.0.0.1 - - [28/Jun/2024 20:51:02] "GET /login?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -
# 127.0.0.1 - - [28/Jun/2024 20:51:02] "GET /login?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 -
# 127.0.0.1 - - [28/Jun/2024 20:51:02] "GET /login?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
# 127.0.0.1 - - [28/Jun/2024 20:51:02] "GET /login?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -
# 127.0.0.1 - - [28/Jun/2024 20:51:11] "GET /login HTTP/1.1" 200 -
# 127.0.0.1 - - [28/Jun/2024 20:51:35] "POST /login HTTP/1.1" 500 -
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1498, in __call__
#     return self.wsgi_app(environ, start_response)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1476, in wsgi_app
#     response = self.handle_exception(e)
#                ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 1473, in wsgi_app
#     response = self.full_dispatch_request()
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 882, in full_dispatch_request
#     rv = self.handle_user_exception(e)
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 880, in full_dispatch_request
#     rv = self.dispatch_request()
#          ^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/app.py", line 865, in dispatch_request
#     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/run.py", line 15, in login
#     session['username']=username
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/render_template/flask/lib/python3.12/site-packages/flask/sessions.py", line 102, in _fail
#     raise RuntimeError(
# RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
# 127.0.0.1 - - [28/Jun/2024 20:51:35] "GET /login?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 -
# 127.0.0.1 - - [28/Jun/2024 20:51:35] "GET /login?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 -
# 127.0.0.1 - - [28/Jun/2024 20:51:35] "GET /login?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -
# 127.0.0.1 - - [28/Jun/2024 20:51:35] "GET /login?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -
# 127.0.0.1 - - [28/Jun/2024 20:51:39] "GET /login HTTP/1.1" 200 -
# ^C%                                                                             (flask) douxiaobo@192 render_template % 