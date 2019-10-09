# -*- coding: utf-8 -*-

from src.tennisgame1.equalitypoints import EqualityPoints
from src.tennisgame1.matchpoints import MatchPoints
from src.tennisgame1.regularpoints import RegularPoints


"""Main run method."""
class TennisGame1:

    def __init__(self, player1Name, player2Name):
        """
        Constructor
        :param player1Name: name of player one.
        :param player2Name:  name of player two.
        """
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        """
        Method to increment the score if a certain player won a point.
        :param playerName: player who wins a point
        :return: player who increments a poont
        """
        if playerName == self.player1Name:
            self.p1points += 1
        elif playerName == self.player2Name:
            self.p2points += 1
        else:
            raise Exception("The player name is invalid.")


    def score(self):
        """
        Helper method to calculate the output score from the points.
        :return: string containing the parsed score.
        """
        if (self.p1points==self.p2points):
            return EqualityPoints().calculate_score_equality(self.p1points)

        elif (self.p1points>=4 or self.p2points>=4):
            return MatchPoints(self.player1Name,
                               self.player2Name,
                               self.p1points,
                               self.p2points).calculate_score_matchpoint()
        else:
            return RegularPoints(
                                 ).calculate_score_regular_points(self.p1points,self.p2points)



