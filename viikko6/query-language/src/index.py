from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, All, QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    #matcher = query.build()
    #matcher = query.playsIn("NYR").build()

    matcher = (
        query
            .oneOf(
            query.playsIn("PHI")
                .hasAtLeast(10, "assists")
                .hasFewerThan(5, "goals")
                .build(),
            query.playsIn("EDM")
                .hasAtLeast(40, "points")
                .build()
        )
            .build()
    )

    '''
    matcher = (
      query
        .playsIn("NYR")
        .hasAtLeast(5, "goals")
        .hasFewerThan(10, "goals")
        .build()
    )
    '''




    '''
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )
    '''

    '''
    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )
    '''


    '''
    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )
    '''

    '''
    matcher = And(
        HasAtLeast(20, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("NJD")
        )
    )
    '''

    #matcher = All()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
