import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ["Ann","Billy"],
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y=json.dumps(x)
print(y) 



j='[{"name":"John","repott":[{"subject":"Math","Score":80},{"subject":"English","Score":70}]},{"name":"mary","repott":[{"subject":"Math","Score":60},{"subject":"English","Score":50}]}]'
p=json.loads(j)
print(p)