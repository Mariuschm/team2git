def NrStrefy():
  strefa = input("podaj region: (EUR , USA, Other: ")
  if strefa != "EUR" and strefa != "USA":
    strefa = ""
  return strefa

wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
  exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:

    print("Witamy!")


def plec(x):
    if x == 1:
        print("Aperol gratis")
    else:
        print("Pij i płać")


x = int(input("Podaj płeć: kobieta(1), mężczyzna(2), inne(3) "))

plec(x)



region = NrStrefy()


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

def pelnoletni(wiek,region):
    if wiek>0 and wiek<=120:
        if region=="USA" and wiek >= 21 or region=="EUR" and wiek>=18:
             print("Witamy!")

        else:
            print("Jesteś niepełnoletni")

    else:
        print("Podałeś nieprawidłową wartość, wiek musi być z przedziału 1-120")


