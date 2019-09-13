from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin 
from . import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy="dynamic")    
    
    def __repr__(self):
        return f'User {self.name}'


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),index = True)
    pass_secure = db.Column(db.String(255))
    email  = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError("You cannot read the pasword")

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'


class Movie:
    def __init__(self,id,title,overview,image,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.image = 'https://image.tmdb.org/t/p/w500/'+ image
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review:
    reviews = []
    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self. imageurl = imageurl
        self.review = review
    def save(self):
        Review.reviews.append(self)
    
    @classmethod
    def clear_all_reviews(cls):
        Review.reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.reviews:
            if review.movie_id == id:
                response.append(review)

        return response