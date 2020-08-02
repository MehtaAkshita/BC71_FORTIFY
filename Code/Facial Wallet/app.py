from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['UPLOAD_FOLDER'] = '/uploads'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'this_is_a_secret_key'

db = SQLAlchemy(app)


from views import *
from models import *

db.create_all()

if __name__ == '__main__':
    app.run()
