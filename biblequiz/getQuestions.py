import json

f = open("quiz.json")
jsondata = json.load(f)
questions = jsondata["questions"]
for q in questions:
  print(q)
