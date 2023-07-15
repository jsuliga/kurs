import random

eur = 100
usd = 100
lista_kursow = []
nowy_kurs = 1
how_many_runs = 5
learning_test_file = "kursy"


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


class Inputs:
    def __init__(self):
        self.input_list = []
        self.input_list_working = []

    def __str__(self):
        print(str(self.input_list))
        print(str(self.input_list_working))
        return "ok"

    def load_file(self, file_name):
        file = open(file_name, "r")
        self.input_list = []
        for line in file:
            self.input_list.append(line.strip())
        self.input_list_working = self.input_list

    def next_element(self):
        try:
            next_element_temp = self.input_list_working.pop(0)
        except:
            while True:
                try:
                    next_element_temp = float(input("Lista pusta, podaj kurs: "))
                    return next_element_temp
                except:
                    print("Nieprawidlowy kurs")
        return next_element_temp

    def all_elements(self):
        return self.input_list

class Teacher:
    def __str__(self):
        self.percepton_temp = Percepton


take_inputs = Inputs()
take_inputs.load_file(learning_test_file)
print(take_inputs.all_elements())
teaching = Teacher
first_percepton = Percepton(2, 0.1)
first_percepton.lista_wag = [0.9907506605180431, 0.9989830121037068]
for i in range(how_many_runs):
    poprzedni_kurs = nowy_kurs
    nowy_kurs = pobierz_kurs()
    lista_kursow.append(nowy_kurs)
    # ostatnia_roznica = roznica_binarna(nowy_kurs, poprzedni_kurs)
    ostatnia_roznica = nowy_kurs - poprzedni_kurs
    ostatnia_srednia = srednia_xdni(lista_kursow)
    print("Różnica        : ", str(ostatnia_roznica))
    print("Średnia 5 dni  : ", str(ostatnia_srednia))
    if i == 0:
        first_percepton.teach(ostatnia_roznica, ostatnia_srednia, nowy_kurs)
    else:
        przewidziany = first_percepton.run(ostatnia_roznica, ostatnia_srednia)
        first_percepton.teach(ostatnia_roznica, ostatnia_srednia, nowy_kurs)
print(first_percepton.blad)
print(first_percepton.lista_wag)
