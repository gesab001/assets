import json
import re
text = open("christ_object_lessons.TXT", "r")
string = text.read()

pattern = "Chap.\s\d+\s-\s[a-zA-Z\s,\?\-\"]+\n{2}"
chapList = re.split(pattern, string)
chapterTitles = re.findall(pattern, string )

#print(chapList)
del chapList[0]

jsondata = {}
jsondata["title"] = "Christ's Object Lessons"  
jsondata["bookCode"] = "COL"
jsondata["year"] = "1900"
jsondata["author"] = "Ellen G. White"
jsondata["chapters"] = {}

for x in range(0, len(chapList)):

  chapterNu = str(x+1)
  chapterTitleRaw = chapterTitles[x].strip()
  pattern = "Chap.\s\d+\s-\s"
  titleSplit = re.split(pattern, chapterTitleRaw)
  chapterTitle = titleSplit[1]
  jsondata["chapters"][chapterNu] = {"chapterNumber": chapterNu , "chapterTitle": chapterTitle, "paragraphs": []}
  
  #divide chapter into paragraphs
  chapItemString = chapList[x].strip()
  pattern = "\{[A-Z]+\s\d+.\d+\}"
  parList = re.split(pattern, chapItemString)
  del parList[len(parList)-1]
  references = re.findall(pattern, chapItemString )
  #print(parList)
  #print(references)
  for i in range(0, len(parList)):
    word = parList[i].strip()
    pattern = "   \d+"
    containsPageNumber = re.findall(pattern, word)
    #print(word)

    if len(containsPageNumber)>0:
      print("chapter: " + chapterNu)
      print("paragraph: " + str(i))
      print("containsPageNumber: " + str(containsPageNumber))
      wordsplit = re.split(pattern, word)
      wordJoin = ""
      for wordsplititem in wordsplit:
         wordJoin = wordJoin + wordsplititem.strip()
      
      print(wordsplit)
      print()
      print(wordJoin)
      word = wordJoin
      #proceed = input("pause: ")
    reference = references[i].replace("{", "")
    reference = reference.replace("}", "")
    page = reference.split(" ")[1].split(".")[0]
    paragraphNumber = reference.split(" ")[1].split(".")[1]
    jsonobj = {"reference": reference, "chapter": chapterNu, "page": page, "paragraphNo": paragraphNumber, "word": word}
    jsondata["chapters"][chapterNu]["paragraphs"].append(jsonobj)
    

with open("col.json", "w") as outfile:
  json.dump(jsondata, outfile, indent=4) 