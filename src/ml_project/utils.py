import os,sys
from src.ml_project.exception import CustomException
from src.ml_project.logger    import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql
import pickle
import numpy as np

load_dotenv()
host     =os.getenv("host")
user     =os.getenv("user")
password =os.getenv("password")
db       =os.getenv("db")

def read_sql():
    logging.info("Reading data started")
    try:
        mydb=pymysql.connect(
            host="localhost",
            user="root",
            password="SKji@119",
            db="health",
        )
        logging.info("conection established", mydb)
        df=pd.read_sql_query("SELECT * FROM `healthcare-dataset-stroke-data`;",mydb)
        return (df)
    except Exception as e:
        raise CustomException(e,sys)

def save_object(f,f_path):
    try:
       dir_path=os.path.dirname(f_path)
       os.makedirs(dir_path,exist_ok=True)
       with open(f_path,"wb") as a:
           pickle.dump(f,a)
    except Exception as e:   
        raise CustomException(e,sys)
