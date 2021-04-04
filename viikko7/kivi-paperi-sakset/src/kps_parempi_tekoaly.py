from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from KiviPaperiSakset import KPS

# luokka perii luokan KPS
class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ekan_siirto)

        return tokan_siirto