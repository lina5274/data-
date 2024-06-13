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

def export_data_to_csv(data, filename):

with open('output.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    for row in data:
        csv_writer.writerow(row)

if __name__ == '__main__':
    ticker = 'GOOGL'
    stock_data = fetch_stock_data(ticker,)
    stock_data = add_moving_average(stock_data)
    calculate_and_display_average_price(stock_data)



