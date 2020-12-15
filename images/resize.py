import subprocess
from subprocess import check_output

def updateIndexHtml(message):
    fileappend = open("../index.html", "a+")
    fileappend.write("<p>added " + message + "</p>")
    fileappend.close() 

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
    updateIndexHtml(filename)




folder = input("folder: ")
filename = input("filename: ")
path = "./" + folder + "/" + filename
resize(path)
