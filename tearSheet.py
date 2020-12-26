import numpy as np
import pandas as pd
from empyrical import max_drawdown, alpha_beta, sharpe_ratio
import warnings
warnings.filterwarnings('ignore')

bestDrawdown = 0
bestSharpe = 0
lowestDrawdown = float('inf') * -1
highestSharpeRatio = float('inf') * -1


for i in range(1,100):
    returnsName = "portfolio"+str(i)+"DailyPercentChange.pkl"
    returns = pd.read_pickle(returnsName)

    drawDown = max_drawdown(returns).mean()
    sharpe = sharpe_ratio(returns).mean() # risk free = 0, period = daily
    # calculate the max drawdown
    if  drawDown > lowestDrawdown:
        bestDrawdown = i
        lowestDrawdown = drawDown

    # calculate the sharpe ratio 
    if sharpe > highestSharpeRatio:
        bestSharpe = i
        highestSharpeRatio = sharpe
    



print(lowestDrawdown)
print(bestDrawdown)

print(highestSharpeRatio)
print(bestSharpe)



bestPortHoldings = "portfolio"+str(bestDrawdown)+"DailyPercentChange.pkl"
bestPortHoldings = pd.read_pickle(bestPortHoldings)
print(bestPortHoldings)



# calculate alpha and beta
# alpha, beta = alpha_beta(returns, benchmark_returns)