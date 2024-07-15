# Stock Price Prediction

## High-level Overview
The project aims to develop a stock price predictor that forecasts the adjusted close price of Apple Inc. (AAPL) using historical trading data. This tool is designed to help investors and analysts make informed decisions based on predictive insights into stock price movements.

## Description of Input Data
For this stock price predictor, we utilize historical trading data of Apple Inc. (AAPL) from January 2019 to December 2023. The dataset includes multiple metrics such as:
- **Opening Price (Open)**: The price at which the stock starts trading at the beginning of the day.
- **Highest Price (High)**: The maximum price the stock reaches during the trading day.
- **Trading Volume (Volume)**: The number of shares traded during the day.
- **Adjusted Close Price (Adjusted Close)**: The closing price adjusted for stock splits and dividends, which our system aims to predict.

## Strategy for Solving the Problem
Our approach involved a comprehensive data-driven process:
1. **Data Cleaning and EDA**: Ensuring data quality and exploring key patterns.
2. **Feature Engineering**: Creating lag features and moving averages to capture temporal dependencies.
3. **Model Selection**: Evaluating different models, including Ridge Regression and SARIMA, to identify the best-performing one.
4. **Hyperparameter Tuning**: Using grid search to optimize model performance.
5. **Evaluation**: Assessing the model using relevant metrics and visualizations.

## Discussion of the Expected Solution
The solution architecture involves data preprocessing, feature engineering, model training, and evaluation. The workflow starts with data cleaning, followed by feature engineering to create relevant features for the models. We then train multiple models, tune their hyperparameters, and evaluate their performance to select the best one. The final model is deployed in a Flask web application for user interaction.

## Metrics with Justification
- **Mean Absolute Error (MAE)**: Measures the average magnitude of errors in predictions without considering their direction. It provides a clear indication of the average prediction error.
- **Mean Squared Error (MSE)**: Emphasizes larger errors due to the squaring term, helping to penalize significant deviations more than MAE.
- **Root Mean Squared Error (RMSE)**: Provides error magnitude in the same units as the target variable, making it easier to interpret.
- **Mean Absolute Percentage Error (MAPE)**: Indicates the accuracy as a percentage, making it easier to understand relative prediction errors.
- **R-squared**: Measures the proportion of variance explained by the model, indicating the model's explanatory power.

## Exploratory Data Analysis (EDA)
EDA provided insights into the dataset's structure and identified patterns and trends using summary statistics and visualization techniques. This helped address business questions like Adjusted Close Price Trend Over Time, Annual High and Low Prices, Trading Volume, Monthly Returns, and 30-Day Rolling Average.

## Data Preprocessing
The preprocessing steps included:
1. **Handling Missing Values**: No missing values were found in the dataset.
2. **Removing Duplicates**: No duplicate records were detected.
3. **Feature Engineering**: Created lag features and moving averages to capture temporal patterns.
4. **Dropping NA Values**: Removed rows with any NA values resulting from the above operations.

## Modeling
We explored multiple models:
1. **Ridge Regression**: A linear model with L2 regularization to prevent overfitting.
2. **SARIMA**: A time series model that captures both seasonal and non-seasonal components.

We chose Ridge Regression due to its robustness and ability to handle multicollinearity. The model was trained using lag features and moving averages as predictors.

## Hyperparameter Tuning
We used grid search for hyperparameter tuning. For Ridge Regression, we tuned parameters like `alpha` and `solver`. The optimal parameters were selected based on cross-validated performance metrics.

## Results
The final model's performance was evaluated using the chosen metrics:
- **MAE**: 1.0953532692134627
- **MSE**: 2.0597566576190974
- **RMSE**: 1.4351886817181853
- **MAPE**: 0.0096449479734243943
- **R-squared**: 0.9932174961013785

These results indicate a high level of accuracy in the model's predictions.

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

## Conclusion
The stock price prediction model demonstrates strong predictive capabilities, accurately forecasting the adjusted close price of AAPL. This tool can assist investors in making informed decisions by providing insights into future stock price movements.

## Improvements
Future enhancements could include incorporating additional features such as macroeconomic indicators, sentiment analysis from news articles, and more sophisticated modeling techniques like deep learning.

## Acknowledgment
We acknowledge the support and resources provided by the data science community, open-source libraries, and the organizations that made the data available.

