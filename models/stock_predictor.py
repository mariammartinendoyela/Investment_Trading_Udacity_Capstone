import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from datetime import timedelta

class StockPredictor:
    def __init__(self):
        self.models = {}
        self.features = ['Adj Close Lag1', 'Adj Close Lag2', 'Adj Close Lag3', 'SMA_5', 'SMA_10']
    
    def load_data(self, file_path):
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
        return data
    
    def train(self, ticker, data, start_date, end_date):
        stock_data = data[(data.index >= start_date) & (data.index <= end_date)].copy()
        
        stock_data['Adj Close Lag1'] = stock_data['Adj Close'].shift(1)
        stock_data['Adj Close Lag2'] = stock_data['Adj Close'].shift(2)
        stock_data['Adj Close Lag3'] = stock_data['Adj Close'].shift(3)
        stock_data['SMA_5'] = stock_data['Adj Close'].rolling(window=5).mean()
        stock_data['SMA_10'] = stock_data['Adj Close'].rolling(window=10).mean()
        stock_data.dropna(inplace=True)
        
        X = stock_data[self.features]
        y = stock_data['Adj Close']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        self.models[ticker] = (model, stock_data)
        
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = model.score(X_test, y_test)
        
        print(f'Ticker: {ticker}, Mean Squared Error: {mse}, R-squared: {r2}')
        return model
    
    def predict(self, dates, ticker):
        model, stock_data = self.models[ticker]
        last_date = stock_data.index[-1]
        predictions = {}

        for date in dates:
            if date <= last_date:
                lag1 = stock_data.loc[date - timedelta(days=1), 'Adj Close']
                lag2 = stock_data.loc[date - timedelta(days=2), 'Adj Close']
                lag3 = stock_data.loc[date - timedelta(days=3), 'Adj Close']
                sma_5 = stock_data.loc[date, 'SMA_5']
                sma_10 = stock_data.loc[date, 'SMA_10']
            else:
                if (date - timedelta(days=1)) in predictions:
                    lag1 = predictions[date - timedelta(days=1)]
                else:
                    lag1 = stock_data.iloc[-1]['Adj Close']
                if (date - timedelta(days=2)) in predictions:
                    lag2 = predictions[date - timedelta(days=2)]
                else:
                    lag2 = stock_data.iloc[-2]['Adj Close']
                if (date - timedelta(days=3)) in predictions:
                    lag3 = predictions[date - timedelta(days=3)]
                else:
                    lag3 = stock_data.iloc[-3]['Adj Close']
                sma_5 = sum([predictions[date - timedelta(days=x)] if (date - timedelta(days=x)) in predictions else stock_data.iloc[-x]['Adj Close'] for x in range(1, 6)]) / 5
                sma_10 = sum([predictions[date - timedelta(days=x)] if (date - timedelta(days=x)) in predictions else stock_data.iloc[-x]['Adj Close'] for x in range(1, 11)]) / 10
            
            features = pd.DataFrame([[lag1, lag2, lag3, sma_5, sma_10]], columns=self.features)
            predicted_price = model.predict(features)[0]
            predictions[date] = predicted_price
        
        return predictions
