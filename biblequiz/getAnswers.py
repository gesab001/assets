import json
import random

f = open("quiz.json")
jsondata = json.load(f)
answers = jsondata["answers"]
shuffled = random.shuffle(answers)
for a in answers:
  print(a)
