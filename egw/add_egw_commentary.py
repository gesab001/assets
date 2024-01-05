import json

f = open("egw_commentary.json", "r")

jsonData = json.loads(f.read())
print(jsonData)
f.close()
book = input("book: ")
chapter = input("chapter: ")
verse = input("verse: ")
word = input("word: " )

egw = []
while True:
  comment = input("egw comment: (leave blank to exit)")
  if comment=="":
    break
  else:
    proceed = input("add this comment? (y/n)")
    if proceed.lower()=="y":
       egw.append(comment)

if book in jsonData:
 if chapter in jsonData[book]:
   jsonData[book][chapter][verse] = {"word": word, "egw": egw}
 else:
   jsonData[book][chapter] = {verse: {}}
   jsonData[book][chapter][verse] = {"word": word, "egw": egw}
else:
  jsonData[book] = {}
  jsonData[book][chapter] = {verse: {}}
  jsonData[book][chapter][verse] = {"word": word, "egw": egw}
  
with open("egw_commentary.json", "w") as outfile:
  json.dump(jsonData, outfile, indent=4)    

verseFileName = book.replace(" ", "-") + "_"+chapter+"_"+verse+".json"  
verseJsonData = {book: chapter}
with open(verseFileName, "w") as outfile:
  json.dump(verseJsonData, outfile, indent=4)   