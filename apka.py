wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)

#TODO:
# specjalne ceny dla osob +40
# przemyslenie klas rownowaznosci
#KR 1 <=0
#KR 2 1-18
#KR 3 18-99
#Tutaj obsługa kraju
pelnoletni = (wiek >= 18 and wiek <40)
pozaZakresem = (wiek <=0 or wiek>99)
ponad40 = (wiek>=40 and wiek<=99)

if pozaZakresem:
    exit(f"Podany wiek {wiek} nie mieście się w zakresie 1-99")
elif pelnoletni:
    print("Witamy!")
elif ponad40: #specjalne ceny dla osob +40
    print("Witamy dla osóbg 40+ mamy specjalne ceny")
else:
    exit("Zakaz wstępu!")