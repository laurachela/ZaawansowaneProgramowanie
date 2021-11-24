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
