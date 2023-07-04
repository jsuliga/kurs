import requests
import json
import datetime
import time


def pobierz_kurs(waluta="usd", termin="today"):
    try:
        wynik = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/' + waluta + '/' + termin + '/')
        wynik = json.loads(wynik.content)
        wynik = wynik['rates'][0]['mid']
        return wynik
    except:
        return 0


def lista_dat(poczatek="2023-01-01", koniec="2023-06-06", format='%Y-%m-%d'):
    a = datetime.datetime.strptime(poczatek, format)
    b = datetime.datetime.strptime(koniec, format)
    if (b - a).days > 0:
        lista = []
        while a.date() != b.date():
            if a.weekday() > 4:
                a += datetime.timedelta(1)
            else:
                lista.append(a.date().__str__())
                a += datetime.timedelta(1)
        return lista
    else:
        return []


def roznica_binarna(x, y=0):
    if x - y <= 0:
        return 0
    return 1


def srednia_xdni(x, y=5):
    suma = 0
    if len(x) == 0:
        return 0
    if len(x) < y:
        for x in x:
            suma += x
    else:
        for x in x[-y:]:
            suma += x
    return suma / len(x)


wynik = {}
# start = input("Podaj poczatkowa date")
start = "2023-01-01"
# koniec = input("Podaj koncowa date")
koniec = "2023-01-30"
xxx = lista_dat(start, koniec)
for data in xxx:
    a = pobierz_kurs('usd', data)
    b = pobierz_kurs('eur', data)
    try:
        c = b / a
    except:
        pass
    wynik[data] = {'usd': a, 'eur': b, 'kurs': c}
    time.sleep(0.1)
for aaaa in wynik:
    print(aaaa.__str__())
#print(json.dumps(wynik, indent=4))
# print(pobierz_kurs('eur', str(poczatek)))
# print(pobierz_kurs('usd', str(poczatek)))
