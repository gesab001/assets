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
     question = input("question: ")
     answer = input("answer: ")
     a = answer
     b = input("choice b: ")
     c = input("choice c: ")
     d = input("choice d: ")
     data["question"] = question
     data["answer"] = answer
     data["choices"] = [a, b, c, d]
     questions.append(data)
   return questions

def createSlides(title, book, chapter):
    imagefolder = title.lower().replace(" ", "")
    
    bibletext = imagefolder + ".txt"
    print("bibletext:" + bibletext)
    f = open(bibletext)
    string = f.read()
    
    par = string.split("\n\n")
   
    slides = {"slides": []}
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
     slide = {"text": combined, "reference": {"book": book, "chapter": chapter, "verse": {"start": start, "end": end}}, "image": "https://raw.githubusercontent.com/gesab001/assets/master/images/"+imagefolder}
     

     slides["slides"].append(slide)
    for slide in slides["slides"]:
        print(slide["text"])
    return slides["slides"];

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
     if jsondata["atoz"][i]["letter"]==letter:
        if title not in jsondata["atoz"][i]["names"]:
          jsondata["atoz"][i]["names"].append(title)
          #add to new
          jsondata["new"].append(title)
          print(jsondata)
          with open("stories.json", "w") as outfile:
             json.dump(jsondata, outfile, indent=4)
          createNewStory(title["title"], book, chapter)

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
   title = input("story title: " )
   otherTitle = input("alternative story title: " )
   description = input("description: ")
   categories = input("categories: (split by comma)")
   categorieslist = categories.split(",")
   book = input("book: ")
   chapter = input("chapter: ")
   letter = title[0:1].upper()
   titleJson = {"title": title.capitalize(), "otherTitle": otherTitle.capitalize(), "description": description, "categories": categorieslist}
   addStory(titleJson, letter, book, chapter)
   updateIndexHtml("added a new story - " + title) 
