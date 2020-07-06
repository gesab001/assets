import os
import json

f = open("videolist.json")
jsondata = json.load(f) 
f.close()
arr = os.listdir()

for x in arr:
   isDirectory = os.path.isdir(x)
   if isDirectory:
     print("not a video file")
   else:
     if x in jsondata["items"]:
             print(x + ": exists")  
     else:
             print("not exists")
             url = 'https://gesab001.github.io/assets/videos/' + x  
             jsondata["items"].append(url)


#newimage = input("url : " )
#folder = input("folder: " )
#if newimage not in jsondata[folder]:   
#   jsondata[folder].append(newimage)

with open("videolist.json", "w") as outfile:
    json.dump(jsondata, outfile)
