from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import sys
from src.ml_project.components.data_ingestion import DataIngention
from src.ml_project.components.data_ingestion import DataIngentionConfig
from src.ml_project.components.data_transformation import dataTransformationConfig
from src.ml_project.components.data_transformation import dataTrans
import os

if __name__=="__main__":
    logging.info("started")

    # try :
    #     DIC=DataIngentionConfig()
    #     DI=DataIngention()
    #     DI.IniitiateData()
    # except Exception as e:
    #     logging.info("CUSTOM EXCEPTION")
    #     raise CustomException(e,sys)
    try:
        # dtc=dataTransformationConfig()
        t=os.path.join("artifacts","train.csv")
        te=os.path.join("artifacts","test.csv")
        dt=dataTrans()
        dt.iniate(t,te)

    except Exception as e:
        raise CustomException(e,sys)
