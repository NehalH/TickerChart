from flask import Flask, request
from flask_restful import Resource, Api

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
        return {
            'data': ticker,
            'period': period,
            'interval': interval
        }, 200

api.add_resource(Chart, "/chart")

if __name__ == "__main__":
    app.run(debug=True)
