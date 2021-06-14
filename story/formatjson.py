import json

filename = input("filename: ")
f = open(filename)
data = json.load(f)
f.close()
with open(filename, "w") as outfile:
   json.dump(data, outfile, indent=4, sort_keys=True)
