f = open("sample.txt")
string = f.read()
par = string.split("\n\n")
slides = []
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
 slide = {"text": combined, "book": "John", "chapter": 11, "verse": {"start": start, "end": end}}
 print(slide)
 print()
