import requests
import json
import datetime


def pobierz_kurs(waluta="usd", termin="today"):
    try:
        wynik = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/' + waluta + '/' + termin + '/')
        wynik = json.loads(wynik.content)
        wynik = wynik['rates'][0]['mid']
        return wynik
    except:
        return 0


class Percepton:
    lista = []
    def __init__(self):
        pass

    def __str__(self,lista):
        return ("Wartosc obiektu"+str(lista))

    def last_100_days(self):
        print("Pobieram")


#poczatek = datetime.date(2022, 5, 5)
zwariowane_kursy = Percepton
zwariowane_kursy.last_100_days(zwariowane_kursy)

#print(pobierz_kurs('eur', str(poczatek)))
#print(pobierz_kurs('usd', str(poczatek)))