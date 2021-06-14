import subprocess
import json
import os


arr = os.listdir("../story/articles")
arr.sort()


arrindex = 0
articlejson = 0
folder = ""

def printArticleList():
	for x in range(0, len(arr)):
		print(str(x+1) + ". " + arr[x])
	
def resize(filename):
    command = "identify -format " + "%wx%h "
    p = subprocess.Popen(['identify', '-format', '%w', filename], stdout=subprocess.PIPE)
    result = p.communicate()[0].decode("utf-8") 
    print (result)
    width = 710
    height = 400
    command = "convert "+filename+" -resize " + str(width) + "x" + str(height) + "\! " + filename
    print(command)
    subprocess.call(command, shell=True)
    p = subprocess.Popen(['identify', '-format', '%wx%h', filename], stdout=subprocess.PIPE)
    result = p.communicate()[0].decode("utf-8") 
    print ("new size: " + result)

def resizePoster(filename):
    command = "identify -format " + "%wx%h "
    p = subprocess.Popen(['identify', '-format', '%w', filename], stdout=subprocess.PIPE)
    result = p.communicate()[0].decode("utf-8") 
    print (result)
    width = 400
    height = 710
    command = "convert "+filename+" -resize " + str(width) + "x" + str(height) + "\! " + filename
    print(command)
    subprocess.call(command, shell=True)
    p = subprocess.Popen(['identify', '-format', '%wx%h', filename], stdout=subprocess.PIPE)
    result = p.communicate()[0].decode("utf-8") 
    print ("new size: " + result)

def updateIndexHtml(message):
    fileappend = open("../index.html", "a+")
    fileappend.write("<p>added " + message + "</p>")
    fileappend.close() 

def updateImage():
    f = open("../story/articles/"+articlejson)
    string = f.reads()
    jsondata = json.loads(string)

def getSlides():
    f = open("../story/articles/"+articlejson)
    string = f.read()
    jsondata = json.loads(string)
    f.close()

    return jsondata

def updateImage(jsondata, slidenumber, filename):
  jsondata["slides"][slidenumber]["image"] = "https://gesab001.github.io/assets/images/"+folder+"/"+filename
  print(jsondata["slides"][slidenumber]["image"])  
  with open("../story/articles/"+articlejson, "w") as outfile:
        json.dump(jsondata, outfile, indent=4)

def downloadImage(url, path):
	command = "curl -L " + url + " --output " + path
	subprocess.call(command, shell=True)
	proc = subprocess.Popen(["curl", "-L", url, "-o", path],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	proc.wait()
	(stdout, stderr) = proc.communicate()

	if proc.returncode != 0:
	 print(stderr)
	else:
	 print("success")
	 resize(path) 
	 updateIndexHtml(path)
	 displayImage(path)
	 

def displayImage(path):
	command = "display " + path
	subprocess.call(command, shell=True)	 

def updatePoster():
	jsondata["poster"]= "https://gesab001.github.io/assets/images/"+folder+"/poster.jpg"
	with open("../story/articles/"+articlejson, "w") as outfile:
		json.dump(jsondata, outfile, indent=4)
        	
def downloadPoster(url, path):
	command = "curl -L " + url + " --output " + path
	subprocess.call(command, shell=True)
	proc = subprocess.Popen(["curl", "-L", url, "-o", path],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	proc.wait()
	(stdout, stderr) = proc.communicate()

	if proc.returncode != 0:
	 print(stderr)
	else:
	 print("success")
	 resizePoster(path) 
	 updateIndexHtml(path)
	 displayImage(path)
	 updatePoster()
	 	 


while True:
	printArticleList()
	arrindex = int(input("story json filename:"))
	articlejson = arr[arrindex-1]
	print(articlejson)
	foldertest = articlejson.split(".")
	foldertest = foldertest[0]
	foldertest = foldertest.replace("_", "")
	folder = foldertest.lower()
	folderexists = os.path.exists(folder)
	if folderexists==True:
		print("folder exists")
		print(folder)
	else:
		print("folder doesn't exist")
		print("creating a folder")
		command = "mkdir " + folder
		subprocess.call(command, shell=True)
		folderexists = os.path.exists(folder)
		if folderexists==True:
			print("folder created")
		
	jsondata = getSlides()
	slides = jsondata["slides"]
	try:
		print(jsondata["poster"])
		print("poster already exists")
		print("change this poster")
		url = input("poster url: ")
		path = "./"+folder+"/poster.jpg"
		downloadPoster(url, path)
	except:
		url = input("poster url: ")
		path = "./"+folder+"/poster.jpg"
		downloadPoster(url, path)
	
	
