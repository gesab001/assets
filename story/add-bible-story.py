import json
import subprocess
#from tkinter import *
#from tkinter import messagebox

f = open("stories.json")
jsondata = json.load(f)
f.close()
alphabets = "abcdefghijklmnopqrstuvwxyz"

"""
top = Tk()

keys = ["Title", "Other Title", "Description", "Categories", "Book", "Chapter"]
keyspairs = {}

for i in range(0,5):
	key = keys[i]
	print(key)
	Label(top, text=key).pack()
	pair = Entry(top, width=50).pack()
	keyspairs[key] = pair
	keyspairs[key] = pair

def submit():
   #msg = messagebox.showinfo( "Hello Python", E1.get())
   title = keyspairs["Title"].get()
   print(title)
   otherTitle = E2.get()
   description = E3.get()
   categories = E4.get()
   categorieslist = categories.split(",")
   book = E5.get()
   chapter = E6.get()
   bibletext = title.lower().replace(" ", "") 
   imagefolder = title.lower().replace(" ", "")
   bibletext = bibletext + ".txt"
   slides = createSlides(bibletext, imagefolder, book, chapter)
   letter = otherTitle[0:1].upper()
   folder = title.replace(" ", "").lower()
   titleJson = {"title": title.capitalize(), "otherTitle": otherTitle.capitalize(), "description": description, "categories": categorieslist, "newcoverposter": ""}
   questions = createQuestions() 
   addStory(titleJson, letter, slides, questions)
   updateIndexHtml("added a new story - " + title) 
   
B = Button(top, text = "Submit", command = submit)
B.pack(side = TOP)


	
L1 = Label(top, text = "story title")
L1.pack( side = TOP)
E1 = Entry(top, bd = 5)
E1.pack(side = TOP)

L2 = Label(top, text = "alternative title")
L2.pack( side = TOP)
E2 = Entry(top, bd = 5)
E2.pack(side = TOP)

L3 = Label(top, text = "description")
L3.pack( side = TOP)
E3 = Entry(top, bd = 5)
E3.pack(side = TOP)

L4 = Label(top, text = "categories")
L4.pack( side = TOP)
E4 = Entry(top, bd = 5)
E4.pack(side = TOP)

L5 = Label(top, text = "book")
L5.pack( side = TOP)
E5 = Entry(top, bd = 5)
E5.pack(side = TOP)

L6 = Label(top, text = "chapter")
L6.pack( side = TOP)
E6 = Entry(top, bd = 5)
E6.pack(side = TOP)


#QUESTION 1
question1 = Label(top, text = "question 1")
question1.pack( side = TOP)
question1 = Entry(top, bd = 5	)
question1.pack(side = TOP)

#ANSWER
answer1 = Label(top, text = "answer")
answer1.pack( side = TOP)
answer1 = Entry(top, bd = 5)
answer1.pack(side = TOP)

#B
b1 = Label(top, text = "b")
b1.pack( side = TOP)
b1 = Entry(top, bd = 5)
b1.pack(side = TOP)

#C
c1 = Label(top, text = "c")
c1.pack( side = TOP)
c1 = Entry(top, bd = 5)
c1.pack(side = TOP)

#D
d1 = Label(top, text = "d")
d1.pack( side = TOP)
d1 = Entry(top, bd = 5)
d1.pack(side = TOP)

#QUESTION 2
question2 = Label(top, text = "question 2")
question2.pack( side = TOP)
question2 = Entry(top, bd = 5)
question2.pack(side = TOP)

#ANSWER
answer2 = Label(top, text = "answer")
answer2.pack( side = TOP)
answer2 = Entry(top, bd = 5)
answer2.pack(side = TOP)

#B
b2 = Label(top, text = "b")
b2.pack( side = TOP)
b2 = Entry(top, bd = 5)
b2.pack(side = TOP)

#C
c2 = Label(top, text = "c")
c2.pack( side = TOP)
c2 = Entry(top, bd = 5)
c2.pack(side = TOP)

#D
d2 = Label(top, text = "d")
d2.pack( side = TOP)
d2 = Entry(top, bd = 5)
d2.pack(side = TOP)

#QUESTION 3
question3 = Label(top, text = "question 3")
question3.pack( side = TOP)
question3 = Entry(top, bd = 5)
question3.pack(side = TOP)

#ANSWER
answer3 = Label(top, text = "answer")
answer3.pack( side = TOP)
answer3 = Entry(top, bd = 5)
answer3.pack(side = TOP)

#B
b3 = Label(top, text = "b")
b3.pack( side = TOP)
b3 = Entry(top, bd = 5)
b3.pack(side = TOP)

#C
c3 = Label(top, text = "c")
c3.pack( side = TOP)
c3 = Entry(top, bd = 5)
c3.pack(side = TOP)

#D
d3 = Label(top, text = "d")
d3.pack( side = TOP)
d3 = Entry(top, bd = 5)
d3.pack(side = TOP)

#QUESTION 4
question4 = Label(top, text = "question 4")
question4.pack( side = TOP)
question4 = Entry(top, bd = 5)
question4.pack(side = TOP)

#ANSWER
answer4 = Label(top, text = "answer")
answer4.pack( side = TOP)
answer4 = Entry(top, bd = 5)
answer4.pack(side = TOP)

#B
b4 = Label(top, text = "b")
b4.pack( side = TOP)
b4 = Entry(top, bd = 5)
b4.pack(side = TOP)

#C
c4 = Label(top, text = "c")
c4.pack( side = TOP)
c4 = Entry(top, bd = 5)
c4.pack(side = TOP)

#D
d4 = Label(top, text = "d")
d4.pack( side = TOP)
d4 = Entry(top, bd = 5)
d4.pack(side = TOP)

#QUESTION 5
question5 = Label(top, text = "question 5")
question5.pack( side = TOP)
question5 = Entry(top, bd = 5)
question5.pack(side = TOP)

#ANSWER
answer5 = Label(top, text = "answer")
answer5.pack( side = TOP)
answer5 = Entry(top, bd = 5)
answer5.pack(side = TOP)

#B
b5 = Label(top, text = "b")
b5.pack( side = TOP)
b5 = Entry(top, bd = 5)
b5.pack(side = TOP)

#C
c5 = Label(top, text = "c")
c5.pack( side = TOP)
c5 = Entry(top, bd = 5)
c5.pack(side = TOP)

#D
d5 = Label(top, text = "d")
d5.pack( side = TOP)
d5 = Entry(top, bd = 5)
d5.pack(side = TOP)

"""

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

