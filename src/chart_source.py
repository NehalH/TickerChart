import yfinance as yf

def get_stock_data(ticker, period, interval):
    ticker += '.NS'
    # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    data = yf.download(tickers=ticker, period=period, interval=interval)
    
    # Convert the data to a dictionary
    data_dict = data.to_dict(orient='records')
    
    return data_dict