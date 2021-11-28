# 1. Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
# następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
# uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
# wyświetlić ( print )
print("Zad. 1")

def funkcja1(name: str, surname: str):
    print(f"Cześć {name} {surname}!")

funkcja1("Laura","Chela")

print("\n")
# 2. Stworzyć funkcję, która przyjmie 2 argumenty typu int , a następnie zwróci wynik
# mnożenia obu liczb.
print("Zad. 2")

def mnozenieobu(x: int, y: int):
    wynik = x*y
    print(f"Wynik mnożenia liczb {x} i {y} wynosi: {wynik}")

mnozenieobu(2,6)

print("\n")
# 3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
# parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
# uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
# wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
# "Liczba nieparzysta"
print("Zad. 3")

def sprawdzenie(liczba: int) -> bool:
    if liczba % 2 == 0:
        return True
    else:
        return False

    #if (liczba%2==0):
    #    print("true")
    #else:
    #    print("false")

zmienna = sprawdzenie(3)
print(zmienna)

if zmienna is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

print("\n")
# 4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
# pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
# jako typ logiczny bool
print("Zad. 4")

def trzyarg(x: int, y: int, z: int) -> bool:
    if x+y >= z:
        return True
    else:
        return False

print(trzyarg(2,3,6))

print("\n")
# 5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int.
# Funkcja ma sprawdzić, czy lista z parametru pierwszego zawiera taką wartość
# jaką przekazano w parametrze drugim.
print("Zad. 5")

def dwaarg(x: list, y: int) -> bool:
    if y in x:
        return True # f"Lista zawiera wartość przekazaną w drugim argumencie, czyli {y}"
    else:
        return False # f"Nie istnieje w liście podana wartość, czyli {y}"

listaA=[1,2,3,4,5]
print(dwaarg(listaA, 5))

print("\n")
# 6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
# Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
# element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.
print("Zad. 6")

def dwielisty(a: list, b: list) -> list:
    listaab = a + b
    listaab = set(listaab)
    print(listaab)
    # print([x ** 3 for x in listaab])
    return [x ** 3 for x in listaab]

la=[1,2,3]
lb=[3,4,5]
#dwielisty(la,lb)
print(dwielisty(la,lb))
