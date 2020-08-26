import json

questions = []
add = int(input("add number: "))
for x in range(0,100):
  
   question = str(x)  + " + " +   str(add)
   answer = x + add
   a = answer
   b = x  - (add-1)
   c = x + (add+1)
   d = x + (add+2)
   choices = [a, b, c, d]
   jsondata = {"question": question, "answer": answer, "choices": choices}
   questions.append(jsondata)

with open("sample.json", "w") as outfile:
    json.dump(questions, outfile, indent=4)


f = open("math_questions.json")

jsondata = json.load(f)
f.close()

#clearDatabase()

samplefile = open("sample.json")
samplejson = json.load(samplefile)

titleset = input("titleset: ")
questions = samplejson
type = "addition"
jsondata[titleset] = {"type": type, "questions": []}
jsondata[titleset]["questions"] = questions

with open("math_questions.json", "w") as outfile:
   json.dump(jsondata, outfile, indent=4)

