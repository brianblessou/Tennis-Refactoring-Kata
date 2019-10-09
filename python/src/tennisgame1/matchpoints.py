
"""
Class to calculate the outcome string when the scores are above 40.
"""
class MatchPoints():

    def __init__(self,
             player_one_name,
             player_two_name,
             player_one_score,
             player_two_score
             ):
        """
        Constructor
        :param player_one_name:  name of player one.
        :param player_two_name:  name of player two.
        :param player_one_score:  score of player one.
        :param player_two_score:  score of player two.
        """

        self.player_one_score = player_one_score
        self.player_two_score = player_two_score
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name


    def calculate_score_matchpoint(self):
        """
        This function calculates the score when they are bigger or equal than four.
        :return: a string containing the score.
        """
        minusResult = self.player_one_score - self.player_two_score

        if (minusResult==1):
           return "Advantage " + self.player_one_name
        elif (minusResult ==-1):
           return "Advantage " + self.player_two_name
        elif (minusResult>=2):
            return "Win for " + self.player_one_name
        elif (minusResult <=-2):
            return "Win for " + self.player_two_name
        else:
            raise Exception("This should never be reached.")
