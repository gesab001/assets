import json

f = open("city.list.json")
citylist = json.load(f)
f.close()
f = open("countries.json")
countries = json.load(f)
count = len(citylist)
for x in citylist:
  country = x["country"]
  city = x["name"]
  filename = country + ".json"
  id = x["id"]
  data = {"name": city, "id": id}
  f = open(filename)
  jsondata = json.load(f)
  jsondata["items"].append(data)

  f.close()
  with open(filename, "w") as outfile:
     json.dump(jsondata, outfile)
     print("added " + city + " to " + filename)
     print("left: " + str(count))
     count = count - 1
