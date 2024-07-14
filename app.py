from flask import Flask, render_template, request
from models.stock_predictor import StockPredictor
import pandas as pd

app = Flask(__name__)

# Initialize StockPredictor
predictor = StockPredictor()
file_paths = {'AAPL': 'C:/Users/martm002/Stock/AAPL.csv'}
for ticker, file_path in file_paths.items():
    data = predictor.load_data(file_path)
    predictor.train(ticker, data, '2019-01-02', '2023-11-30')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ticker = request.form['ticker']
    interval = int(request.form['interval'])
    
    future_dates = pd.date_range(start='2023-12-01', periods=interval + 1, freq='D')
    predictions = predictor.predict(future_dates, ticker)
    
    return render_template('results.html', predictions=predictions, ticker=ticker)

if __name__ == '__main__':
    app.run(debug=True)
