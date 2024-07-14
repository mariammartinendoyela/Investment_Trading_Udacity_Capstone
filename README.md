
# Stock Price Predictor

## Project Overview
This project involves building a stock price predictor that takes daily trading data over a specified date range as input and outputs projected estimates for given query dates. The focus is on predicting the Adjusted Close price using historical data from Apple Inc. (AAPL) over the period from January 2019 to December 2023.

## Features
- **Data Loading**: Load historical stock prices from a CSV file.
- **Data Preprocessing**: Handle missing values, calculate additional features such as moving averages.
- **Model Training**: Train a linear regression model on the historical data.
- **Prediction**: Predict future stock prices based on the trained model.
- **Performance Measurement**: Evaluate model performance using Mean Squared Error (MSE) and R-squared metrics.
- **Visualization**: Provide various visualizations including adjusted close price trends, high and low prices over time, trading volume, monthly returns, and 30-day rolling average.

## Notable Files
- **`app.py`**: The main Flask application file for running the web interface.
- **`models/stock_predictor.py`**: Contains the StockPredictor class responsible for loading data, training the model, and making predictions.
- **`templates/index.html`**: The main page of the web interface.
- **`templates/results.html`**: Displays the prediction results.
- **`static/styles.css`**: CSS file for styling the web interface.

## Installation
1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    ```
2. **Navigate to the project directory**:
    ```sh
    cd Stock/project
    ```
3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. **Run the Flask application**:
    ```sh
    python app.py
    ```
2. **Open the application in your web browser**:
    Navigate to `http://127.0.0.1:5000/`
3. **Use the web interface**:
    - Enter the stock ticker symbol (e.g., AAPL).
    - Specify the prediction interval.
    - View the prediction results and visualizations.

## Visualizations
- **Adjusted Close Price Trend**: Shows the adjusted close price over time.
- **Annual High and Low Prices**: Candlestick chart of high and low prices over yearly intervals.
- **Trading Volume**: Visualizes trading volume in six-month intervals using a horizontal bar chart.
- **Monthly Returns**: Scatter plot of monthly returns over time.
- **30-Day Rolling Average**: Line chart comparing adjusted close price with its 30-day rolling average.


## Performance Metrics
- **Mean Squared Error (MSE)**: Evaluates the accuracy of the predictions.
- **R-squared**: Measures the proportion of the variance for the dependent variable.

## Conclusion
This project demonstrates the ability to predict stock prices using historical data and machine learning techniques. The web interface provides an easy-to-use platform for making predictions and visualizing stock performance.

