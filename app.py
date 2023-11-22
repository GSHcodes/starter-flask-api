from flask import Flask, request
import json

from forex_python.converter import CurrencyRates
currency=CurrencyRates()

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount_source = data['queryResult']['parameters']['unit-currency']['amount']
        to_currency = data['queryResult']['parameters']['currency-name']
        converted = currency.convert(source_currency, to_currency, amount_source)
        response = {
            'fulfillmentText': "{}  {}  is equivalent to  {}  {}".format(amount_source,source_currency,round(converted,2),to_currency),  # You can modify this message accordingly
            # Additional fields if needed
        }

        # Returning the response as a JSON string
        return json.dumps(response)
    else:
        return "Method Not Allowed", 405

if __name__ == '__main__':
    print("Server starting...")
    app.run(debug=True)
