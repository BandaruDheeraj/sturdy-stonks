import numpy as np
import pandas as pd
from empyrical import max_drawdown, alpha_beta
import warnings
warnings.filterwarnings('ignore')

bestPortfolio = 0
lowestDrawdown = float('inf') * -1

for i in range(1,100):
    returnsName = "portfolio"+str(i)+"DailyPercentChange.pkl"
    returns = pd.read_pickle(returnsName)

    # calculate the max drawdown
    if max_drawdown(returns).mean() > lowestDrawdown:
        bestPortfolio = i
        lowestDrawdown = max_drawdown(returns).mean() 

print(lowestDrawdown)
print(bestPortfolio)

bestPortHoldings = "portfolio"+str(bestPortfolio)+"DailyPercentChange.pkl"
bestPortHoldings = pd.read_pickle(bestPortHoldings)
print(bestPortHoldings)

# calculate alpha and beta
# alpha, beta = alpha_beta(returns, benchmark_returns)