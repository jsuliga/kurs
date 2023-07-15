import requests
import datetime
import json
import time


class ExchangeRateNpb:
    def __init__(self):
        self.rate_dic = {}
        self.current_rate = float
        pass

    def get_by_date(self, waluta="usd", termin="today"):
        try:
            wynik = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/' + waluta + '/' + termin + '/')
            wynik = json.loads(wynik.content)
            wynik = wynik['rates'][0]['mid']
            return wynik
        except:
            return 0
        pass

    def get_range(self, date_start, date_end):
        pass

    def file_save(self, file_name):
        pass

    def download(self):
        pass

    def return_list(self):
        pass


def pobierz_kurs(waluta="usd", termin="today"):
    try:
        wynik = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/' + waluta + '/' + termin + '/')
        wynik = json.loads(wynik.content)
        wynik = wynik['rates'][0]['mid']
        return wynik
    except:
        return 0


def lista_dat(x="2022-01-01", y="2022-06-06", z='%Y-%m-%d'):
    a = datetime.datetime.strptime(x, z)
    b = datetime.datetime.strptime(y, z)
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


0# start = input("Podaj poczatkowa date")
#start = "2023-01-01"
# koniec = input("Podaj koncowa date")
#koniec = "2023-06-30"
#xxx = lista_dat(start, koniec)
#plik = open("kursy", "w")
#for data in xxx:
#    a = pobierz_kurs('usd', data)
#    b = pobierz_kurs('eur', data)
#    try:
#        c = b / a
#        plik.write(str(c) + '\n')
#    except:
#        pass
#    time.sleep(0.1)
