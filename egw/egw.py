import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="gesab001",
  password="ch5t8k4u",
  database="egw"
)

book = raw_input("bookcode: " )
mycursor = mydb.cursor()

mycursor.execute("SELECT BOOKCODE, PAGE, PARAGRAPH, WORD, TITLE  FROM egw_writings_complete WHERE BOOKCODE='"+book+"'")

myresult = mycursor.fetchall()
count = 1
for x in myresult:
  print(x[0])
  jsondata = {"bookcode": x[0], "page": x[1], "paragraph": x[2], "word": x[3].strip()}
  filename = "book_{}_id_{}.json".format(x[0], count)
  print(filename)
  print(jsondata)
  with open(filename, "w") as outfile:
    json.dump(jsondata, outfile)
  count+=1
