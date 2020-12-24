import pandas as pd
from stonks import Portfolio

def get_returns_data(df):
    returns_df = pd.DataFrame()
    for ticker, values in df.iteritems():
        ticker = ticker.split(".")[0]
        v_f = values
        v_i = values.shift(periods=1)
        returns_df[f'{ticker}.returns'] = (v_f - v_i) / v_i
    return returns_df

# df = pd.read_pickle("portfolioReturns/portfolio1Returns.pkl")
# that breaks my computer so imma just use a random one for now
df = Portfolio().get_equity_data()
print(df, "\n", get_returns_data(df))

# also implemented within Portfolio class
p = Portfolio()
print(p.get_equity_data(), "\n", p.get_returns_data())
