import json

import requests


with open("./output.txt") as f:
    for line in f:
        try:
            line_json = json.loads(line)
            response = requests.post("http://localhost:80/invoiceitem", json=line_json)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e)
            print("*" * 80)
            print("Original line:")
            print(line_json)
            print("*" * 80)
            print("Response:")
            print(response.json())
            print("*" * 80)
            print("*" * 80)
