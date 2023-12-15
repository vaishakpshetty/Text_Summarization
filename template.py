import os
from pathlib import Path
import logging        #to log all the information to keep an track


#creating logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Creating Project structure
project_name = "textsummarizer"

#all files required for project creation
files_list = [
    ".github/workflows/.gitkeep",                   #used when doing CI/CD deployment[Here we write CI/CD related yaml files automatic file]
    f"src/{project_name}/__init__.py",              #so whenver we commit our code it will automatically take our code from github and it will do the deployment in our cloud that is why .github is important       
    f"src/{project_name}/components/__init__.py",   #constructr files are important to use import local packages
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

#Looping through the list
for filepath in files_list:
    filepath = Path(filepath)                      # convert the path to specified operating system format(helps in handling the path)(it will detect the os we are using and based on that it will provide the path)
    filedir, filename = os.path.split(filepath)    # we need to split the filepath as it contains both folders and file cause first we need to create a folder and then files

    #if folder is empty then we are not creating any(folder creation)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if not os.path.exists(filepath) or (os.path.getsize(filepath) == 0):
        with open( filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filename}")      #only creates file if the file is empty,if it exits ot will ignore that file and create other file