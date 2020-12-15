import subprocess

folder = input("folder: " )

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

while True:
    url = input("url: " )
    filename = input("filename: " )
    if filename=="cancel":
        break
    path = "./"+folder+"/"+filename
    command = "curl -L " + url + " -o " + path
    subprocess.call(command, shell=True)
    resize(path) 
    updateIndexHtml(path)   



