
f = open("fast.txt", "r")
string = f.read()
#print(string)
import re
import os
import json

pattern = "\{\w+ \d+.\d\}"
paraList = re.split(pattern, string)
#print(paraList)
del paraList[-1]
references = re.findall(pattern, string )
#print(x)
# ['one', 'two', 'three', 'four']

print(len(paraList))
print(len(references))

index = 0
for x in range(0, len(paraList)):
  word = paraList[x].strip()
  if "fast" in word.lower():
    reference = references[x]
    reference = re.sub("{", "", reference)
    reference = re.sub("}", "", reference) 
    print(word)
    print(reference)
    bookCode = reference.split(" ")[0]
    page = reference.split(" ")[1].split(".")[0]
    par = reference.split(" ")[1].split(".")[1]
    print("bookCode: " + bookCode)
    print("page: " + page)
    print ("par: " + par)
    index = index + 1
    print("index: " + str(index))
    filenameBookCode = "FAST"
    filename = "book_"+filenameBookCode+"_id_"+str(index)+".json"#book_DA_id_2122.json
    jsonObj = {"word": word, "paragraph": int(par), "bookcode": bookCode, "page": int(page)}
    print("filename: " + filename)
    print(jsonObj)
    #confirm = input("continue")
    with open("./paragraphs/"+filename, "w") as outfile:
      json.dump(jsonObj, outfile, indent=4)
   