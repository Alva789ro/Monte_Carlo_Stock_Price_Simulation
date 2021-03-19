import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm


data=pd.DataFrame()
data['MSFT']= web.DataReader('MSFT', data_source='yahoo', start='2019-10-3')['Close']
real_data=data['MSFT'].values #gets all the original price changes of the security
#print(len(data['MSFT']))


def get_simulation(ticker, name):
    data=pd.DataFrame()
    data[ticker]= web.DataReader(ticker, data_source='yahoo', start='2019-10-3')['Close']
    log_returns = np.log(1+data.pct_change())
    mean = log_returns.mean()
    var = log_returns.var()
    drift = mean - (0.5 * var)
    stdev = log_returns.std()
<<<<<<< HEAD
    t_intervals = 368 #adjust this value depending on the length of values the code from the "web.DataReader" is able to collect, it varies with the date
    iterations = 10 #this will determine the number of simlations we are going to run. Can be more than 10
=======
    t_intervals = 362 #adjust this value depending on the length of values the code from the "web.DataReader" is able to collect, it varies with the date
    iterations = 10 #determines the number of simlations we are going to create. Can be adjusted
>>>>>>> 1c9f57ad63f70d76458d9812fd07bd16a31587f1
    daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
    s0 = data.iloc[-1]
    price_list = np.zeros_like(daily_returns)
    price_list[0] = s0
    for t in range(1, t_intervals): #creates the lists that contain the simlations created
        price_list[t] = price_list[t-1] * daily_returns[t]
<<<<<<< HEAD
    #plot the simulation
=======
    #plotting the scenarios
>>>>>>> 1c9f57ad63f70d76458d9812fd07bd16a31587f1
    plt.figure(figsize = (10,6))
    plt.title("1 Year Monte Carlo Similation for " + name)
    plt.ylabel("Price (P)")
    plt.xlabel("Time (Days)")
    plt.plot(price_list)
    plt.plot(real_data, color='red', label= "Real Price Change")
    plt.legend(loc='upper left')
    plt.savefig("MT_simulation.png")
    plt.show()



get_simulation("MSFT", "Microsoft Inc") #This can be used to change the name of the security we want to look for.
