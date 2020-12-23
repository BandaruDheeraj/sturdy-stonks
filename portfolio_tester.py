from stonks import Portfolio
import pandas as pd

portfolios = [Portfolio() for x in range(100)]

df = pd.DataFrame([p.holdings for p in portfolios])
print(df)