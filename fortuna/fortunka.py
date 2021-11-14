jano = [1,6,5,8]
Tomas = [2,8,9]
Peter = [7,9,8,12]
Ja = input("Kolko golov:")

Ja_list = list (map(int,Ja.split()))
a = []
vstup = ""
with open("vysledky_zapasov.txt", encoding="utf-8") as subor:
    for slovo in subor:
        a = slovo
        numbers = []
        for item in a:
            for subitem in item.split():
                if subitem.isdigit():
                    numbers.append(subitem)
abc = [int(g) for g in numbers]
for i in range(1, len(abc)):
    if i % 2 == 0:
        pass
    else:
        zapas = abc[i-1] + abc[i]
        zapas = str(zapas)
        vstup = vstup + zapas + " "

vstup1 = list(map(int,vstup.split()))

pocetJ = set(vstup1)&set(jano)
tipJ = " ".join(map(str,pocetJ))
kolkoTipJ = len(pocetJ)

pocetT = set(vstup1)&set(Tomas)
tipT = " ".join(map(str,pocetT))
kolkoTipT= len(pocetT)

pocetP = set(vstup1)&set(Peter)
tipP = " ".join(map(str,pocetP))
kolkoTipP = len(pocetP)

pocetJA = set(vstup1)&set(Ja_list)
tipJA = " ".join(map(str,pocetJA))
kolkoTipJA = len(pocetJA)

print('Vysledky zapasov:', a)
print('V zapasoch bolo strelenych golov:' , vstup )
print('Jano trafil:', tipJ)
print('Tomas trafil:', tipT)
print('Peter trafil:', tipP)
print('Ja som trafil:', tipJA)

if kolkoTipJ > kolkoTipT and kolkoTipJ > kolkoTipP and kolkoTipJ > kolkoTipJA:
    print('Jano je vitaz trafil:', kolkoTipJ)
elif kolkoTipT > kolkoTipJ and kolkoTipT > kolkoTipP and kolkoTipT > kolkoTipJA:
    print('Tomas je vitaz trafil:', kolkoTipT)
elif kolkoTipP > kolkoTipJ and kolkoTipP > kolkoTipT and kolkoTipP > kolkoTipJA:
    print('Peter je vitaz trafil:', kolkoTipP)
elif kolkoTipJA > kolkoTipJ and kolkoTipJA > kolkoTipP and kolkoTipJA > kolkoTipT:
    print(' Ja som vitaz trafil som:', kolkoTipJA)
elif kolkoTipJ == kolkoTipT and kolkoTipJ > kolkoTipP and kolkoTipJ > kolkoTipJA:
    print('Jano a Tomas tipli rovnako', kolkoTipJ)
elif kolkoTipJ == kolkoTipT and kolkoTipJ == kolkoTipP and kolkoTipJ > kolkoTipJA:
    print('Jano a Tomas a Peter tipli rovnako', kolkoTipJ)
elif kolkoTipJ == kolkoTipT and kolkoTipJ == kolkoTipP and kolkoTipJ == kolkoTipJA:
    print('vsetci tipli rovnako', kolkoTipJ)
elif kolkoTipJ > kolkoTipT and kolkoTipJ == kolkoTipP and kolkoTipJ > kolkoTipJA:
    print('Jano a Peter tipli rovnako', kolkoTipJ)
elif kolkoTipJ > kolkoTipT and kolkoTipJ == kolkoTipP and kolkoTipJ == kolkoTipJA:
    print('Jano, Peter a Ja sme tipli rovnako', kolkoTipJ)
elif kolkoTipT == kolkoTipP and kolkoTipT > kolkoTipJ and kolkoTipT > kolkoTipJA:
    print('Tomas a Peter tipli rovnako', kolkoTipT)
elif kolkoTipP == kolkoTipJA and kolkoTipP > kolkoTipJ and kolkoTipP > kolkoTipT:
    print('Peter a ja sme tipli rovnako', kolkoTipP)
elif kolkoTipJ == kolkoTipJA and kolkoTipJ > kolkoTipP and kolkoTipJ > kolkoTipT:
    print('Jano a ja sme tipli rovnako', kolkoTipJ)
elif kolkoTipT == kolkoTipJA and kolkoTipT > kolkoTipP and kolkoTipT > kolkoTipJ:
    print('Tomas a ja sme tipli rovnako', kolkoTipT)
elif kolkoTipJ == kolkoTipJA and kolkoTipJ == kolkoTipT and kolkoTipJ > kolkoTipP:
    print('Jano, Tomas a ja sme tipli rovnako', kolkoTipJ)
elif kolkoTipT == kolkoTipJA and kolkoTipT == kolkoTipP and kolkoTipT > kolkoTipJ:
    print('Tomas, Peter a ja sme tipli rovnako', kolkoTipT)
else:
    print('Nikto netipol nic')