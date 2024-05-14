import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import getFamaFrenchFactors as gff
import multiprocessing
import matplotlib.pyplot as plt
import datetime as dt


##ALLOW USER INPUT##
ticker = 'TSLA'
#trainging data#
start_train = '2011-01-01'
end_train =dt.datetime.now() 



#testing data
test_start = '2017-01-01'
test_end= '2018-01-01'


stock_data = yf.download(ticker, start_train, end_train)
#
test_data=yf.download(ticker, test_start, test_end)


ff3_monthly = gff.famaFrench3Factor(frequency='m')
ff3_monthly.rename(columns={"date_ff_factors": 'Date'}, inplace=True)
ff3_monthly.set_index('Date', inplace=True)

#
ff3_test_monthly=gff.famaFrench3Factor(frequency='m') 
ff3_test_monthly.rename(columns={"date_ff_factors" : 'Date'}, inplace=True)
ff3_test_monthly.set_index('Date', inplace=True)

stock_returns = stock_data['Adj Close'].resample('m').last().pct_change().dropna()

stock_returns.name = "Month_Rtn"
ff_data = ff3_monthly.merge(stock_returns,on='Date')
 
X = ff_data[['Mkt-RF', 'SMB', 'HML']]

##Excess return on a monthly basis
y = ff_data['Month_Rtn'] - ff_data['RF']

X = sm.add_constant(X)
ff_model = sm.OLS(y, X).fit()
print(ff_model.summary())
intercept, b1, b2, b3 = ff_model.params

rf = ff_data['RF'].mean()
market_premium = ff3_monthly['Mkt-RF'].mean()
size_premium = ff3_monthly['SMB'].mean()
value_premium = ff3_monthly['HML'].mean()

expected_monthly_return = rf + b1 * market_premium + b2 * size_premium + b3 * value_premium 
expected_yearly_return = expected_monthly_return * 12
print("Expected yearly return: " + str(expected_yearly_return))


plt.scatter(ff_model.fittedvalues, y)
plt.xlabel('Fitted Values')
plt.ylabel('Actual Returns')
plt.title('Fitted Values vs Actual Returns')
plt.show()