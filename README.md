# TickerChart - Stock Market Chart API

TickerChart is a Python-based API built using flask that provides historical stock market chart data for companies listed on the Indian National Stock Exchange (NSE). It leverages the popular Flask web framework and yfinance library to fetch and deliver stock market data in JSON format.

## Deployment

The TickerChart API is now deployed and accessible on PythonAnywhere. You can access the API using the following endpoint:

- **API Endpoint** : [http://nehalhosalikar.pythonanywhere.com/chart](http://nehalhosalikar.pythonanywhere.com/chart)

## How to Use

To use the TickerChart API, send a GET request to the `/chart` endpoint with the required query parameters.

### Parameters

- `ticker`: The stock ticker symbol of the company you want to retrieve data for.
- `period`: The time duration for which you want historical data. Valid periods are: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`.
- `interval`: The time interval between data points. Valid intervals are: `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `1h`, `1d`, `1wk`, `1mo`, `3mo`.

### Response

The API will respond with JSON data containing historical stock market chart data for the requested company and period. The data will be presented in a list of records format.

## Example API Usage

To use the TickerChart API, make a GET request to the `/chart` endpoint with the required query parameters. Here's an example API call:

- **Example API Call** : http://nehalhosalikar.pythonanywhere.com/chart?ticker=TATASTEEL&period=1d&interval=1m

## Setup and Installation (For custom use)

1. Clone this repository to your local machine.
```
git clone https://github.com/NehalH/TickerChart.git
```

2. Navigate to the project directory.
```
cd TickerChart
```

3. Install dependencies.
```
pip install -r requirements.txt
```

### Note

- `Python 3.8` or higher is required.

## Run the API

To run the API, execute the following commands:
```
cd src
```
```
python api.py
```
By default, the API will run on http://127.0.0.1:5000/.

### Example Endpoint (LocalHost)

GET http://127.0.0.1:5000/chart?ticker=TATASTEEL&period=1d&interval=1m

### Error Handling

If the requested ticker symbol is not found, the API will respond with a 404 Not Found status code and a corresponding error message.
For invalid query parameters or any other errors, the API will return a 400 Bad Request status code.