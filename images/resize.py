import subprocess
from subprocess import check_output

filename = input("filename: ")
command = "identify -format " + "%wx%h "
p = subprocess.Popen(['identify', '-format', '%w', filename], stdout=subprocess.PIPE)
result = p.communicate()[0].decode("utf-8") 
print (result)
width = int(result)
height = round(width / 1.78)
command = "convert "+filename+" -resize " + str(width) + "x" + str(height) + "\! " + filename
print(command)
subprocess.call(command, shell=True)
