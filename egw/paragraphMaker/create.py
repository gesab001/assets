
f = open("egw_text.txt", "r")
string = f.read()
#print(string)
import re
import os
import json
import shutil
pattern = "\{\w+ \d+.\d\}"
paraList = re.split(pattern, string)
#print(paraList)
del paraList[-1]
references = re.findall(pattern, string )
#print(x)
# ['one', 'two', 'three', 'four']


print(len(paraList))
print(len(references))
keyword = input("word to search: ")

"""
os.mkdir(keyword.upper())
index = 0
for x in range(0, len(paraList)):
  word = paraList[x].strip()
  if keyword in word.lower():
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
    filenameBookCode = keyword.upper()
    filename = "book_"+filenameBookCode+"_id_"+str(index)+".json"#book_DA_id_2122.json
    jsonObj = {"word": word, "paragraph": int(par), "bookcode": bookCode, "page": int(page)}
    print("filename: " + filename)
    print(jsonObj)
    #confirm = input("continue")

    with open("./" + filenameBookCode +"/"+filename, "w") as outfile:
          json.dump(jsonObj, outfile, indent=4)
"""

paragraphs = os.listdir(keyword.upper())
totalP = len(paragraphs)
bookCode = keyword.upper()
title = keyword.title()
jsonObj = {"total": totalP, "bookcode": bookCode, "title": title}
fopen = open("../booklist.json", "r")
booklistjsonstring = fopen.read()
booklistjson = json.loads(booklistjsonstring)
fopen.close()

print(jsonObj)
for item in booklistjson["items"]:
  itemBookcode = item["bookcode"]
  if itemBookcode== bookCode:
    print("bookcode already exist")
  else:  
    booklistjson["items"].append(jsonObj)
    with open("../booklist.json", "w") as outfile:
       json.dump(booklistjson, outfile, indent=4)
    break   

print(booklistjson)


  
import shutil

original = bookCode
target = "../" + original
try:
 shutil.move(original, target)
 print("directory moved successfully")
except:
 print("directory does not exist")

proceed = input("push to git?")
if proceed=="y":
  import subprocess
  command = "cd .. && cd .. && py pushtogit.py"
  subprocess.call(command, shell=True)
   