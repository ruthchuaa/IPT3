import requests
#import requests to call  API URL
# Assign API URL as an object called URL
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=9HNF6BVRY1CVJKPX'

#Access data from API using get method
r = requests.get(url)

#Retrieve and store data from .json as dictionary using .json()
# and assign it to variable apidata
apidata = r.json()

# Access Real time currency exchange rate dictionary in apidata dictionary 
# and access Currency exchange rate key from there
all = apidata['Realtime Currency Exchange Rate']['5. Exchange Rate']


def convert(USD):
    '''
    - Required parameter : amount you want to convert in USD to SGD
    - Converts USD to SGD
    '''

    try: 
        SGD = float(USD) * float(all)
        return SGD
    except Exception as e:
        return 'Error'
