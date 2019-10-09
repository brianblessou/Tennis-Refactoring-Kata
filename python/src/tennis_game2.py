"""
Main class to run excercise 2.
"""
class TennisGame2:
    def __init__(self, player1Name, player2Name):
        """
        Initialization parameters
        :param player1Name:  name for player one.
        :param player2Name:  name for player two.
        """
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        """
        Funciton to call to add a point for a given player.
        :param playerName: name of the player.
        """
        if playerName == self.player1Name:
            self.p1points +=1
        else:
            self.p2points +=1

    def score(self):
        """
        Function to calculate the score
        :return: string containing the outcome.
        """
        if self.p1points == self.p2points:
            return self._parse_lte_equals()
        else:
            return self._parse_nonequals()

    def _parse_lte_equals(self):
        """
        Internal funciton to calculate the scores if they are less than 3 and equal.
        :return: outputstring
        """
        if self.p1points < 3:
            return self.calculate_score(self.p1points) + "-All"
        else:
            return "Deuce"

    def _parse_nonequals(self):
        """
        Internal function to calculate the scores if they are not equal.
        :return: outputstring
        """
        minusResult = self.p1points - self.p2points
        if self.p1points > 2 and self.p2points > 2:
            if minusResult == 1 or minusResult == -1:
                return self._parse_differences_scores(minusResult)
        if self.p1points >= 4 or self.p2points >= 4:
            return self._parse_differences_scores(minusResult)
        else:
            return self.get_other_result()

    def _parse_differences_scores(self, minusResult):
        """
        Internal function to calculate the differences between the scores if the scores are bigger than 3.
        If the difference is equal to abs(1), somebody has an advantage, if its beq abs(2), somebody has a win.
        :return: outputstring
        """
        if minusResult == 1:
            return "Advantage " + self.player1Name
        if minusResult == -1:
            return  "Advantage " + self.player2Name
        if minusResult >= 2:
            return "Win for " + self.player1Name
        if minusResult <= -2:
            return  "Win for " + self.player2Name
        else:
            return self.get_other_result()

    def get_other_result(self):
        """
        Internal function to calculate the differences if its not an advantage or a win.
        We first get the output string for P1 & p2, then concat this to get the output string.
        :return: outputstring
        """
        P1res = self.calculate_score(self.p1points)
        P2res = self.calculate_score(self.p2points)
        return P1res + "-" + P2res

    def calculate_score(self, points):
        """
        Internal method to map points to the output. ex: 0 => Love
        :param points: points of the player
        :return: outputstring.
        """
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        else:
            return "Forty"





