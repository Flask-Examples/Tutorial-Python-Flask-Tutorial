"""
Flask Tutorials - Corey Schafer.

Python Flask Tutorial_ Full-Featured Web App

Module: Flask, flask-wtf, flask-sqlalchemy, flask-bcrypt, flask-login
       Pillow, flask-mail

set WORKON_HOME=%cd%

Usuários - 
:CoreyMS
:coreyms@blog.com
:coreyms

"""

from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
