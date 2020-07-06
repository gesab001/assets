import os
import json

jsondata = {"items": []}
arr = os.listdir()

for x in arr:
   isDirectory = os.path.isdir(x)
   if isDirectory:
     print(x)
     files = os.listdir(x)
     files.sort()
     jsonobj = {x: []}     
     for file in files:
        if file.endswith(".MP4"):
            url = 'https://gesab001.github.io/assets/videos/'+x+"/"+file 
            jsonobj[x].append(url)
     print(jsonobj)
     jsondata["items"].append(jsonobj)
   else:
     if x in jsondata["items"]:
             print(x + ": exists")  
     else:
             print("not exists")
             if (x.lower().endswith(".mp4")):
              urlsinglevideo = 'https://gesab001.github.io/assets/videos/' + x  
              jsondata["items"].append(urlsinglevideo)


#newimage = input("url : " )
#folder = input("folder: " )
#if newimage not in jsondata[folder]:   
#   jsondata[folder].append(newimage)

with open("videolist.json", "w") as outfile:
    json.dump(jsondata, outfile)
