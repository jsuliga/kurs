
eur = 100
usd = 100
lista_kursow = [1]
waga_a = 1.5
waga_b = 3
predkosc_liczenia = 0.001
nowy_kurs = 1


class Percepton:
    def __init__(self):
        lista_wynikow = []

    def print(self):
        pass

    wszystkie = []
    pass


class Percepton2:
    def __init__(self):
        pass
    def print(self):
        pass

#mozna iterowac po liscie klas, i dec .print
n2 = 2


Percepton.print(n2)


#mozna wykonac funkcje klasy dla elementu
#rozpisac percepton na klase ktora pobiera informacje o liczbie wejsc, ile wejsc na start
#ma utworzycz podstawowe bwagi
#teach i run
#modul random w pythonie, funkcje losowych liczb
# na zwyklych floatach


def statyczna():
    pass



def pobierz_kurs():
    while True:
        try:
            x = float(input("Podaj kurs"))
            return x
        except:
            print("Nieprawidlowy kurs")


def srednia_xdni(lista, dlugosc=5):
    suma = 0
    if len(lista) == 0:
        return 0
    if len(lista) < dlugosc:
        for x in lista:
            suma += x
    else:
        for x in lista[-dlugosc:]:
            suma += x
    return suma / len(lista)


def roznica_binarna(a, b=0):
    if a - b <= 0:
        return 0
    return 1


def licz_wage(waga, blad, predkosc=predkosc_liczenia):
    waga = waga + ostatnia_srednia * blad * predkosc
    return waga
    pass


klasa = Percepton()
del Percepton

for i in range(100):
    poprzedni_kurs = nowy_kurs
    nowy_kurs = pobierz_kurs()
    lista_kursow.append(nowy_kurs)
    ostatnia_srednia = srednia_xdni(lista_kursow)
    ostatnia_roznica = roznica_binarna(nowy_kurs, poprzedni_kurs)
    if i == 0:
        rezultat = ostatnia_srednia * waga_a + ostatnia_roznica * waga_b
        print(rezultat)
    else:
        waga_a = waga_a + ostatnia_srednia * blad * predkosc_liczenia
        waga_b = waga_b + ostatnia_roznica * blad * predkosc_liczenia
        rezultat = ostatnia_srednia * waga_a + ostatnia_roznica * waga_b
        print(rezultat)
    blad = rezultat - nowy_kurs
    print(blad)

class Percepton:
    lista = []

    def __init__(self):
        pass

    def __str__(self, lista):
        return ("Wartosc obiektu" + str(lista))

    def dodaj(self, x, y=lista):
        y = y.append(x)



class Percepton:
    lista = []

    def __init__(self):
        pass

    def __str__(self, x=lista):
        print("Wartosc obiektu" + str(x))

    def dodaj(self, x, y=lista):
        y = y.append(x)