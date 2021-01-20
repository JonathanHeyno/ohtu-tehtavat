import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_loytyy(self):
        pelaaja = self.statistics.search("Lemieux")
        self.assertEqual(pelaaja.name, "Lemieux")

    def test_search_ei_loydy(self):
        self.assertIsNone(self.statistics.search("Aapo"))

    def test_team_loytyy(self):
        self.assertIsNotNone(self.statistics.team("EDM"))

    def test_top_scorers(self):
        self.assertEqual(len(self.statistics.top_scorers(2)), 3)

