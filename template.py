import os
from pathlib import Path        #we can handle below given windows path with this command
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = 'cnnClassifier'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)                          #we can handle path with this command
    filedir,filename = os.path.split(filepath)         #this return file directory and file in form of tuple-->>()

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass                                       #creating an empty file only
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
        