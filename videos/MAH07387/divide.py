import subprocess
import os

arr = os.listdir()

filename = ""
for x in arr:
  if x.lower().endswith(".mp4"):
     filename = x
command = "ffmpeg -i "+filename+"  -c copy -map 0 -segment_time 60  -f segment %03d_"+filename
subprocess.call(command, shell=True)
