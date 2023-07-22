from flask import Flask, request
from flask_restful import Resource, Api
from chart_source import get_stock_data

app = Flask(__name__)
api = Api(app)

class Chart(Resource):
    @staticmethod
    def parse_request():
        args = request.args
        ticker = args.get('ticker', type=str)
        period = args.get('period', type=str)
        interval = args.get('interval', type=str)
        return ticker, period, interval

    def get(self):
        ticker, period, interval = Chart.parse_request()
        if not bool(ticker):
            return {
                'message':'No query parameters were passed for the API call. Refer documentation.',
                'doc':'https://github.com/NehalH/TickerChart/blob/main/README.md#how-to-use'
            }
        
        data = get_stock_data(ticker, period, interval)
        if bool(data):
            return {
                'data': data,
            }, 200
        else:
            return {
                'message': f'The ticker {ticker} was not found.'
            }, 404

api.add_resource(Chart, "/chart")

if __name__ == "__main__":
    app.run(debug=True)