import json

year = input("year: ")
f = open("sample.txt", "r")
string = f.read()
liststring = string.split("\n")
newlist = []
letters = []
for x in liststring:
  if x!='':
     newlist.append(x.strip())
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letterslist = list(alphabets)
print(letterslist)
newtopic = {}
count = 0
activitycount = 1
for x in newlist:
  if "." not in x:
     print(x)
     if count>25:
       newtopic = {"title": x.strip(), "letter": letterslist[count%26]+letterslist[count%26], "activities": []}
     else:
       newtopic = {"title": x.strip(), "letter": letterslist[count], "activities": []}
     letters.append(newtopic)
     count = count + 1
     activitycount = 1
  else:
     newgame = {"number": activitycount, "title": x[4::].strip(), "resource": 'url'}
     newtopic["activities"].append(newgame)
     activitycount = activitycount + 1
  
with open("english_year_"+year+".json", "w") as outfile:
    json.dump(letters, outfile, indent=4)
