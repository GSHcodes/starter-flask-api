from flask import Flask, request, jsonify
from calculations import calculate_age , convert_currency

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        intent_display_name = data['queryResult']['intent']['displayName']

        if intent_display_name == 'CurrencyConvert':
            #fetch data from json
            source_currency = data['queryResult']['parameters']['unit-currency']['currency']
            amount_source = data['queryResult']['parameters']['unit-currency']['amount']
            to_currency = data['queryResult']['parameters']['currency-name']
            #convert usign forex python
            converted = convert_currency(source_currency, amount_source, to_currency)
            #response to dialogflow
            response = {
                'fulfillmentText': "{} {} is equivalent to {} {}".format(amount_source, source_currency, converted, to_currency)
            }

        elif intent_display_name == 'ageCalculator':
            #fetch data
            datetime = data['queryResult']['parameters']["date-time"][0]
            dob_str = datetime.split("T")[0]
            #calculate
            age_result = calculate_age(dob_str)
            print(age_result)
            #response to dialogflow
            response = {
                'fulfillmentText': "{}".format(age_result)
            }

        else:
            # Default response if intent is not recognized
            response = {
                'fulfillmentText': "Intent not recognized"
            }

        return jsonify(response)
    else:
        return "Method Not Allowed", 405

if __name__ == '__main__':
    print("Server starting...")
    app.run(debug=True)
