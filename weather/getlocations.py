import json

f = open("city.list.json")
citylist = json.load(f)
f.close()
f = open("countries.json")
countries = json.load(f)
for x in countries["items"]:
  filename = x + ".json"
  print(filename)
  jsondata = {"items": []}
  with open(filename, "w") as outfile:
     json.dump(jsondata, outfile)
