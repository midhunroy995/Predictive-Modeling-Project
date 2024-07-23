import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "HousePricePrediction"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/data/load_data.py",
    f"src/{project_name}/data/eda.py",
    f"src/{project_name}/preprocessing/__init__.py",
    f"src/{project_name}/preprocessing/preprocess.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/models/train_model.py",
    f"src/{project_name}/models/evaluate_model.py",
    f"src/{project_name}/visualization/__init__.py",
    f"src/{project_name}/visualization/visualize.py",
    "config/config.yaml",
    "requirements.txt",
    "setup.py",
    "notebooks/eda.ipynb",
    "notebooks/modeling.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
