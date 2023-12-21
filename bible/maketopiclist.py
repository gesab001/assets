import json


f = open("topics3.json", "r")
jsonObj = json.loads(f.read())
f.close()
topics = list(jsonObj.keys())
sorted_topiclist = []
for x in topics:
  sorted_topiclist.append(x.title())  
sorted_topiclist.sort()  


f = open("topics3.json", "r")
jsonObj2 = json.loads(f.read())
f.close()
sorted_topiclist2 = []

for x in topics:
    jsonObj2[x.title()] = jsonObj2[x]
    totalverses = len(jsonObj2[x.title()])
    del jsonObj2[x]
    if totalverses==0:
      del jsonObj2[x.title()]

sorted_topiclist2 = list(jsonObj2.keys())
sorted_topiclist2.sort()


"""
    print("totalverses: " + str(totalverses))
    if totalverses==0:
      del jsonObj2[x.title()]
    else:    
      topiclistobj = {x.title(): totalverses}
    sorted_topiclist2.append(topiclistobj)    
"""
result = {"topiclist": sorted_topiclist2, "items": jsonObj2}
print(jsonObj2.keys())    

with open("topics5.json", "w") as outfile:
  json.dump(result, outfile, indent=4, sort_keys=True)