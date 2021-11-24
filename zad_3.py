# 3.
print("Zad.3")

class Property:
    area: str
    rooms: int
    price: str
    address: str

    def __init__(self, area: str, rooms: int, price: str, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Obszar: {self.area}, liczba pokoi: {self.rooms}, cena: {self.cena}, adres: {self.address}'

class House(Property):
    plot: int

    def __init__(self, area: str, rooms: int, price: str, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'rozmiar działki: {self.plot}'

class Flat(Property):
    floor: int

    def __init__(self, area: str, rooms: int, price: str, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'numer piętra: {self.floor}'


x = House("wieś", 7, "500000 zł", "ul. Kwiatowa 3, 42-432 Gliwice", 1000)
y = Flat("miasto", 7, "200000 zł", "ul. Tulipanowa 23, 40-234 Katowice", 4)

print(x)
print(y)
