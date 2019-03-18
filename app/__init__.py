from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './app/static/profile_pics'

ALLOWED_EXTS =set(['png','jpg'])



app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tifmbqnuadlsfc:46b554314cff72d0a57fe39c7bcd101ad5035aeb8ccd68b10515bff203b681eb@ec2-75-101-131-79.compute-1.amazonaws.com:5432/d81mmd336gnaht"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views