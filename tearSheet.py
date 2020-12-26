import numpy as np
import pandas as pd
from empyrical import max_drawdown, alpha_beta, sharpe_ratio, tail_ratio, omega_ratio
import warnings
warnings.filterwarnings('ignore')

bestDrawdown = 0
bestSharpe = 0
lowestDrawdown = float('inf') * -1
highestSharpeRatio = float('inf') * -1
bestTail = 0
highestTailRatio = float('inf')
bestOmega = 0
highestOmegaRatio = float('inf') * -1

for i in range(1,100):
    returnsName = "portfolio"+str(i)+"DailyPercentChange.pkl"
    returns = pd.read_pickle(returnsName)
    returns = returns[1:]
    returns = returns.fillna(0.0)

    drawDown = max_drawdown(returns).mean()
    sharpe = sharpe_ratio(returns).mean() # risk free = 0, period = daily
    tail = tail_ratio(returns).mean()
    # omega = omega_ratio(returns)
    # calculate the max drawdown
    if  drawDown > lowestDrawdown:
        bestDrawdown = i
        lowestDrawdown = drawDown

    # calculate the sharpe ratio 
    if sharpe > highestSharpeRatio:
        bestSharpe = i
        highestSharpeRatio = sharpe

    # calculate the tail ratio 
    if tail < highestTailRatio:
        bestTail = i
        highestTailRatio = tail

    # calculate the omega ratio, required return 100
    # if omega > highestOmegaRatio:
    #     bestOmega = i
    #     highestOmegaRatio = omega
    



print(lowestDrawdown)
print(bestDrawdown)

print(highestSharpeRatio)
print(bestSharpe)

print(highestTailRatio)
print(bestTail)

print(highestOmegaRatio)
print(bestOmega)



bestPortHoldings = "portfolio"+str(bestSharpe)+"DailyPercentChange.pkl"
bestPortHoldings = pd.read_pickle(bestPortHoldings)
print(bestPortHoldings)


#need benchmark for alpha beta calculations
