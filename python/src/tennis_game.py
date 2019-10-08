# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def calculate_equal_score(self,score):
        """
        This function calculates the scores when they are equal.
        :return: a string containing the score.
        """
        return {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All",
        }.get(score, "Deuce")

    def calculate_gte_four(self,
                           player_one_score,
                           player_two_score
                           ):
        """
        This function calculates the score when they are bigger or equal than four.
        :return: a string containing the score.
        """
        minusResult = player_one_score-player_two_score

        if (minusResult==1):
            return "Advantage " + self.player1Name
        elif (minusResult ==-1):
            return "Advantage " + self.player2Name
        elif (minusResult>=2):
            return "Win for " + self.player1Name
        else:
            return "Win for " + self.player2Name

    def score(self):
        if (self.p1points==self.p2points):
            result = self.calculate_equal_score(self.p1points)
        elif (self.p1points>=4 or self.p2points>=4):
            result = self.calculate_gte_four(self.p1points,self.p2points)
        else:
            result = self.getScore(self.p1points) + "-"  +  self.getScore(self.p2points)
        return result

    def getScore(self,score):
            return {
                0 : "Love",
                1 : "Fifteen",
                2 : "Thirty",
                3 : "Forty",
            }[score]




