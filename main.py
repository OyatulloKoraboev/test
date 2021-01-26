import requests
import json
from pprint import pprint


def res(arg):
    response = requests.get(f'https://api.exchangeratesapi.io/{arg}')
    data = json.loads(response.text)
    return data["rates"]['USD']


difference = res('2021-01-26') - res('1999-01-26')

dictionary = {
    "difference": difference,
}

json_object = json.dumps(dictionary, indent=4)
with open("data.json", "w") as outfile:
    outfile.write(json_object)
