from PlayerReader import PlayerReader
from PlayerStats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)




if __name__ == "__main__":
    main()






#from player import Player

#def main():
#    pass

#import requests
#from player import Player

'''
def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name']
        )

        players.append(player)

    print("Oliot:")

    for player in players:
        print(player)
'''