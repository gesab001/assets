import subprocess

url = input("url:")
output = input("filename:")
subprocess.call("youtube-dl -x --audio-format mp3 "+ url +" --output "+output+".mp3", shell=True)
