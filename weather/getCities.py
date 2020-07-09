import json

f = open("city.list.json")
citylist = json.load(f)
f.close()
cities = {}
count = len(citylist)
for x in citylist:
  city = x["name"]
  id = x["id"]
  cities[city] = id
  count = count - 1
  print(count)

with open("cities.json", "w") as outfile:
   json.dump(cities, outfile)


