import requests
import json
from pprint import pprint


def res(arg):
    var = requests.get(f'https://api.exchangeratesapi.io/{arg}')
    data = json.loads(var.text)
    return data["rates"]['USD']


difference = res('2021-01-26') - res('1999-01-26')


def res1(arg):
    var = requests.get(f'https://api.exchangeratesapi.io/{arg}')
    data = json.loads(var.text)
    return data


dif_currency = res1('latest?base=RUB')


def res2(arg):
    var = requests.get(f'https://api.exchangeratesapi.io/{arg}')
    data = json.loads(var.text)
    return data


character = res2('latest?symbols=USD,GBP')


def res3(arg):
    var = requests.get(f'https://api.exchangeratesapi.io/{arg}')
    data = json.loads(var.text)
    return data


dates = res3('history?start_at=2018-01-01&end_at=2018-01-07')




dictionary = {
    "Difference": difference,
    'Different currency': dif_currency,
    'Different_character': character,
    'Different_dates': dates,
}

json_object = json.dumps(dictionary, indent=4)
with open("data.json", "w") as outfile:
    outfile.write(json_object)
