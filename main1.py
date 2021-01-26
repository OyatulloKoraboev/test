import requests
import json
from pprint import pprint


def res(arg):
    var = requests.get(f'https://randomuser.me/api/?{arg}')
    data = json.loads(var.text)
    return data


users = res('results=5')






dictionary = {
    "Users": users,
}

json_object = json.dumps(dictionary, indent=4)
with open("data1.json", "w") as outfile:
    outfile.write(json_object)

