from datetime import datetime
from shop import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash





class Item(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    carbon = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(40), nullable=False,default='default.jpg')
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}','{self.description}')"

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128))
    items = []

    def __repr__(self):
        return f"User('{self.username}')"

    @property
    def password(self):
        raise AttributeError('Password is not readable.')

    @password.setter
    def password(self,password):
        self.hashed_password=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hashed_password,password)


@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

