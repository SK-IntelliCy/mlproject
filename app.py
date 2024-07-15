from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import sys
from src.ml_project.components.data_ingestion import DataIngention
from src.ml_project.components.data_ingestion import DataIngentionConfig

if __name__=="__main__":
    logging.info("started")

    try :
        DIC=DataIngentionConfig()
        DI=DataIngention()
        DI.IniitiateData()
    except Exception as e:
        logging.info("CUSTOM EXCEPTION")
        raise CustomException(e,sys)
