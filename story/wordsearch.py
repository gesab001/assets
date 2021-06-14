import json
import re

f = open("gadarenes.txt")
string = f.read()
list1 = string.strip().split(" ")
filterwords = ["the", "a", "an", "thy", "thee", "of", "and", "thou", "unto", "have", "into", "also", "with", "them", "among", "they", "came", "other", "saith", "when", "been", "would", "come", "said", "hath", "himself", "went", "might", "ask", "asked", "saying", "that", "there", "What", "what", "their", "about", "much", "were", "could", "told", "because", "began"]
list_set = set(list1) 
    # convert the set to the list 
unique_list = (list(list_set)) 
unique_list2 = []
for word in unique_list:
   word1 = word.replace("\n", "")
   word2 = word1.replace(".", "")
   word3 = word2.replace(",", "")
   word4 = word3.replace("?", "")
   output = re.sub(r'\d+', '', word4)
   output = re.sub(r'[\[\]\:\;\)\(]*', '', output)
   wordlength = len(output)

   if output.lower() not in filterwords:
     if wordlength>3:
       unique_list2.append(output.upper())

for word in unique_list2:
   print(word)  
print(len(unique_list2))