def createSlides(filename, imagefolder, book, chapter):
    print("bibletext:" + filename)
    f = open(filename)
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
     slide = {"text": combined, "reference": {"book": book, "chapter": chapter, "verse": {"start": start, "end": end}}, "image": "https://raw.githubusercontent.com/gesab001/assets/master/images/"+filename}
     

     slides["slides"].append(slide)
    for slide in slides["slides"]:
        print(slide["text"])
    return slides["slides"];

def createNewStory(title, slides, questions):
   filename = title.replace(" ", "_") + ".json"
   folder = title.replace(" ", "").lower()
   jsonobject = {"title": title, "slides": slides, "questions": questions, "activities": [], "references": []}
   with open("./articles/"+filename, "w") as outfile:
      json.dump(jsonobject, outfile, indent=4)
      print ("created article " + filename)
   subprocess.call("mkdir  ~/assets/public/images/" + folder, shell=True)


def addStory(title, letter, slides, questions):
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
          newtitle = title
          jsondata["new"].append(title)
          print(jsondata)
          with open("stories.json", "w") as outfile:
             json.dump(jsondata, outfile, indent=4)
          createNewStory(title["title"], slides, questions)

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





#top.mainloop()


while True:
   title = input("story title: " )
   otherTitle = input("alternative story title: " )
   videourl = otherTitle + ".mp4"
   description = input("description: ")
   categories = input("categories: (split by comma)")
   categorieslist = categories.split(",")
   book = input("book: ")
   chapter = input("chapter: ")
   bibletext = title.lower().replace(" ", "") 
   imagefolder = title.lower().replace(" ", "")
   bibletext = bibletext + ".txt"
   slides = createSlides(bibletext, imagefolder, book, chapter)
   letter = otherTitle[0:1].upper()
   folder = title.replace(" ", "").lower()
   titleJson = {"title": title.capitalize(), "otherTitle": otherTitle.capitalize(), "video": videourl, "description": description, "categories": categorieslist, "newcoverposter": "https://gesab001.github.io/assets/"+folder+"/newcoverposter.jpg"}
   questions = createQuestions() 
   addStory(titleJson, letter, slides, questions)
   updateIndexHtml("added a new story - " + title) 
   
