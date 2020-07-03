import json

f = open("quiz.json")
jsondata = json.load(f)
print(jsondata)
totalQuestions = str(len(jsondata["items"]))
print("total questions: "+totalQuestions)
f.close()
count = 0
while True:
  question = input("question: ")
  answer = input("answer: ")
  newdata = {}
  newdata["question"] = question
  newdata["answer"] = answer
  jsondata["items"].append(newdata)
  jsondata["answers"].append(answer)
  jsondata["questions"].append(question)
  with open("quiz.json", "w") as outfile:
    json.dump(jsondata, outfile)
  count = count + 1
  print(count)
