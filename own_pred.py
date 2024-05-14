# %%
import pandas as pd
import yfinance as yf
import statsmodels.api as sm 
import getFamaFrenchFactors as gff 
import datetime as dt
import multiprocessing

ticker = 'V'
start = '2000-01-01'
end = '2019-01-01'

stock_data = yf.download(ticker, start, end, actions=True)
print(stock_data)


# %%
ff3_monthly = gff.famaFrench3Factor(frequency='m')
ff3_monthly.rename(columns={"date_ff_factors" : 'Date'}, inplace=True)
ff3_monthly.set_index('Date', inplace=True)
print(ff3_monthly)


# %%
import yfinance as yf
import multiprocessing
ticker = ticker
start_test = '2020-01-01'
end_test = '2021-01-01'

# Download historical stock data
stock_test = yf.download(ticker, start_test, end_test, actions=True)

# Drop unnecessary columns
columns_to_drop = ['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']
stock_test.drop(columns=columns_to_drop, inplace=True)

# Extract adjusted closing prices
adj_close_prices = stock_test['Adj Close']
global percentage_difference
# Calculate percentage difference from the start of the year to the end
start_of_year_price = adj_close_prices.iloc[0]
end_of_year_price = adj_close_prices.iloc[-1]
percentage_difference = ((end_of_year_price - start_of_year_price) / start_of_year_price) * 100

print(stock_test)
print(f"Start of Year Date: {start_test}, Adjusted Close: ${start_of_year_price:.2f}")
print(f"End of Year Date: {end_test}, Adjusted Close: ${end_of_year_price:.2f}")
print(f"Percentage Difference: {percentage_difference:.2f}%")


# %%
import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import getFamaFrenchFactors as gff
import multiprocessing
import matplotlib.pyplot as plt
import datetime as dt


##ALLOW USER INPUT##
ticker = ticker
#trainging data#
start_train = '2001-01-01'
end_train ='2020-01-01'



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
global expected_yearly_return_int
expected_monthly_return = rf + b1 * market_premium + b2 * size_premium + b3 * value_premium 
expected_yearly_return = expected_monthly_return * 12
expected_yearly_return_int = float (expected_yearly_return *100)
print("Expected yearly return: " + str(expected_yearly_return))
print (f"Number {expected_yearly_return_int}")

# %%
import multiprocessing 
#Just to give more weight on newer data
avg_est_return = ((expected_yearly_return_int + percentage_difference * 1.5 )) / 2 
print(avg_est_return)



# %%
