# -*- coding: utf-8 -*-

import unittest

from src.tennis_game import TennisGame1

test_cases = [
    (0, 0, "Love-All", 'player1', 'player2'),
    (1, 1, "Fifteen-All", 'player1', 'player2'),
    (2, 2, "Thirty-All", 'player1', 'player2'),
    (3, 3, "Deuce", 'player1', 'player2'),
    (4, 4, "Deuce", 'player1', 'player2'),

    (1, 0, "Fifteen-Love", 'player1', 'player2'),
    (0, 1, "Love-Fifteen", 'player1', 'player2'),
    (2, 0, "Thirty-Love", 'player1', 'player2'),
    (0, 2, "Love-Thirty", 'player1', 'player2'),
    (3, 0, "Forty-Love", 'player1', 'player2'),
    (0, 3, "Love-Forty", 'player1', 'player2'),
    (4, 0, "Win for player1", 'player1', 'player2'),
    (0, 4, "Win for player2", 'player1', 'player2'),

    (2, 1, "Thirty-Fifteen", 'player1', 'player2'),
    (1, 2, "Fifteen-Thirty", 'player1', 'player2'),
    (3, 1, "Forty-Fifteen", 'player1', 'player2'),
    (1, 3, "Fifteen-Forty", 'player1', 'player2'),
    (4, 1, "Win for player1", 'player1', 'player2'),
    (1, 4, "Win for player2", 'player1', 'player2'),

    (3, 2, "Forty-Thirty", 'player1', 'player2'),
    (2, 3, "Thirty-Forty", 'player1', 'player2'),
    (4, 2, "Win for player1", 'player1', 'player2'),
    (2, 4, "Win for player2", 'player1', 'player2'),

    (4, 3, "Advantage player1", 'player1', 'player2'),
    (3, 4, "Advantage player2", 'player1', 'player2'),
    (5, 4, "Advantage player1", 'player1', 'player2'),
    (4, 5, "Advantage player2", 'player1', 'player2'),
    (15, 14, "Advantage player1", 'player1', 'player2'),
    (14, 15, "Advantage player2", 'player1', 'player2'),

    (6, 4, 'Win for player1', 'player1', 'player2'), 
    (4, 6, 'Win for player2', 'player1', 'player2'), 
    (16, 14, 'Win for player1', 'player1', 'player2'), 
    (14, 16, 'Win for player2', 'player1', 'player2'), 

    (6, 4, 'Win for One', 'One', 'player2'),
    (4, 6, 'Win for Two', 'player1', 'Two'), 
    (6, 5, 'Advantage One', 'One', 'player2'),
    (5, 6, 'Advantage Two', 'player1', 'Two'), 
    
    ]

def play_game(TennisGame, p1Points, p2Points, p1Name, p2Name):
    game = TennisGame(p1Name, p2Name)
    for i in range(max(p1Points, p2Points)):
        if i < p1Points:
            game.won_point(p1Name)
        if i < p2Points:
            game.won_point(p2Name)
    return game

class TestTennis(unittest.TestCase):
     
    def test_Score_Game1(self):
        for testcase in test_cases:
            (p1Points, p2Points, score, p1Name, p2Name) = testcase
            game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
            self.assertEqual(score, game.score())

    def test_calculate_equal_score(self):
        p1Name = "player_one"
        p2Name = "player_two"
        game = TennisGame1(p1Name, p2Name)

        actual = game.calculate_equal_score(0)
        expected = "Love-All"
        assert(actual == expected)


        actual = game.calculate_equal_score(1)
        expected = "Fifteen-All"
        assert(actual == expected)

        actual = game.calculate_equal_score(2)
        expected = "Thirty-All"
        assert(actual == expected)

        actual = game.calculate_equal_score(3)
        expected = "Deuce"
        assert(actual == expected)

    def test_calculate_gte_four(self):
        p1Name = "player_one"
        p2Name = "player_two"
        game = TennisGame1(p1Name, p2Name)

        actual = game.calculate_gte_four(self)

if __name__ == "__main__":
    unittest.main()
