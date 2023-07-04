import random

eur = 100
usd = 100
lista_kursow = []
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


class Percepton:
    def __init__(self, x, y=0.01):
        self.lista_wag = []
        self.predkosc_uczenia = y
        self.ilos_wag = x
        self.blad = 0
        for i in range(0, x):
            self.lista_wag.append(random.random())

    def teach(self, *argv):
        lista = list(argv)
        rezultat = lista.pop()
        self.blad = rezultat - self.run(*lista)
        for i in range(0, len(self.lista_wag)):
            self.lista_wag[i] = self.lista_wag[i] + argv[i] * self.predkosc_uczenia * self.blad
        print("blad" + str(self.blad))
        print("lista" + str(self.lista_wag))

    def run(self, *argv):
        suma = 0
        for i in range(0, len(argv)):
            suma += self.lista_wag[i] * argv[i]
        return suma


cholera = Percepton(2, 0.1)
cholera.lista_wag = [0.9907506605180431, 0.9989830121037068]
for i in range(100):
    poprzedni_kurs = nowy_kurs
    nowy_kurs = pobierz_kurs()
    lista_kursow.append(nowy_kurs)
    #ostatnia_roznica = roznica_binarna(nowy_kurs, poprzedni_kurs)
    ostatnia_roznica = nowy_kurs - poprzedni_kurs
    ostatnia_srednia = srednia_xdni(lista_kursow)
    print("Różnica        : ", str(ostatnia_roznica))
    print("Średnia 5 dni  : ", str(ostatnia_srednia))
    if i == 0:
        cholera.teach(ostatnia_roznica, ostatnia_srednia, nowy_kurs)
    else:
        przewidziany = cholera.run(ostatnia_roznica, ostatnia_srednia)
        cholera.teach(ostatnia_roznica, ostatnia_srednia, nowy_kurs)
print(cholera.blad)
print(cholera.lista_wag)
