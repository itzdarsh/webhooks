from flask import Flask, request
import json,urllib,sys
import re

alert=[]
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
    with open('filename.txt', 'w') as f:
        sys.stdout = f
        print(payload['p'])
        alert.push(payload['p'])
    print(payload['p'])
    return (alert)

@app.route('/', methods=['GET'])
def home():
    html =  '''
    <h1> Hello world </h1>
    <h4><a href='/covid'> click here </a> for Covid-19 Data</h4>
    '''
    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
