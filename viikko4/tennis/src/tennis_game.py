class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.points()

    def points(self):
        self.points = {0: "Love",
                       1: "Fifteen",
                       2: "Thirty",
                       3: "Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def even(self):
        if self.m_score1 < 4:
            return self.points.get(self.m_score1)+"-All"
        else:
            return "Deuce"

    def aboutToWin(self):
        leaderName = self.player2_name
        if self.m_score1 >= self.m_score2:
            leaderName = self.player1_name

        if abs(self.m_score1-self.m_score2) == 1:
            return "Advantage "+leaderName
        return "Win for "+leaderName

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.even()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.aboutToWin()

        else:
            return self.points.get(self.m_score1)+"-"+self.points.get(self.m_score2)

