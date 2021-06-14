import json

book = input("book: ")
chapter = input("chapter: ")
imagefolder = input("imagefolder:" )
f = open("sample.txt")
string = f.read()
par = string.split("\n\n")
slides = {"slides": []}
for x in par:
 verse = x.split("\n")
 empty = ""
 if empty in verse:
   verse.remove(empty)
 combined = ""
 start = verse[0][0:2].strip()
 end = verse[-1][0:2].strip()
 for y in verse:
   if y!='':
     index = y.index(".")+2
     string = y[index::]
     combined = combined + string + "  "
 slide = {"text": combined, "reference": {"book": book, "chapter": chapter, "verse": {"start": start, "end": end}}, "image": "https://gesab001.github.io/assets/images/"+imagefolder}

 slides["slides"].append(slide)

with open("bibleslides.json", "w") as outfile:
   json.dump(slides, outfile, indent=4)
