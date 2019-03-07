import sys
import os
import rollbar
from flask import Flask, request, abort

app = Flask(__name__)

token=os.environ['ROLLBAR_ACCESS_KEY']

rollbar.init(token, environment='external')

@rollbar.lambda_function
def rollbar_handler(event, context):
    networkName = event['networkName']
    alertType = event['alertType']
    rollbar.report_message(f"Meraki alert from: {networkName} alert type: {alertType}", 'warning', request, extra_data=event)

@app.route('/', methods=['POST'])
def webhook() -> object:
    print("{\"action\":\"called webhook()\"}")
    sys.stdout.flush()
    if request.method == 'POST':
        if request.json['organizationId'] == os.environ['ORGANIZATION_ID']:
            msg = str(request.json).replace("u'", "\"").replace("'", "\"")
            print(msg)
            rollbar_handler(request.json, msg)
            print("{\"success\":\"200\"}")
            return "{\"success\":\"200\"}", 200
        else:
            print("{\"outcome\":\"abort with 401\"}")
            abort(401)
    else:
        print("{\"outcome\":\"abort with 400\"}")
        abort(400)


if __name__ == '__main__':
    app.run()