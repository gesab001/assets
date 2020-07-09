import json

f = open("city.list.json")
jsondata = json.load(f)
print(jsondata[0])
nz = []
countries = []
for x in jsondata:
   location = x["name"]
   country = x["country"]
   print(location)
   if country not in countries:
      countries.append(country)
      print("added new country")

countries.sort()
del countries[0]
print("total countries: " + str(len(countries)))
with open("countries.json", "w") as outfile:
   data = {"items" : countries}
   json.dump(data, outfile)
