import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = 10

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_nollaa_virheellisen_tilavuuden(self):
        self.varasto = Varasto(-2)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_nollaa_virheellisen_alkusaldon(self):
        self.varasto = Varasto(10, -2)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_tayttaa_varaston_kun_saldo_yli_tilavuuden(self):
        self.varasto = Varasto(10, 11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_vaara_lisays_ei_muuta_varastoa(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_suuri_lisays_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_ottaminen_ei_muuta_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_tyhjentäminen_palauttaa_kaiken_otettavan(self):
        self.varasto.lisaa_varastoon(8)
        tyhjennys = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(tyhjennys, 8)

    def test_tulostaminen_toimii(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
