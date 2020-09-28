import json

questions = []
#addition 1-100 adding 0-9

add = int(input("add number: "))
minN = add
maxN = 100+minN
for x in range(minN,maxN):
  
   question = str(x)  + " - " +   str(add)
   answer = x - add
   a = answer
   b = a  + 1 
   c = a  + 2
   d = a + 3
   choices = [a, b, c, d]
   jsondata = {"question": question, "answer": answer, "choices": choices}
   questions.append(jsondata)

with open("sample.json", "w") as outfile:
    json.dump(questions, outfile, indent=4)



#counting to 10
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(0,100):
   question = "L" * numbers[0]
   answer = numbers[0]
   a = answer
   b = x  - (answer-1)
   c = x + (answer+1)
   d = x + (answer+2)
   choices = [a, b, c, d]
   jsondata = {"question": question, "answer": answer, "choices": choices}
   questions.append(jsondata)
   del numbers[0]
   if len(numbers)==0:
      numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open("sample.json", "w") as outfile:
    json.dump(questions, outfile, indent=4)
"""

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

