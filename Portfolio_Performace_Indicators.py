# Library importations
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import datetime
from linreg import lin_regr_func



def processPriceData(dfPrices,startinput,endinput):
    
    R = pd.DataFrame()
    R = dfPrices/dfPrices.shift(1) - 1 # calculate the returns
    R = R[1:] # eliminate the first row which is undefined

    # Annualisation of the mean vector and variance
    n = len(R) # calculate the number of returns observed
    d = len(R.columns) # calculate the number of stocks used
    # Calculation of the average fraction of time (expressed in years) between two observations
    Ys = int(startinput[0:4])
    Ms = int(startinput[5:7])
    Ds = int(startinput[8:10])
    Ye = int(endinput[0:4])
    Me = int(endinput[5:7])
    De = int(endinput[8:10])

    startdate = datetime.date(Ys, Ms, Ds)
    enddate = datetime.date(Ye, Me, De)
    z = enddate - startdate
    Duration = float(z.days) # calculate the number of calendar days between the two dates
    m = float(n - 1)
    delta = Duration/365/m # calculate the time interval,delta

    return R, delta #, Covar_A.to_numpy(), Mean_A.to_numpy()



class fund(object):
    """
    Class for funds
    """


    def __init__(self, fund_ticker, bench_ticker):
        """
        Attributes
        ==========
        ticker : string
            fund ticker symbol
        """
        self.ticker = fund_ticker
        self.bench_ticker = bench_ticker


    """
    Methods
    =======
    """

    def getPriceData(self, start_date, end_date):
        """
        getPriceData
            return nothing
        """
        self.start_date = start_date
        self.end_date = end_date
        # Data extraction
        S = pd.DataFrame() #create the data frame that will contain the data
        S[self.ticker] = web.DataReader(name = self.ticker, data_source = 'yahoo' ,start = self.start_date , end= self.end_date)['Close']
        self.returns, self.delta = processPriceData(S,self.start_date,self.end_date)
        
        B = pd.DataFrame() #create the data frame that will contain the data
        B[self.bench_ticker] = web.DataReader(name = self.bench_ticker, data_source = 'yahoo' ,start = self.start_date , end= self.end_date)['Close']
        self.bench_returns, self.delta = processPriceData(B,self.start_date,self.end_date)


    def portSharpe(self, rf):
        """
        portSharpe : float
            return Sharpe Ratio of a portfolio
        """
        # rf is annualized as given
        returns = self.returns
        delta = self.delta
        
        portRets_A = returns/delta # daily percentage return to annualized percentage returns
        
        return (portRets_A.mean() - rf)/portRets_A.std()/np.sqrt(delta)


    def benchSharpe(self, rf):
        """
        benchSharpe : float
            return Sharpe Ratio of a benchmark
        """
        # rf is annualized as given
        returns = self.bench_returns
        delta = self.delta
        
        benchRets_A = returns/delta # daily percentage return to annualized percentage returns
        
        return ((benchRets_A.mean() - rf)/benchRets_A.std())/np.sqrt(delta)


    def jensonIndex(self, rf):
        """
        jensonIndex : float
            return the Jensen Index of a portfolio
        """

        portRets = (self.returns / self.delta).squeeze()  # daily percentage return to annualized percentage return for portfolio
        benchRets = (self.bench_returns / self.delta).squeeze()  # daily percentage return to annualized percentage returns for benchmark

        # calculate beta
        regr = lin_regr_func(benchRets, portRets)  # Beta is calculated using the slope equation of function lin_regr_func in linreg.py file
        beta = regr[1]
        
        # Jenson index
        return (portRets.mean() - (rf + beta * (benchRets.mean() - rf)))


    def treynorIndex(self, rf):
        """
        portSharpe : float
            return the treynor index of a portfolio
        """

        portRets = (self.returns / self.delta).squeeze()  # daily percentage return to annualized percentage return for portfolio
        benchRets = (self.bench_returns / self.delta).squeeze()  # daily percentage return to annualized percentage returns for benchmark
        
        # calculate beta
        regr = lin_regr_func(benchRets, portRets)  # Beta calculated using the slope equation of function lin_regr_func in linreg.py file
        beta = regr[1]
        
        # Treynor index
        return ((portRets.mean() - rf) / beta)


    def sortinoRatio(self, rf):
        """
        sortinoRatio : float
            return the Sortino Ratio of a portfolio
        """
        portRets = (self.returns/self.delta).squeeze() # daily percentage return to annualized percentage returns
        
        # calculate semi-deviation
        avg = portRets.mean()
        a = 0 # x is the total number of observations below the mean
        b = 0 # y is the (the average - the observed value)^2
        for i in portRets:
            if i < avg:
                a += 1
                b += (avg - i)**2
        semiDeviation = np.sqrt((b/a))
        
        # Sortino Ratio
        return (portRets.mean() - rf)/semiDeviation/np.sqrt(self.delta)

    
    def ModiglianiModigliani(self, rf):
        """
        ModiglianiModigliani : float
            return the Modigliani-Modigliani Ratio of a portfolio
        """
        benchRets = (self.bench_returns / self.delta).squeeze()  # daily percentage return to annualized percentage returns for benchmark
        std = (benchRets.std()) * np.sqrt(self.delta).squeeze() # standard deviation of the return of benchmark

        # Modigliani-Modigliani Ratio
        return (rf + (std * self.portSharpe(rf)))
   

    def informationRatio(self, rf):
        """
        Information Ratio : float
            return the Information Ratio of a portfolio
        """        
        portRets = (self.returns / self.delta).squeeze()  # daily percentage return to annualized percentage return for portfolio
        benchRets = (self.bench_returns / self.delta).squeeze()  # daily percentage return to annualized percentage returns for benchmark
  
        # difference between portfolio and benchmark return
        diff = portRets - benchRets
        
        # tracking error
        te = diff.std()
        
        # Information Ratio
        return ((portRets.mean() - benchRets.mean())/ te/ np.sqrt(self.delta))
        
        

