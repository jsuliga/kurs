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

def lista_kursow(lista = lista_dat()):


wynik = {}
start = input("Podaj poczatkowa date")
koniec = input("Podaj koncowa date")
x = lista_dat(start, koniec)
for data in x:
    a = pobierz_kurs('usd', data)
    b = pobierz_kurs('eur', data)
    c = a / b
    wynik[data] = {'usd': a, 'eur': b, 'pln': c}
    print(str(wynik))
    print(pobierz_kurs('usd', data))
    time.sleep(0.1)
# print(pobierz_kurs('eur', str(poczatek)))
# print(pobierz_kurs('usd', str(poczatek)))
