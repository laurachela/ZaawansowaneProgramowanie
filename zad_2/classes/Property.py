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
        return f'Obszar: {self.area}, liczba pokoi: {self.rooms}, cena: {self.price}, adres: {self.address}'
