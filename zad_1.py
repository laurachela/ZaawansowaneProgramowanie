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
