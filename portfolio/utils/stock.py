import requests

def get(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=1min&apikey=KMVGVC8ECNLDJQVE'
    responseJsonObj = requests.get(url).json()
    timeSeriesSorted = sorted(responseJsonObj['Time Series (1min)'], reverse=True)
    lastPrice = responseJsonObj['Time Series (1min)'][timeSeriesSorted[0]]['4. close']
    return {'last_price': lastPrice}


    





