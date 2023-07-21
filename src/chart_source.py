import yfinance as yf

def get_stock_data(ticker, period, interval):

    ticker += '.NS'

    # Validating the interval value
    valid_intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '1h', '1d', '1wk', '1mo', '3mo']
    if interval not in valid_intervals:
        raise ValueError("Invalid interval value. Allowed intervals are: " + ", ".join(valid_intervals))

    # Validating the period value
    valid_periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    if period not in valid_periods:
        raise ValueError("Invalid period value. Allowed periods are: " + ", ".join(valid_periods))

    # Interval required 1 minute
    data = yf.download(tickers=ticker, period=period, interval=interval)

    # Convert the data to a dictionary
    data_dict = data.to_dict(orient='records')

    return data_dict
