'''
    This file is used to create a template for the project.
'''
import os
from pathlib import Path
import logging

# logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

PROJECT_NAME = 'textSummarization'

list_of_files = [
    ".github/workflows/",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    path = Path(file)
    file_dir, file_name = os.path.split(file)

    if file_dir != '' :
        os.makedirs(file_dir, exist_ok=True)
        logging.info("Created directory: %s", file_dir)

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0) :
        with open(file, 'w', encoding='utf-8') as f:
            logging.info("Created file: %s", file)

    else:
        logging.info("File already exists: %s", file)
