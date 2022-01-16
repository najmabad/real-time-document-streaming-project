import json
import requests

with open('./output.txt') as f:
    for line in f:
        line_json = json.loads(line)
        response = requests.post('http://localhost:80/invoiceitem', json=line_json)

        if response.status_code != 201:
            print("*"*80)
            print("Original line:")
            print(line_json)
            print("*"*80)
            print("Response:")
            print(response.json())
            print("*"*80)
            print("*"*80)