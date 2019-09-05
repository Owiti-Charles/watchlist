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
