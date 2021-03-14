import PlayerReader

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        self.reader.players.sort(key=lambda x: (x.assists + x.goals), reverse=True)
        rettari = []
        for player in self.reader.players:
            if player.nationality == nationality:
                rettari.append(player)
        return rettari