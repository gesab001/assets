import json




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
while True:
    f = open("math_questions.json")
    jsondata = json.load(f)
    f.close()
    title = input("title: ")
    name = input("class name: ")
    newjsonobj = {"title": title, "name": name}
    jsondata["icons"].append(newjsonobj)
    with open("math_questions.json", "w") as outfile:
       json.dump(jsondata, outfile, indent=4)

