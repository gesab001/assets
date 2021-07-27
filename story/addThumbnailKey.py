import json
  
# Opening JSON file
f = open('stories.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in range(0, len(data["new"])):

     name = data["new"][i]["title"]
     folder = name.replace(" ", "").lower();
     url = "https://gesab001.github.io/assets/images/"+folder+"/poster.jpg";
     data["new"][i]["thumbnail"] = url
     print(data["new"][i])
  
# Closing file
f.close()

with open("stories.json", "w") as json_outfile:
   json.dump(data, json_outfile, indent=4)
