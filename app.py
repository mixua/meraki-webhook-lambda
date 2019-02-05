import sys
import os
import rollbar
from flask import Flask, request, abort

app = Flask(__name__)

rollbar.init(os.environ.get('ROLLBAR_ACCESS_KEY'))


def rollbar_handler(record):
    message = 'title: Meraki Alert\n environment: external'.format(**record)
    rollbar.report_message(message, level='error')


@app.route('/', methods=['POST'])
def webhook() -> object:
    print("{\"action\":\"called webhook()\"}")
    sys.stdout.flush()
    if request.method == 'POST':
        if request.json['organizationId'] == os.environ['ORGANIZATION_ID']:
            msg = str(request.json).replace("u'", "\"").replace("'", "\"")
            print(msg)
            rollbar_handler(request.json)
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
