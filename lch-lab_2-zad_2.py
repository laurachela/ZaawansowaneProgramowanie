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


wyswietl_imiona(names=['name1', 'name2', 'name3', 'name4', 'name5'])

# b) Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych
# liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci.
# Zadanie należy wykonać w 2 wersjach:
# i)


def liczbyx2(tab_numbers: list) -> list:
    lista = []
    for i_number in tab_numbers:
        lista.append(i_number*2)
    return lista


print(liczbyx2(tab_numbers=[1, 2, 3, 4, 5]))

# ii)


def liczbyx2next(tab2_numbers: list) -> list:
    return [i2number*2 for i2number in tab2_numbers]


print(liczbyx2next(tab2_numbers=[1, 2, 3, 4, 5]))


# c) Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane
# wykorzystanie funkcji range ), która wyświetla jedynie parzyste elementy.

numbers2 = range(1, 10)
for x in numbers2:
    if x % 2 == 0:
        print(x)

# d) Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane
# wykorzystanie funkcji range ), która wyświetla co drugi element.

numbers3 = range(1, 10)
for i, y in enumerate(numbers3):
    if i % 2 == 0:
        print(y)
