import json
import subprocess
f = open("stories.json")
jsondata = json.load(f)
f.close()
alphabets = "abcdefghijklmnopqrstuvwxyz"

def createNewStory(title):
   filename = title.replace(" ", "_") + ".json"
   jsonobject = {"title": title, "slides": [{"text": "", "image": "https://gesab001.github.io/assets/images/"}], "questions": [{"question": "", "answer": "", "choices": []}], "activities": [], "references": []}
   with open("./articles/"+filename, "w") as outfile:
      json.dump(jsonobject, outfile)



def addStory(title, letter):
  print(title)
  print(letter)
  f = open("stories.json")
  jsondata = json.load(f)
  f.close()
  for i in range(0, 26):
     if jsondata[i]["letter"]==letter:
        if title not in jsondata[i]["names"]:
          jsondata[i]["names"].append(title)
          print(jsondata)
          with open("stories.json", "w") as outfile:
             json.dump(jsondata, outfile)
          createNewStory(title)

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
   newstory = input("story title: " )
   letter = newstory[0:1].upper()
   addStory(newstory.capitalize(), letter)
