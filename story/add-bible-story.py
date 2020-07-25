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

def createSlides(folder, book, chapter):
    slides = []
    f = open("sample.txt")
    string = f.read()
    par = string.split("\n\n")
    for x in par:
        verse = x.split("\n")
        empty = ""
        if empty in verse:
            verse.remove(empty)
        combined = ""
        start = verse[0][0:2].strip()
        end = verse[-1][0:2].strip()
        for y in verse:
            if y!='':
                index = y.index(".")+2
                string = y[index::]
                combined = combined + string + "  "
        slide = {"text": combined.strip(), "reference": {"book": book, "chapter": chapter, "verse": {"start": start, "end": end}}, "image": "https://gesab001.github.io/assets/images/"+folder+"/"}
        slides.append(slide)
    return slides

def createNewStory(title, book, chapter):
   filename = title.replace(" ", "_") + ".json"
   folder = title.replace(" ", "").lower()
   jsonobject = {"title": title, "slides": createSlides(folder, book, chapter), "questions": createQuestions(), "activities": [], "references": []}
   with open("./articles/"+filename, "w") as outfile:
      json.dump(jsonobject, outfile, indent=4)
   subprocess.call("mkdir  ~/assets/public/images/" + folder, shell=True)


def addStory(title, letter, book, chapter):
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
          createNewStory(title, book, chapter)

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
   book = input("book: ")
   chapter = input("chapter: ")
   letter = newstory[0:1].upper()
   addStory(newstory.capitalize(), letter, book, chapter)
   updateIndexHtml("added a new story - " + newstory) 
