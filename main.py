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
