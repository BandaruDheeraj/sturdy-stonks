from stonks import Portfolio
import pandas as pd

portfolios = [Portfolio() for x in range(100)]

df = pd.DataFrame([p.holdings for p in portfolios])
df.to_pickle("test.pkl")

numPort = 1

for p in portfolios:
    returnsName = "portfolio"+str(numPort)+"Returns.pkl"
    dailyReturns = p.get_equity_data()
    dailyReturns.to_pickle(returnsName)
    numPort += 1

