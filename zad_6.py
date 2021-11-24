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
