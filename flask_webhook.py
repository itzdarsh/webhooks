from flask import Flask, request
import json,urllib
import re


app = Flask(__name__)

def parse_request(req):
    """
    Parses application/json request body data into a Python dictionary
    """
    payload = req.get_data()
    payload = urllib.parse.quote_plus(payload)
    payload = re.sub('payload=', '', payload)
    payload = json.loads(payload)

    return payload

@app.route('/alerting', methods=['POST'])
def print_test():
    """
    Send a POST request to localhost:5000/api/print with a JSON body with a "p" key
    to print that message in the server console.
    """
    payload = parse_request(request)
    print(payload['p'])
    return ("", 200, None)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True,host='192.168.1.11', port=8080)