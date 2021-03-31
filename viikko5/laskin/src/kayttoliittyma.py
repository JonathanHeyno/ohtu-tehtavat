from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote)
        }

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovelluslogiikka.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        if not komento == Komento.KUMOA:
            self._komennot[Komento.KUMOA].asetaEdellinen(komento_olio)
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL


        if self._sovelluslogiikka.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.tulos)



class Operaatio:
    def __init__(self, sovelluslogiikka, luku):
        self.sovelluslogiikka = sovelluslogiikka
        self.luku = luku
        self.edellinen = 0
    def alusta(self):
        arvo = int(self.luku())
        self.edellinen = self.sovelluslogiikka.tulos
        return arvo
    def suorita(self):
        pass
    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen)


class Summa(Operaatio):
    def __init__(self, sovelluslogiikka, luku):
        super().__init__(sovelluslogiikka, luku)
    def suorita(self):
        self.sovelluslogiikka.plus(self.alusta())


class Erotus(Operaatio):
    def __init__(self, sovelluslogiikka, luku):
        super().__init__(sovelluslogiikka, luku)
    def suorita(self):
        self.sovelluslogiikka.miinus(self.alusta())


class Nollaus(Operaatio):
    def __init__(self, sovelluslogiikka, luku):
        super().__init__(sovelluslogiikka, luku)
    def suorita(self):
        self.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.nollaa()


class Kumoa:
    def __init__(self, sovelluslogiikka, luku):
        self.edellinen = self
    def asetaEdellinen(self, olio):
        self.edellinen = olio
    def suorita(self):
        self.edellinen.kumoa()
    def kumoa(self):
        pass