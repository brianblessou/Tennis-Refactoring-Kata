
import unittest
from src.tennisgame1.matchpoints import  MatchPoints

class TestMatchPoints(unittest.TestCase):
    def test_calculate_gte_four(self):
        p1Name = "player_one"
        p2Name = "player_two"

        actual = MatchPoints(p1Name, p2Name,3,2).calculate_score_matchpoint()
        assert(actual == "Advantage player_one")

        actual = MatchPoints(p1Name, p2Name,4,2).calculate_score_matchpoint()
        assert(actual == "Win for player_one")

        actual = MatchPoints(p1Name, p2Name,2,3).calculate_score_matchpoint()
        assert(actual == "Advantage player_two")

        actual = MatchPoints(p1Name, p2Name,2,4).calculate_score_matchpoint()
        assert(actual == "Win for player_two")
