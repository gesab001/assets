import subprocess
import json

url = input("youtube url: ")
title = input("title: ")
preacher = input("preacher: ")
filename = title.lower().replace(" ", "_") + "_" + preacher.lower().replace(" ", "_") + ".mp3"
command = "youtube-dl -x --audio-format mp3 --write-info-json --write-thumbnail --audio-quality 9 --embed-thumbnail " + url + " -o " + filename
subprocess.call(command, shell=True)

infofile = open(filename+".info.json")
infodata = json.load(infofile)
fileopen = open("sermons.json")
jsondata = json.load(fileopen)
jsonobj = {"title": title, "preacher": preacher, "filename": filename, "info": infodata, "thumbnail": filename+".jpg"}

if jsonobj not in jsondata["items"]:
 jsondata["items"].append(jsonobj)
 with open("sermons.json", "w") as outfile:
  json.dump(jsondata, outfile, indent=4)
