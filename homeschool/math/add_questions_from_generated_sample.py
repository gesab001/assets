import json

f = open("math_questions.json")

jsondata = json.load(f)
f.close()


def updateIndexHtml(message):
    fileappend = open("../index.html", "a+")
    fileappend.write("<p>added " + message + "</p>")
    fileappend.close() 

def createQuestions():
   questions = []
   for x in range(20):
     data = {"question": "", "answer": "", "choices": ["", "", "", ""]}
     question = input("question " + str(x+1) + ": " )
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



#clearDatabase()

samplefile = open("sample.json")
samplejson = json.load(samplefile)

titleset = input("titleset: ")
questions = samplejson
jsondata[titleset] = {"questions": []}
jsondata[titleset]["questions"] = questions

with open("math_questions.json", "w") as outfile:
   json.dump(jsondata, outfile, indent=4)

