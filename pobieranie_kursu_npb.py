# http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/{date}/
import requests
import datetime
import json
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


# start = input("Podaj poczatkowa date")
start = "2023-01-01"
# koniec = input("Podaj koncowa date")
koniec = "2023-06-30"
xxx = lista_dat(start, koniec)
plik = open("kursy", "w")
for data in xxx:
    a = pobierz_kurs('usd', data)
    b = pobierz_kurs('eur', data)
    try:
        c = b / a
        plik.write(str(c) + '\n')
    except:
        pass
    time.sleep(0.1)
