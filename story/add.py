import json
import subprocess
f = open("stories.json")
jsondata = json.load(f)
f.close()
alphabets = "abcdefghijklmnopqrstuvwxyz"


def updateIndexHtml(message):
    fileappend = open("../index.html", "a+")
    fileappend.write("<p>added " + message + "</p>")
    fileappend.close() 

def createQuestions():
   questions = []
   for x in range(5):
     data = {"question": "", "answer": "", "choices": ["", "", "", ""]}
     questions.append(data)
   return questions

def createSlides(folder):
   slides = []
   for x in range(10):
     data = {"text": "", "image": "https://gesab001.github.io/assets/images/"+folder+"/"}
     slides.append(data)
   return slides

def createNewStory(title):
   filename = title.replace(" ", "_") + ".json"
   folder = title.replace(" ", "").lower()
   jsonobject = {"title": title, "slides": createSlides(folder), "questions": createQuestions(), "activities": [], "references": []}
   with open("./articles/"+filename, "w") as outfile:
      json.dump(jsonobject, outfile, indent=4)
   subprocess.call("mkdir  ~/assets/public/images/" + folder, shell=True)


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
   updateIndexHtml("added a new story - " + newstory) 
