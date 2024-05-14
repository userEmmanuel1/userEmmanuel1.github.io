import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score  
import multiprocessing


def predict(ticker, stocks):
    



    # Input tracking stock
    ticker = ticker
    ticker = stocks

    # Fetch historical stock data from 2000 onwards
    prediction = yf.Ticker(ticker)
    prediction_2000 = prediction.history(period="max", start="2000-01-01")

    # Remove unnecessary columns from the DataFrame
    prediction_data = prediction_2000.drop(columns=["Dividends", "Stock Splits"])

    # Plot the closing prices over time
    #plt.plot(prediction_2000.index, prediction_2000['Close'], label=ticker)
    #plt.xlabel('Date')
    #plt.ylabel('Closing Price')
    #plt.title(f'{ticker} Closing Prices Over Time')
    #plt.legend()
    #plt.show()

    # Create a column for the next day's closing price
    prediction_2000["Tomorrow"] = prediction_2000["Close"].shift(-1)

    # Adding a binary target variable
    prediction_2000["Target"] = (prediction_2000["Tomorrow"] > prediction_2000["Close"]).astype(int)

    # Assuming "Target" is the column you want to predict
    train = prediction_2000.iloc[:-700]
    test = prediction_2000.iloc[-200:]
    predictors = ["Close", "Volume", "Open", "High", "Low"]

    # Train the model
    model = RandomForestClassifier(n_estimators=1000, min_samples_split=100, random_state=1)
    model.fit(train[predictors], train["Target"])

    # Make predictions on the test set
    preds = model.predict(test[predictors])

    # Calculate precision score
    precision = precision_score(test["Target"], preds)
    print("Precision Score:", precision)

    # Create a DataFrame to combine true and predicted values
    combine = pd.concat([test["Target"], pd.Series(preds, index=test.index, name="Predicted")], axis=1)

    # NOT NEEDED RN, ADD LATER
    #combine.plot(kind='bar', figsize=(10, 6))
    #   #plt.xlabel('Index')
    #   #plt.ylabel('Target and Predicted Values')
    #   #plt.title('Comparison of Target and Predicted Values')
    #   #plt.legend(["Target", "Predicted"])
    #   #plt.show()
predict('AAPL', 'AAPL')