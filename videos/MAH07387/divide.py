import subprocess

filename = "MAH07387.MP4"
command = "ffmpeg -i "+filename+"  -c copy -map 0 -segment_time 60  -f segment %03d_"+filename
subprocess.call(command, shell=True)
