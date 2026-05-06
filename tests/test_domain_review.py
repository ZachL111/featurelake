import unittest

from src.featurelake.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(40, 24, 9, 77)
        self.assertEqual(review_score(item), 154)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()
