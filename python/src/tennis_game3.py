class TennisGame3:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_score = 0
        self.player_two_score = 0

    def won_point(self, current_player):
        if current_player == self.player_one_name:
            self.player_one_score += 1
        else:
            self.player_two_score += 1

    def score(self):
        if (self.player_one_score < 4 and self.player_two_score < 4) \
                and (self.player_one_score + self.player_two_score < 6):
            result_scores = ["Love", "Fifteen", "Thirty", "Forty"]
            result_string = result_scores[self.player_one_score]
            if self.player_one_score == self.player_two_score:
                return result_string + "-All"
            else:
                return result_string + "-" + result_scores[self.player_two_score]
        else:
            if self.player_one_score == self.player_two_score:
                return "Deuce"
            if self.player_one_score > self.player_two_score:
                winning_player = self.player_one_name
            else:
                winning_player = self.player_two_name
            if (self.player_one_score - self.player_two_score) * (self.player_one_score - self.player_two_score) == 1:
                    return "Advantage " + winning_player
            else: return "Win for " + winning_player
