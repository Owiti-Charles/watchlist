from . import db
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy="dynamic")
    def __repr__(self):
        return f'User {self.name}'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
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