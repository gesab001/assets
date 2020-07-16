import subprocess

url = input("url: " )
filename = input("filename: " )
command = "curl -L " + url + " -o " + filename
subprocess.call(command, shell=True)
