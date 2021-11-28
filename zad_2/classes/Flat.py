from classes.Property import Property


class Flat(Property):
    floor: int

    def __init__(self, area: str, rooms: int, price: str, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'numer piętra: {self.floor}'
