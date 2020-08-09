import subprocess
import json
import os
arr = os.listdir("../story/articles")

folder = input("folder: " )
print(arr)
articlejson = input("story json filename:")

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

slidenumber = 0


while True:
    print("slide number:" + str(slidenumber))
    jsondata = getSlides()
    slides = jsondata["slides"]
    print(slides[slidenumber]["text"])
    print(slides[slidenumber]["image"])
    subprocess.call("ls " + folder, shell=True)
    url = input("url: " )
    if url=="skip":
       print("skip")
       slidenumber = slidenumber + 1
    else:
      filename = input("filename: " )   
      updateImage(jsondata, slidenumber, filename)
      path = "./"+folder+"/"+filename
      command = "curl -L " + url + " -o " + path
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
         slidenumber = slidenumber + 1



