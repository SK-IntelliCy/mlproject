import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project="ml_project"
list_of_file =[
   f"src/{project}/__init__.py",
   f"src/{project}/components/__init__",
   f"src/{project}/components/data_ingestion.py",
   f"src/{project}/components/data_transformation.py",
   f"src/{project}/components/model_trainer.py",
   f"src/{project}/components/model_monitering.py",
   f"src/{project}/pipelines/__init__",
   f"src/{project}/pipelines/training_pipeline",
   f"src/{project}/pipelines/prediction_pipeline",
   f"src/{project}/exception.py",
   f"src/{project}/logger.py",
   f"src/{project}/utils.py",
   "app.py",
   "dockerfile",
   "requirements.txt",
   "setup.py"
]
for f in list_of_file:
    f_path=Path(f)
    f_dir,f_name=os.path.split(f_path)

    if f_dir!="":
        os.makedirs(f_dir,exist_ok=True)
        logging.info(f"creating directory :{f_dir} for {f_name}  ")
    if (not os.path.exists(f_path)or (os.path.getsize(f_path)==0)):
        with open(f_path,"w") as o:
            pass
        logging.info(f"creating empty {f_name}")
    else:
        logging.info(f"{f_name} already existst")        