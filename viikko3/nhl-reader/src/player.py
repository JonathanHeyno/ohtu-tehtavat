class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        #return self.name+" "+self.team+" "+str(self.goals)+" + "+str(self.assists)+" = "+str(self.goals+self.assists)
        return f"{self.name:30}"+f"{self.team:5}"+f"{str(self.goals):2}"+"  "+f"{str(self.assists):2}"+"  =  "+f"{str(self.goals+self.assists):2}"