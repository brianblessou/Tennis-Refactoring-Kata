"""
class to calculate the outcome string when the scores are equal.
"""


class EqualityPoints(object):

    @staticmethod
    def calculate_score_equality(score):
        """
        This function calculates the scores when they are equal.
        :return: a string containing the score.
        """
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(score, "Deuce")
