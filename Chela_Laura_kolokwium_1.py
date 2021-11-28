class Produkt:

    def __init__(self, nazwa: str, ilosc: int, cena: int, lokalizacja: str, producent: str):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.cena = cena
        self.lokalizacja = lokalizacja
        self.producent = producent

    def __str__(self):
        return f'Nazwa: {self.nazwa}\nProducent: {self.producent}'

    @property
    def stan(self):
        if self.ilosc > 100:
            return f'{self.nazwa} jest na stanie'


class Magazyn:

    def __init__(self, wielkość: str, lokalizacja: str, numer: int, obłożenie: str, produkt: str):
        self.wielkość = wielkość
        self.lokalizacja = lokalizacja
        self.numer = numer
        self.obłożenie = obłożenie
        self.produkt = produkt

    def __str__(self):
        return f'Numer magazynu: {self.numer}, produkt: {self.produkt}'
    
    @property
    def ktory_mg(self):
        return self.numer


class Klient:

    def __init__(self, nazwa: str, adres: str, nr_telefonu: str, region: int):
        self.nazwa = nazwa
        self.adres = adres
        self.nr_telefonu = nr_telefonu
        self.region = region

    def __str__(self):
        return f'Klasa nadrzędna klientów...'


class KlientDetaliczny(Klient):
    detaliczny = 'Tak'

    def __init__(self, nazwa: str, adres: str, nr_telefonu: str, region: int, detaliczny: str):
        super().__init__(nazwa, adres, nr_telefonu, region)
        self.detaliczny = detaliczny

    def __str__(self):
        return f'Klasa dziedzicząca Klienta...'

    @property
    def pod_adres(self):
        return self.adres


class KlientBiznesowy(Klient):

    def __init__(self, nazwa: str, adres: str, nr_telefonu: str, region: int, faktura: str):
        super().__init__(nazwa, adres, nr_telefonu, region)
        self.faktura = faktura

    def __str__(self):
        return f'Klasa dziedzicząca po Klient, faktura {self.faktura}'

    @property
    def czy_detaliczny(self):
        return self.faktura


class Zamówienie:
 #  klient : Klient
 #  produkt: Produkt

    def __init__(self, numer_zam: int, produkt: str, ile: int, cena: int, klient: str):
        self.numer_zam = numer_zam
        self.produkt = produkt
        self.ile = ile
        self.cena = cena
        self.klient = klient

    def __str__(self):
        return f'Zamówienie: {self.numer_zam} na klineta: {self.klient}'

    @property
    def pob_nr_zam(self):
        return self.numer_zam

    @property
    def pob_produkt(self):
        return self.produkt

    @property
    def pob_ilość(self):
        return self.ile

    @property
    def pob_cene(self):
        return self.cena

    @property
    def pob_klienta(self):
        return self.klient

    def wartość_zam(self):
        x = self.cena * self.ile
        x = round(x, 2)
        return x

    def adres_klienta(self):
        nazwa, ul, ulica, numer, kod_pocztowy, miasto = self.klient.split()
        return ul + ulica + numer + kod_pocztowy + miasto


prod = Produkt("karta gr", 50, 2000, "mały mag", "Acer")
cust = KlientBiznesowy("Adamex", "ul. Kwiatowa 65, 41-250 Kato", "123-456-789", 2, "NIP: 123333")

zam1 = Zamówienie(1012, "karta graficzna", 20, 2000, "Adamex, ul. Kwiatowa 65, 41-250 Katowice")

print("Opis zamówienia: ")
print(zam1.__str__())
print("\nWartość zamówienia: ")
print(zam1.wartość_zam())
print("\nAdres klienta: ")
print(zam1.adres_klienta())
