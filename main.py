import requests
import json

def res(arg):
    var = requests.get(f'https://api.exchangeratesapi.io/{arg}')
    data = json.loads(var.text)
    return data["rates"]['USD']


difference = res('2021-01-26') - res('1999-01-26')


def res1(arg):
    var = requests.get(f'https://api.exchangeratesapi.io/{arg}')
    data = json.loads(var.text)
    return data


currency = res1('latest?base=RUB')
character = res1('latest?symbols=USD,GBP')
dates = res1('history?start_at=2018-01-01&end_at=2018-01-07')


dictionary = {
    "Difference": difference,
    'Different currency': currency,
    'Different_character': character,
    'Different_dates': dates,
}

json_object = json.dumps(dictionary, indent=4)
with open("data.json", "w") as outfile:
    outfile.write(json_object)
