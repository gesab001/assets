import json

def getStories():
 f = open("stories.json")
 jsondata = json.load(f)
 f.close()
 return jsondata

alphabets = "abcdefghijklmnopqrstuvwxyz"


def deleteStory(title, letter):
  print(title)
  print(letter)
  f = open("stories.json")
  jsondata = json.load(f)
  f.close()
  for i in range(0, 26):
     if jsondata[i]["letter"]==letter:
         jsondata[i]["names"].remove(title)
  print(jsondata)
  with open("stories.json", "w") as outfile:
     json.dump(jsondata, outfile)
def getLettersList():
  result = list(alphabets)
  return result
  
def clearDatabase():
  jsondata = []
  letterslist = getLettersList()
  for l in letterslist:
    print(l.capitalize())
    letter = l.capitalize()
    obj = {"letter": letter, "names":[]}
    jsondata.append(obj)
  with open("stories.json", "w") as outfile:
    json.dump(jsondata, outfile)

#clearDatabase()


while True:
   print(getStories())
   newstory = input("story title: " )
   letter = newstory[0:1].upper()
   deleteStory(newstory.capitalize(), letter)