# Code Testing Purpose
if __name__ == "__main__":
    
    # Comparing Fidelity® ZERO Large Cap Index Fund with selected benchmark S&P 500
    print("Fidelity® ZERO Large Cap Index Fund VS S&P 500")
    F = fund("FNILX", "SPY")
    F.getPriceData("2018-09-30", "2020-10-31")
    # Let's assume the risk-free rate is 1% (0.01)
    rf = 0.01
    print(f"Risk free rate is {rf}")
    print(f"Portfolio's Sharpe Ratio: {F.portSharpe(rf)}")
    print(f"Benchmark's Sharpe Ratio: {F.benchSharpe(rf)}")
    print(f"Jenson Index: {F.jensonIndex(rf)}")
    print(f"Treynor Index: {F.treynorIndex(rf)}")
    print(f"Sortino Ratio: {F.sortinoRatio(rf)}")
    print(f"Modigliani-Modigliani Ratio: {F.ModiglianiModigliani(rf)}")
    print(f"Information Ratio: {F.informationRatio(rf)}")

    print("\n")    

    # Comparing Bitcoin with selected benchmark NASDAQ
    print("Bitcoin VS NASDAQ")
    F = fund("BTC-USD", "^IXIC")
    F.getPriceData("2018-09-30", "2020-10-31")
    # Let's assume the risk-free rate is 1% (0.01)
    rf = 0.01
    print(f"Risk free rate is {rf}")
    print(f"Portfolio's Sharpe Ratio: {F.portSharpe(rf)}")
    print(f"Benchmark's Sharpe Ratio: {F.benchSharpe(rf)}")
    print(f"Jenson Index: {F.jensonIndex(rf)}")
    print(f"Treynor Index: {F.treynorIndex(rf)}")
    print(f"Sortino Ratio: {F.sortinoRatio(rf)}")
    print(f"Modigliani-Modigliani Ratio: {F.ModiglianiModigliani(rf)}")
    print(f"Information Ratio: {F.informationRatio(rf)}")