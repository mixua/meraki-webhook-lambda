import sys
import os
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    print("called webhook()")
    sys.stdout.flush()
    if request.method == 'POST':
        if request.json['organizationId'] == os.environ['ORGANIZATION_ID']:
            print(request.json)
            print("success with 200")
            return "{\"success\":\"200\"}", 200
        else:
            print("abort with 401");
            abort(401)
    else:
        print("abort with 400")
        abort(400)


if __name__ == '__main__':
    app.run()
