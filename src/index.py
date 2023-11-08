from varasto import Varasto


def start(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def errors(tilavuus, alkusaldo=None):
    huono = Varasto(tilavuus)
    if not alkusaldo:
        print(f"Varasto({tilavuus});")
    else:
        print(f"Varasto({tilavuus}, {alkusaldo})")
    print(huono)

def add_or_remove(varastotyyppi, varasto, toimenpide, maara):
    print(f"{varastotyyppi}: {varasto}")

    if varastotyyppi == "Olutvarasto":
        if toimenpide == "lisaa":
            print(f"olutta.lisaa_varastoon({maara})")
            varasto.lisaa_varastoon(maara)
        elif toimenpide == "ota":
            print(f"""olutta.ota_varastosta({maara})
                  saatiin {varasto.ota_varastosta(maara)}""")

    elif varastotyyppi == "Mehuvarasto":
        if toimenpide == "lisaa":
            print(f"mehua.lisaa_varastoon({maara})")
            varasto.lisaa_varastoon(maara)
        elif toimenpide == "ota":
            print(f"""mehua.otaVarastosta({maara})
                  saatiin {varasto.ota_varastosta(maara)}""")

    print(f"{varastotyyppi}: {varasto}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    start(mehua, olutta)

    print("Virhetilanteita:")
    errors(-100.0)
    errors(100.0, -50.7)

    add_or_remove("Olutvarasto", olutta, "lisaa", 1000.0)

    add_or_remove("Mehuvarasto", mehua, "lisaa", -666.0)

    add_or_remove("Olutvarasto", olutta, "ota", 1000.0)

    add_or_remove("Mehuvarasto", mehua, "ota", -32.9)


if __name__ == "__main__":
    main()
