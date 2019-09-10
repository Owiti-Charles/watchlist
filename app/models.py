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