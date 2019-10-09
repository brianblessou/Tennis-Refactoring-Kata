"""
Class to calculate the scores when the points are not equal or above 40.
"""


class RegularPoints(object):


    def calculate_score_regular_points(self,
                                       player_one_score,
                                       player_two_score):
        """
        Helper to get the general score for two players.
        :return: String with the game score.
        """
        return self._calculate_player_score(player_one_score) + \
               "-" + self._calculate_player_score(player_two_score)

    def _calculate_player_score(self,
                                score):
        """
        This function calculates an individual player his score
        :param score:  the score to calculate
        :return:  the corresponding string value.
        """
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }[score]
