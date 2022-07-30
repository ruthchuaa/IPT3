import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=9HNF6BVRY1CVJKPX'
r = requests.get(url)
data = r.json()

print(data)