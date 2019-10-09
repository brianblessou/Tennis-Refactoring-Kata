"""
Main class to run excercise 2.
"""


class TennisGame2:
    def __init__(self, player_one_name, player_two_name):
        """
        Initialization parameters
        :param player_one_name:  name for player one.
        :param player_two_name:  name for player two.
        """
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """
        Funciton to call to add a point for a given player.
        :param player_name: name of the player.
        """
        if player_name == self.player_one_name:
            self.p1points += 1
        else:
            self.p2points += 1

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
            return self._calculate_score(self.p1points) + "-All"
        else:
            return "Deuce"

    def _parse_nonequals(self):
        """
        Internal function to calculate the scores if they are not equal.
        :return: outputstring
        """
        minus_result = self.p1points - self.p2points
        if self.p1points > 2 and self.p2points > 2:
            if minus_result == 1 or minus_result == -1:
                return self._parse_differences_scores(minus_result)
        if self.p1points >= 4 or self.p2points >= 4:
            return self._parse_differences_scores(minus_result)
        else:
            return self._get_other_result()

    def _parse_differences_scores(self, minusResult):
        """
        Internal function to calculate the differences between the scores if the scores are bigger than 3.
        If the difference is equal to abs(1), somebody has an advantage, if its beq abs(2), somebody has a win.
        :return: outputstring
        """
        if minusResult == 1:
            return "Advantage " + self.player_one_name
        if minusResult == -1:
            return "Advantage " + self.player_two_name
        if minusResult >= 2:
            return "Win for " + self.player_one_name
        if minusResult <= -2:
            return "Win for " + self.player_two_name
        else:
            return self._get_other_result()

    def _get_other_result(self):
        """
        Internal function to calculate the differences if its not an advantage or a win.
        We first get the output string for P1 & p2, then concat this to get the output string.
        :return: outputstring
        """
        P1res = self._calculate_score(self.p1points)
        P2res = self._calculate_score(self.p2points)
        return P1res + "-" + P2res

    def _calculate_score(self, points):
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
