from kps_tehdas import KPSTehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        peli = KPSTehdas().annaPelaaja(vastaus)

        if not peli:
            break
        else:
            peli.pelaa()


if __name__ == "__main__":
    main()
