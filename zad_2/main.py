import classes.Student as Stud
import classes.Library as Lb2
import classes.Employee as Emp2
import classes.Book as Bk2
import classes.Order as Ord2
import classes.House as Ho2
import classes.Flat as Ft2
from datetime import date

# 1.
print("Zad.1")


s1 = Stud.Student('Adam N', 55)
s2 = Stud.Student('Andrzej N', 45)

# s1.powitanie()
print(s1.powitanie)
print(s1.is_passed)

# s2.powitanie()
print(s2.powitanie)
print(s2.is_passed)

# 2.
print("Zad.2")

biblio1 = Lb2.Library('Katowice', 'Bogucicka 7', '41-255', '8:00-19:00', '234-765-890')
biblio2 = Lb2.Library('Gliwice', 'Warszawska 27', '41-345', '8:00-19:00', '432-765-890')

prac1 = Emp2.Employee("Ewa", "Elska", date(2015, 4, 20), date(1975, 2, 19), "Kato", "1 Maja 5", "41-245", "123-456-789")
prac2 = Emp2.Employee("Iza", "Iga", date(2016, 7, 13), date(1976, 8, 11), "Kato", "Kwita 7", "41-245", "789-123-098")
prac3 = Emp2.Employee("Olo", "Bąk", date(2015, 5, 19), date(1975, 6, 25), "Kato", "Tulip 28", "41-245", "456-321-678")

student1 = Stud.Student("Adam Jędrzejczyk", 55)
student2 = Stud.Student("Paweł Rawski", 65)
student3 = Stud.Student("Krzysztof Bednarek", 60)

ks1 = Bk2.Book(biblio1, date(2014, 12, 13), "Anna", "Hanna", 250)
ks2 = Bk2.Book(biblio2, date(2015, 12, 14), "William", "Szekspir", 150)
ks3 = Bk2.Book(biblio1, date(2010, 12, 15), "Ernest", "Hemingway", 127)
ks4 = Bk2.Book(biblio2, date(2013, 12, 16), "Pan", "Lusterko", 1000)
ks5 = Bk2.Book(biblio1, date(2014, 12, 17), "Julian", "Pankratz", 50)

zam1 = Ord2.Order(prac2, student1, ks5, date(2021, 12, 13))
zam2 = Ord2.Order(prac3, student3, ks3, date(2021, 11, 15))

print(biblio1.__str__())
print("\n")
print(prac1.__str__())

print("\n")
print(zam1)
print("\n")
print(zam2)

# 3.
print("Zad.3")


x = Ho2.House("wieś", 7, "500000 zł", "ul. Kwiatowa 3, 42-432 Gliwice", 1000)
y = Ft2.Flat("wieś", 7, "500000 zł", "ul. Kwiatowa 3, 42-432 Gliwice", 4)

print(x)
print(y)
