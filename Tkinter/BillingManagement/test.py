ll = [['Name', 2, 3.3, 'Value'], ['Some', 5, 10.2, 'Thing']]

import json

json_str = json.dumps(ll)

print(type(json_str), json_str)

json_json = json.loads(json_str)

print(type(json_json), json_json)