from classes.Property import Property


class House(Property):
    plot: int

    def __init__(self, area: str, rooms: int, price: str, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'rozmiar działki: {self.plot}'
