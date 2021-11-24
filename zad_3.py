# 3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
# parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
# uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
# wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
# "Liczba nieparzysta"
print("Zad. 3")
def sprawdzenie(liczba: int) -> bool:
    if (liczba % 2 == 0):
        return True
    else:
        return False

    #if (liczba%2==0):
    #    print("true")
    #else:
    #    print("false")

zmienna = sprawdzenie(3)
print(zmienna)

if zmienna==True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
