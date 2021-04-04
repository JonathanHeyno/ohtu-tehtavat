from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KPSTehdas:
    def annaPelaaja(self, vastaus):
        if vastaus.endswith("a"):
            return KPSPelaajaVsPelaaja()
        elif vastaus.endswith("b"):
            return KPSTekoaly()
        elif vastaus.endswith("c"):
            return KPSParempiTekoaly()
        else:
            return