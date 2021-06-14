import json

with open("stories.json") as f:
    data = json.load(f)

with open("categoriesGroup.json") as f:
    categoriesGroupData = json.load(f)

def addNewCategory():
    new = input("new category: ")
    categoriesGroupData["items"].append(new)
    saveData("categoriesGroup.json", categoriesGroupData)

def printCategoriesGroup():
    categoriesGroup = categoriesGroupData["items"]
    for x in range(0, len(categoriesGroup)):
        count = str(x)
        print(count + ". " + categoriesGroup[x])    
    return categoriesGroup

def printData():
    count = 1
    for group in data:
        titles = group["names"]
        for title in titles:
            print(str(count)+". "  + str(title))
            count = count + 1
            
def saveData(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=True)
        
for group in data:
    printData()
    titles = group["names"]
    for title in titles:
        if type(title) is not dict:
            print(title + " needs an update")
            otherTitle = input("otherTitle: ")
            otherTitle = otherTitle.capitalize()
            if (otherTitle=="skip"):
                print("skip")
            elif (otherTitle=="exit"):
                  exit(0)
            else:
                description = input("description: ")
                categoriesGroup = printCategoriesGroup()
                categories = ""
                categories = input("categories: ")
                if (categories=="0"):
                    addNewCategory()
                    categoriesGroup = printCategoriesGroup()
                    categories = input("categories: ")
                categories = categories.replace(" ", "")
                categoriesindex = categories.split(",")
                categorieslist = []
                for x in categoriesindex:
                    category = categoriesGroup[int(x)]
                    categorieslist.append(category)
                titleJson = {"title": title, "otherTitle": otherTitle, "description": description, "categories": categorieslist}
                data[data.index(group)]["names"][titles.index(title)] = titleJson

                saveData("stories.json", data)

