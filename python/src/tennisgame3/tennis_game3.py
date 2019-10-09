"""
Main runfunciton for tennisgame 3.
"""

class TennisGame3:
    def __init__(self, player_one_name, player_two_name):
        """
        Initialization parameters
        :param player_one_name:  name for player one.
        :param player_two_name:  name for player two.
        """
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_score = 0
        self.player_two_score = 0
        self.result_scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, current_player):
        """
        Function to call to add a point for a given player.
        :param player_name: name of the player.
        """
        if current_player == self.player_one_name:
            self.player_one_score += 1
        else:
            self.player_two_score += 1

    def score(self):
        """
        Function to calculate the score
        :return: string containing the outcome.
        """
        if (self.player_one_score < 4 and self.player_two_score < 4) \
                and (self.player_one_score + self.player_two_score < 6):
            return self.parse_equals_or_regular_points(self.result_scores)
        else:
            if self.player_one_score == self.player_two_score:
                return "Deuce"
            winning_player = self.get_winning_player()
            return self.parse_advantage_or_win(winning_player)

    def parse_equals_or_regular_points(self, score_array):
        """
        Helper function to parse the game if or the two scores are equal. (if statement one)
        or if the game is not equal, but the added scores are less than 6 (So no advantage or win) and
        each player has an individual score of less than 4. (So no win. => can happen that 4-0 is a win)
        :param score_array: array containing strings to calculate the output string containing the scores.
        :return: output string.
        """
        player_one_score = score_array[self.player_one_score]
        if self.player_one_score == self.player_two_score:
            return player_one_score + "-All"
        else:
            return player_one_score + "-" + score_array[self.player_two_score]

    def parse_advantage_or_win(self,winning_player):
        """
        Helper function to parse get the output score if the game is at a stage that is
        either an advantage or somebody will win.
        :param winning_player: player with the advantage.
        :return: output result.
        """
        if (self.player_one_score - self.player_two_score) * (self.player_one_score - self.player_two_score) == 1:
            return "Advantage " + winning_player
        else:
            return "Win for " + winning_player

    def get_winning_player(self):
        """
        Helper function to calculate the player who has an advantage or won.
        :return: player with the highest score.
        """
        if self.player_one_score > self.player_two_score:
            return self.player_one_name
        else:
            return self.player_two_name
