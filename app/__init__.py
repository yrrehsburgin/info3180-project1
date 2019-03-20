from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://iayihqcjfespgd:b544d094ece0771fa0f63b9f84f2f8df95c1411e276a503194ca76196a3074b7@ec2-50-17-227-28.compute-1.amazonaws.com:5432/d2i000hqf9obno"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
