import subprocess
from subprocess import check_output
import json

def updateIndexHtml(message):
    fileappend = open("../index.html", "a+")
    fileappend.write("<p>added " + message + "</p>")
    fileappend.close() 

def resize(folder,filename, device, width, height):
    command = "identify -format " + "%wx%h "
    path = "./" + folder + "/" + filename
    p = subprocess.Popen(['identify', '-format', '%w', path], stdout=subprocess.PIPE)
    result = p.communicate()[0].decode("utf-8") 
    print (result)
    command = "convert "+path+" -resize " + str(width) + "x" + str(height) + "\! "+folder+"/icon-" + str(width)+"x"+str(height)+".png"
    print(command)
    subprocess.call(command, shell=True)
    p = subprocess.Popen(['identify', '-format', '%wx%h', path], stdout=subprocess.PIPE)
    result = p.communicate()[0].decode("utf-8") 
    print ("added icons for " + result)
    updateIndexHtml(path)

def getSizes():
   f = open ("sizes.json")
   string = f.read()
   jsondata = json.loads(string)["items"]
   return jsondata


   
sizes = getSizes()
folder = input("folder: ")
filename = "icon.png"
for items in sizes:
 for device in items:
    for dimension in items[device]:
        width = dimension["width"]
        height = dimension["height"]
        print(width)
        print(height)   
        resize(folder, filename, device, width, height)
