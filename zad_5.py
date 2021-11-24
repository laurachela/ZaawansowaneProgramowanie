# 5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int.
# Funkcja ma sprawdzić, czy lista z parametru pierwszego zawiera taką wartość
# jaką przekazano w parametrze drugim.
print("Zad. 5")
def dwaarg(x: list, y: int) -> bool:
    if y in x:
        print(f"Lista zawiera wartość przekazaną w drugim argumencie, czyli {y}")
    else:
        print(f"Nie istnieje w liście podana wartość, czyli {y}")

listaA=[1,2,3,4,5]
dwaarg(listaA, 5)
