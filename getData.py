import configparser
from pathlib import Path
import os


config = configparser.ConfigParser(inline_comment_prefixes=(';', '#'))
config.read("config.ini")
d_path = config["general"]["downloaded_path"]
dst_path = config["general"]["path"]

path = Path(d_path)
copy_path = Path(dst_path)

search = "*.json"
for file in path.rglob(search):
    if "character-json.json" in file.name:

        srcpath = str(path) + "/character-json.json"
        srcpath = Path(srcpath)

        try:
            with open(srcpath,"rb") as src, open(copy_path,"wb") as dst:
                dst.write(src.read())
                print("File written successfully!")
            
            os.remove(srcpath)
                
        except:
            print("!!!Check Formatting")