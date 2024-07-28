import json
import os

bookcode = "GC"
chapterT = "The Destruction of Jerusalem"
chapterN = 1
files = os.listdir()
jsonfiles = []
jsonfiles.sort()
for f in files:
  if f.endswith("json"):
     jsonfiles.append(f)
     
print(len(jsonfiles))
totalfiles = len(jsonfiles)
for x in range(1, totalfiles+1):
  filename = "book_"+bookcode+"_id_"+str(x)+".json"
  f = open(filename, "r")
  jsonobj = json.loads(f.read())
  f.close()
  page = str(jsonobj["page"])
  word = jsonobj["word"]
  proceed = input("continue?")
  print(word)
  print(page)
