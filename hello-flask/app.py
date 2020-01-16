from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey Flask!"

if __name__ == '__main__':
    app.run(debug=True)




# E:\school\FULL-STACK-COURSE\Python-Course\hello-flask>pipenv install flask
# Installing flask…
# Adding flask to Pipfile's [packages]…
# Installation Succeeded
# Pipfile.lock not found, creating…
# Locking [dev-packages] dependencies…
# Locking [packages] dependencies…
# Success!
# Updated Pipfile.lock (ac8e32)!
# Installing dependencies from Pipfile.lock (ac8e32)…
#   ================================ 6/6 - 00:00:01
# To activate this project's virtualenv, run pipenv shell.
# Alternatively, run a command inside the virtualenv with pipenv run.

# E:\school\FULL-STACK-COURSE\Python-Course\hello-flask>pipenv shell
# Launching subshell in virtual environment…
# Microsoft Windows [Version 10.0.18363.592]
# (c) 2019 Microsoft Corporation. All rights reserved.

# (hello-flask-oqiL98EQ) E:\school\FULL-STACK-COURSE\Python-Course\hello-flask>python app.py
#  * Serving Flask app "app" (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: on
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 275-452-218
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 127.0.0.1 - - [16/Jan/2020 09:47:13] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [16/Jan/2020 09:47:13] "GET /favicon.ico HTTP/1.1" 404 -