
import unittest
from src.tennisgame1.equalitypoints import EqualityPoints

class TestEqualityPoints(unittest.TestCase):

    def test_calculate_equal_score(self):
        game = EqualityPoints()

        actual = game.calculate_score_equality(0)
        expected = "Love-All"
        assert(actual == expected)

        actual = game.calculate_score_equality(1)
        expected = "Fifteen-All"
        assert(actual == expected)

        actual = game.calculate_score_equality(2)
        expected = "Thirty-All"
        assert(actual == expected)

        actual = game.calculate_score_equality(3)
        expected = "Deuce"
        assert(actual == expected)
