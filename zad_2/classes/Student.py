class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Dane studenta:\nImię i nazwisko: {self.name}'

    @property
    def is_passed(self):
        if self.marks > 50:
            return True
        else:
            return False

    @property
    def powitanie(self):
        print(f"Hi, {self.name}. Wynik twoich ocen to {self.marks}")
