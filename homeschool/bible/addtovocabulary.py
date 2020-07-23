import json

filename = input("filename: ")
f = open(filename)
jsondata = json.load(f.read())
print(jsondata)
