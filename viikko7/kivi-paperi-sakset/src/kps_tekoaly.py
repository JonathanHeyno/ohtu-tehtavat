#from tuomari import Tuomari
from tekoaly import Tekoaly
from KiviPaperiSakset import KPS

# luokka perii luokan KPS
class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly = Tekoaly()

    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()

        return tokan_siirto