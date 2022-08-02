import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=9HNF6BVRY1CVJKPX'
r = requests.get(url)
apidata = r.json()

all = apidata['Realtime Currency Exchange Rate']['5. Exchange Rate']
def convert(USD):
    SGD = int(USD) * all 
    return SGD