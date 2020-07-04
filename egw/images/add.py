import os
import json

f = open("imagelist.json")
jsondata = json.load(f) 
f.close()
arr = os.listdir()

for x in arr:
   isDirectory = os.path.isdir(x)
   if isDirectory:
      if x not in jsondata:
       jsondata[x] = []
      files = os.listdir(x)
      for file in files:
          url = 'https://gesab001.github.io/assets/egw/images/' + x + "/" + file  
          if url in jsondata[x]:
             print(x + ": exists")  
          else:
             print("not exists")
             url = 'https://gesab001.github.io/assets/egw/images/' + x + "/" + file  
             jsondata[x].append(url)


#newimage = input("url : " )
#folder = input("folder: " )
#if newimage not in jsondata[folder]:   
#   jsondata[folder].append(newimage)

with open("imagelist.json", "w") as outfile:
    json.dump(jsondata, outfile)
