import subprocess
from subprocess import check_output
import os



def resize(folder, filename):
    filepath = "./" + folder + "/" + filename
    command = "identify -format " + "%wx%h "
    p = subprocess.Popen(['identify', '-format', '%w', filepath], stdout=subprocess.PIPE)
    result = p.communicate()[0].decode("utf-8") 
    print (result)
    width = 710
    height = 400
    command = "convert "+filepath+" -resize " + str(width) + "x" + str(height) + "\! " + filepath
    print(command)
    subprocess.call(command, shell=True)
    p = subprocess.Popen(['identify', '-format', '%wx%h', filepath], stdout=subprocess.PIPE)
    result = p.communicate()[0].decode("utf-8") 
    print ("new size: " + result)

folder = input("folder: ")
arr = os.listdir(folder)
for x in arr:
   if x.endswith("png") or x.endswith("jpg") or x.endswith("jpeg"):
     resize(folder, x)
