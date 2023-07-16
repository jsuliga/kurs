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
    def __init__(self, ilosc_wag=2, y=0.01):
        self.lista_wag = []
        self.predkosc_uczenia = y
        self.ilos_wag = ilosc_wag
        self.blad = 0
        for i in range(0, ilosc_wag):
            self.lista_wag.append(random.random())

    def __str__(self):
        return str(self.lista_wag)

    def teach(self, *argv):
        lista = list(argv)
        rezultat = lista.pop()
        self.blad = rezultat - self.run(*lista)
        for i in range(0, len(self.lista_wag)):
            self.lista_wag[i] = self.lista_wag[i] + argv[i] * self.predkosc_uczenia * self.blad
        print("Blad: " + str(self.blad))
        print("Lista: " + str(self.lista_wag))

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

    def load_file(self, file_name="kursy"):
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
    def __init__(self):
        self.percepton_temp = Percepton()
        self.percepton_list = []
        self.wyniki_lista = []
        for learning_speed_iteration in range(-10, 10):
            temp_learning_speed=10**learning_speed_iteration
            self.percepton_list.append(Percepton(y=temp_learning_speed))


    def __str__(self):
        str_temp = "One percepton: " + str(self.percepton_temp) +"\n"
        for element in self.percepton_list:
            str_temp +="Array of percepton: " + str(element) +"\n"
        return str(str_temp)

    def __print_list(self, print_list):
        for element in print_list:
            print(element)


    def add_percepton(self, perc):
        self.percepton_temp = perc

    def reset_percepton(self):
        self.percepton_temp = Percepton()

    def teach_one(self, input_one):
        pass

    def find_best(self, *args):
        tem_array = Inputs()
        tem_array.load_file()
        aaaaaaaa = tem_array.all_elements()
        for element in self.percepton_list:
            for asd in aaaaaaaa:
                element.teach(asd)







take_inputs = Inputs()
take_inputs.load_file(learning_test_file)
teaching = Teacher()
teaching.find_best(1)


