import os
import shutil

files = os.listdir(r"C:\Users\giova\Documents\assets\egw")

def createFolder(folder):
  source_folder = os.path.join(r"C:\Users\giova\Documents\assets\egw", folder)
  isExist = os.path.exists(source_folder)
  if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(source_folder)
   print("The new directory is created!")

def copyFile(src, dst):
   shutil.copyfile(src, dst)
  
for f in files:
  try:
    namesplit = f.split("_")#"book_TttC_id_9998.json'"
    folder = namesplit[1]
    createFolder(folder)
    print(folder)
    src = os.path.join(r"C:\Users\giova\Documents\assets\egw", f)
    dst = os.path.join(r"C:\Users\giova\Documents\assets\egw", folder, f)
    print(src)
    print(dst)
    copyFile(src, dst)
    
  except Exception as e:
    print(e)