#http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
#http://api.nbp.pl/api/exchangerates/rates/a/usd/{date}/
import requests

x = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/usd/')
print(x.status_code)
