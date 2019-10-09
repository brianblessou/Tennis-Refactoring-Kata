class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points +=1
        else:
            self.p2points +=1

    def calculate_score(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        else:
            return "Forty"


    def score(self):
        result = ""
        if self.p1points == self.p2points:
            if self.p1points < 3:
                result = self.calculate_score(self.p1points) + "-All"
            else:
                result = "Deuce"

        if (self.p1points or self.p2points < 4):

            if (self.p2points != self.p1points ) \
                or (self.p2points > 0 and self.p1points==0) \
                or (self.p1points > 0 and self.p2points==0):
                P1res = self.calculate_score(self.p1points)
                P2res = self.calculate_score(self.p2points)
                result = P1res + "-" + P2res

            if self.p1points > self.p2points:
                if self.p2points >= 3:
                     result = "Advantage " + self.player1Name

            if self.p2points > self.p1points:
                 if self.p1points >= 3:
                     result = "Advantage " + self.player2Name


        if self.p1points>=4 or self.p2points >= 4:
            if self.p2points>=0 or self.p1points >= 0:
                minusResult = self.p1points - self.p2points
                if minusResult>=2:
                    result = "Win for " + self.player1Name
                if minusResult <= -2:
                    result = "Win for " + self.player2Name

        return result




