# 1. Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
# logiczną, pozytywną gdy ocena jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
# obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .
print("Zad.1")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Dane studenta:\nImię i nazwisko: {self.name}'

    def is_passed(self):
        if self.marks > 50:
            return True
        else:
            return False

    def powitanie(self):
        print(f"Hi, {self.name}. Wynik twoich ocen to {self.marks}")


s1 = Student('Adam N', 55)
s2 = Student('Andrzej N', 45)

s1.powitanie()
print(s1.is_passed())

s2.powitanie()
print(s2.is_passed())

# 2.
print("Zad.2")

from datetime import date

class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Adres biblioteki: ul. {self.street}, {self.zip_code} {self.city}. Jest ona otwarta w godzinach: ' \
               f'{self.open_hours}. Telefon: {self.phone}'

class Employee:
    first_name: str
    last_name: str
    hire_date: date
    birth_date: date
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(self, first_name: str, last_name: str, hire_date: date, birth_date: date, city: str,
                 street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Dane pracownika biblioteki:\nImię i nazwisko: {self.first_name} {self.last_name}\nData urodzenia: ' \
               f'{self.birth_date}\nAdres zamieszkania: ul. {self.street}, {self.zip_code} {self.city}\nTelefon: ' \
               f'{self.phone}'


class Book:
    library: Library
    public_date: date
    author_name: str
    author_surname: str
    number_of_pages: int

    def __init__(self, library: Library, publication_date: date, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Dane książki:\nAutor: {self.author_name} {self.author_surname}\nData publikacji: {self.publication_date}\nLiczba stron: {self.number_of_pages}\nBiblioteka: {self.library}'


class Order:
    employee: Employee
    student: Student
    books: Book
    order_date: date

    def __init__(self, employee: Employee, student: Student, books: Book, order_date: date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Dane zamówienia:\nSTUDENT\n{self.student}\nKSIĄŻKA\n{self.books}\nData zamówienia: {self.order_date}\nOSOBA OBSŁUGUJĄCA ZAMÓWIENIE\n{self.employee}'


biblio1 = Library('Katowice', 'Bogucicka 7', '41-255', '8:00-19:00', '234-765-890')
biblio2 = Library('Gliwice', 'Warszawska 27', '41-345', '8:00-19:00', '432-765-890')

prac1 = Employee("Ewa", "Elska", date(2015, 4, 20), date(1975, 2, 19), "Katowice", "1 Maja 50", "41-245", "123-456-789")
prac2 = Employee("Iza", "Igielska", date(2016, 7, 13), date(1976, 8, 11), "Katowice", "Kwiatowa 7", "41-245",
                 "789-123-098")
prac3 = Employee("Bartosz", "Baryłka", date(2015, 5, 19), date(1975, 6, 25), "Katowice", "Tulipanowa 28", "41-245",
                 "456-321-678")

student1 = Student("Adam Jędrzejczyk", 55)
student2 = Student("Paweł Rawski", 65)
student3 = Student("Krzysztof Bednarek", 60)

ks1 = Book(biblio1, date(2014, 12, 13), "Anna", "Hanna", 250)
ks2 = Book(biblio2, date(2015, 12, 14), "William", "Szekspir", 150)
ks3 = Book(biblio1, date(2010, 12, 15), "Ernest", "Hemingway", 127)
ks4 = Book(biblio2, date(2013, 12, 16), "Pan", "Lusterko", 1000)
ks5 = Book(biblio1, date(2014, 12, 17), "Julian", "Pankratz", 50)

zam1 = Order(prac2, student1, ks5, date(2021, 12, 13))
zam2 = Order(prac3, student3, ks3, date(2021, 11, 15))

print(biblio1.__str__())
print("\n")
print(prac1.__str__())


print("\n")
print(zam1)
print("\n")
print(zam2)

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
