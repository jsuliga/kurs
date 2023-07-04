eur = 100
usd = 100
lista_kursow = []
waga_a = 1.5
waga_b = 3
predkosc_liczenia = 0.001
nowy_kurs = 1


def pobierz_kurs():
    while True:
        try:
            x = float(input("Podaj kurs: "))
            return float(x)
        except:
            print("Nieprawidlowy kurs")


def roznica_binarna(x=[], y=0):
    if x - y <= 0:
        return 0
    return 1


def srednia_xdni(x, y=5):
    suma = 0
    if len(x) == 0:
        return 0
    if len(x) < y:
        for z in x:
            suma += z
        return suma / len(x)
    else:
        for z in x[-y:]:
            suma += z
    return suma / y


def licz_wage(waga, blad, predkosc=predkosc_liczenia):
    waga = waga + ostatnia_srednia * blad * predkosc
    return waga
    pass


class Percepton:
    wagi_poczatkowe=[]
    def __init__(self):
        pass

cholera = Percepton
for i in range(100):
    poprzedni_kurs = nowy_kurs
    nowy_kurs = pobierz_kurs()
    lista_kursow.append(nowy_kurs)
    print(type(lista_kursow))
    print(lista_kursow)
    print("Różnica binarna: ", str(roznica_binarna(nowy_kurs, poprzedni_kurs)))
    print("Średnia 5 dni  : ", str(srednia_xdni(lista_kursow)))
    print(cholera.wagi_poczatkowe)