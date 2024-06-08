import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    data = data["Close"].mean()
    print(data)

if __name__ == '__main__':
    data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03'], 'Close': [150, 110, 120]}
    df = pd.DataFrame(data)
    calculate_and_display_average_price(df)



