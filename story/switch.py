import json

with open("stories.json") as f:
    data = json.load(f)

abc = "abcdefghijklmnopqrstuvwxyz"
abclist = list(abc)
newStoryList = []
for i in abclist:
    jsondata = {"letter": i.upper(), "names":[]}
    newStoryList.append(jsondata)
    
for item in data:
    print(item)
    titles = item["names"]
    for title in titles:
        otherTitle = title["otherTitle"]
        firstletter = otherTitle[0].lower()
        print(firstletter)
        indexLetter = abclist.index(firstletter)
        itemtomove = title
        print("itemtomove: ")
        print(itemtomove)
        newStoryList[indexLetter]["names"].append(itemtomove)

print("NEW STORY LIST")
for x in newStoryList:
    print(x)
    print()

with open("stories2.json", "w") as f:
    json.dump(newStoryList, f, indent=True)