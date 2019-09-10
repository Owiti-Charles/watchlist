import unittest
from app.models import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.new_review = Review(12345,'Review for movies',"https://image.tmdb.org/t/p/w500/jdjdjdjn",'This movie is the best thing since sliced bread')


    def tearDown(self):
        Review.clear_all_reviews()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,12345)
        self.assertEquals(self.new_review.title,'Review for movies')
        self.assertEquals(self.new_review.imageurl,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.review,'This movie is the best thing since sliced bread')


    def test_save_review(self):
        self.new_review.save()
        self.assertTrue(len(Review.reviews)>0)

if __name__ == '__main__':
    unittest.main()