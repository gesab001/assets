import json

questions = []

for x in range(0,100):

   question = str(x)  + " + " +   str(1)
   answer = x + 1
   a = x - 1
   b = x 
   c = x + 2
   d = x + 3
   choices = [a, b, c, d]
   jsondata = {"question": question, "answer": answer, "choices": choices}
   questions.append(jsondata)

with open("sample.json", "w") as outfile:
    json.dump(questions, outfile, indent=4)
