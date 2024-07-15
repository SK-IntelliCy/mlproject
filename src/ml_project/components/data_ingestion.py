import os,sys

from src.ml_project.exception import CustomException
from src.ml_project.logger    import logging
import pandas as pd 
from dataclasses import dataclass
from src.ml_project.utils import read_sql
from sklearn.model_selection import train_test_split

@dataclass
class DataIngentionConfig:
    train_d_p:str=os.path.join("artifacts","train.csv")
    test_d_p:str=os.path.join("artifacts","test.csv")
    raw_d_p:str=os.path.join("artifacts","raw.csv")

class DataIngention:
    def __init__(self):
        self.IngentionConfig=DataIngentionConfig()

    def IniitiateData(self):
        try:
            df=read_sql()
            logging.info("Reading compleated")
            os.makedirs(os.path.dirname( self.IngentionConfig.raw_d_p),exist_ok=True)
            df.to_csv(self.IngentionConfig.raw_d_p,index=False,header=True) 
            t_d,te_d=train_test_split(df,test_size=0.2,random_state=37)
            te_d.to_csv(self.IngentionConfig.test_d_p,index=False,header=True) 
            t_d.to_csv(self.IngentionConfig.train_d_p,index=False,header=True)
            logging.info("DATA INGESTION COMPLETE")
            return (
                self.IngentionConfig.test_d_p,
                self.IngentionConfig.train_d_p
            )

        except Exception as e:
            raise CustomException(e,sys)       
