from datetime import date


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
