def pocet_suborov():
    while True:
        pocet = input("Kolko suborov chcete: ")
        try:
            return abs(int(pocet))
        except ValueError:
            print("Nezadali ste cislo")


a = []
retaz_slov = 0

with open("basnicka.txt", encoding="utf-8") as subor:
    for slovo in subor:
        a += slovo.split()

for i in range(pocet_suborov()):
    retaz_slov += 1
    if retaz_slov == len(a):
        retaz_slov -= len(a)
    with open(f"""slovo{i}""", mode="w", encoding="utf-8") as subor:
        print(a[retaz_slov - 1], file=subor)