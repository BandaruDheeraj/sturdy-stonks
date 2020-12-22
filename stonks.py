###### below line CRUCIAL when running Windows, otherwise multiprocessing doesn't work! (not necessary on Linux)
from findatapy.util import SwimPool; SwimPool()

import csv
import random
from pprint import pprint
from findatapy.market import Market, MarketDataRequest, MarketDataGenerator

def get_equity_data_example():
    market = Market(market_data_generator=MarketDataGenerator())

    md_request = MarketDataRequest(
        start_date="year",            # start date
        data_source='yahoo',            # use Bloomberg as data source
        tickers=['Apple', 'S&P500-ETF'], # ticker (findatapy)  <- not necessary
        fields=['close'],               # which fields to download
        vendor_tickers=['aapl','spy'],   # ticker (Yahoo)
        vendor_fields=['Close'])        # which Bloomberg fields to download)
    
    df = market.fetch_market(md_request)
    print(df.tail(5))
get_equity_data_example()


def get_tickers(year=2016):
    reader = csv.reader(open("nasdaq_screener_1608613054944.csv"))
    next(reader)
    stocks = [line[0].strip() for line in reader if all(punc not in line[0] for punc in ['.','/']) and (not line[7] or int(line[7]) < year)]
    return stocks

class Portfolio:
    all_tickers = get_tickers(2016)
    market = Market(market_data_generator=MarketDataGenerator())
    def __init__(self, num=5):
        self.holdings = []
        for x in range(num):
            self.pick_stock()
    def pick_stock(self):
        i = random.randint(0, len(self.all_tickers))
        ticker = self.all_tickers[i]
        if ticker in self.holdings:
            self.pick_stock()
        else:
            self.holdings.append(ticker)
    def get_equity_data(self):
        md_request = MarketDataRequest(
            start_date='1 Jan 2016',
            data_source='yahoo',
            vendor_tickers=self.holdings,
            vendor_fields=['Close']
        )

        df = self.market.fetch_market(md_request)
        return df

p = Portfolio()
print(p.holdings)
print(p.get_equity_data().tail(5))
