import json
import os
import re

path = "book_MONEY_id_1881.json"
f = open(path, "r")
string = f.read()
f.close()
regext = "{YI, October 4, 1900 par. 2}"
pattern = "\{\w+\s*\w*, \w+ \d+, \d+ par. \d+\}"
paraList = re.split(pattern, string)

references = re.findall(pattern, string )

del paraList[len(paraList)-1]
print(paraList[len(paraList)-1])

print(len(paraList))
print(len(references))
index = 3544
lastFilename = ""
for x in range(0, len(paraList)):
  word = paraList[x].strip()
  if "money" in word.lower():
    reference = references[x]
    reference = re.sub("{", "", reference)
    reference = re.sub("}", "", reference) 
    print(word)
    print(reference)


    bookCode = reference.split(" ")[0].replace(",", "")
    print("bookCode: " + bookCode)
    pattern = "\w+ \d+, \d+"
    page = re.search(pattern, reference).group()
    print(page)
    pattern = "par. \d+"
    par = re.search(pattern, reference).group().replace("par. ", "")
    print(par)

    index = index + 1
    print("index: " + str(index))
    filenameBookCode = "DEBT"
    filename = "book_"+filenameBookCode+"_id_"+str(index)+".json"#book_DA_id_2122.json
    jsonObj = {"word": word, "paragraph": int(par), "bookcode": bookCode, "page": page}
    print("filename: " + filename)
    print(jsonObj)
    #choice = input("continue: ")
    #confirm = input("continue")
    with open(filename, "w") as outfile:
      json.dump(jsonObj, outfile, indent=4)
    lastFilename = filename  

print("lastFilename: " + lastFilename)
try:
  os.remove(path)
except Exception as e:
  print(e)

try:
  os.rename(lastFilename, path)
except Exception as e:
  print(e)
  
