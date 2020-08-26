import json

questions = []

for x in range(0,100):

   question = str(x)  + " + " +   str(1)
   answer = x + 1
   a = answer
   b = x  - 1
   c = x
   d = x + 2
   choices = [a, b, c, d]
   jsondata = {"question": question, "answer": answer, "choices": choices}
   questions.append(jsondata)

with open("sample.json", "w") as outfile:
    json.dump(questions, outfile, indent=4)
