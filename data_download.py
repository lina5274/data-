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
    data.to_csv(filename, index=True)

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    return data

def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
    data['EMA12'] = data['Close'].ewm(span=fast_period, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=slow_period, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal_Line'] = data['MACD'].ewm(span=signal_period, adjust=False).mean()
    return data

def plot_stock_data_with_indicators(data, ticker):
    plt.figure(figsize=(14, 7))

    plt.subplot(3, 1, 1)
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['Moving_Average'], label='Moving Average')
    plt.title(f'{ticker} Stock Price and Moving Average')
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(data['RSI'], label='RSI')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title('RSI')
    plt.legend()
    plt.subplot(3, 1, 3)
    plt.plot(data['MACD'], label='MACD')
    plt.plot(data['Signal_Line'], label='Signal Line')
    plt.title('MACD')
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    ticker = 'GOOGL'
    stock_data = fetch_stock_data(ticker,)
    stock_data = add_moving_average(stock_data)
    calculate_and_display_average_price(stock_data)
    export_data_to_csv(stock_data, 'stock_data.csv')
    plot_stock_data_with_indicators(stock_data, ticker)



