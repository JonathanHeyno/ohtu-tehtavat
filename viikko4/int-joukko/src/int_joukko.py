KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.luvut = list()

    def kuuluu(self, n):
        return n in self.luvut

    def lisaa(self, n):
        if not n in self.luvut:
            self.luvut.append(n)

    def poista(self, n):
        if n in self.luvut:
            self.luvut.remove(n)

    def mahtavuus(self):
        return len(self.luvut)

    def to_int_list(self):
        return self.luvut.copy()


    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if not self.luvut:
            return "{}"

        tuotos = "{" + str(self.luvut[0])
        for i in range(1, len(self.luvut)):
            tuotos += ", "+str(self.luvut[i])
        tuotos += "}"
        return tuotos