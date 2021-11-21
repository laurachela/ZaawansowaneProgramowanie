"""
Laura Chela
Grupa laboratoryjna 1
lab_2
Zad. 2

"""
# a) Utwórz funkcje, która otrzyma w parametrze listę 5 imion, a nastepnie wyświetl każde z nich.

def wyswietl_imiona(names: list) -> None:
    for name in names:
        print(name)

wyswietl_imiona(names = ['name1', 'name2' ,'name3' ,'name4' ,'name5'])

# b) Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych
# liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci.
# Zadanie należy wykonać w 2 wersjach:
# i)

def liczbyx2(numbers: list) -> list:
    lista = []
    for number in numbers:
        lista.append(number*2)
    return lista

print(liczbyx2(numbers = [1, 2, 3, 4, 5]))

# ii)

def liczbyx2next(numbers: list) -> list:
    return [number*2 for number in numbers]

print(liczbyx2next(numbers = [1, 2, 3, 4, 5]))


# c) Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane
# wykorzystanie funkcji range ), która wyświetla jedynie parzyste elementy.

numbers = range(1,10)
for number in numbers:
    if number%2==0:
        print(number)

#d) Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane
# wykorzystanie funkcji range ), która wyświetla co drugi element.

numbers = range(1,10)
for i, number in enumerate(numbers):
    if i%2==0:
       print(number)