import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import os

from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
from src.ml_project.utils import save_object


@dataclass
class dataTransformationConfig:
    prefile=os.path.join("artifacts","preprocer.pkl")

class dataTrans:
    def __init__(self):
        self.DTC=dataTransformationConfig()

    def get_transformer_object(self):
        try:
           raw=pd.read_csv(os.path.join("artifacts","raw.csv"))
           numC=['id', 'age', 'hypertension', 'heart_disease', 'avg_glucose_level','bmi']
           catC=['gender', 'ever_married', 'work_type', 'Residence_type','smoking_status']
           numpipeline=Pipeline(steps=[
               ("imputer",SimpleImputer(strategy="mean")),
               ("scaller",StandardScaler())
           ])
           cattpipeline=Pipeline(steps=[
               ("imputer",SimpleImputer(strategy="most_frequent")),
               ("OHE",OneHotEncoder()),
               ("scaler",StandardScaler(with_mean=False))
           ])
           logging.info(f"numerical columns")
           logging.info(f"catagorical columns")

           preprocessor=ColumnTransformer(
           [("num_pipeline",numpipeline,numC),
            ("cateogorical_pipeline",cattpipeline,catC)
           ])
           return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    def iniate(self,t_P,te_p):
        try:
            train=pd.read_csv(t_P)
            test=pd.read_csv(te_p)
            logging.info("Reading Train and test file")

            pobj=self.get_transformer_object()
            tcolum=["stroke"]

            x_t=train.drop(tcolum,axis=1)
            y_t=train[tcolum]

            x_te=test.drop(tcolum,axis=1)
            y_te=test[tcolum]

            logging.info("Aplying Preprocessing")
            x_t_array=pobj.fit_transform(x_t)
            x_te_array=pobj.transform(x_te)

            train_array=np.c_[x_t_array,np.array(y_t)]
            test_array=np.c_[x_te_array,np.array(y_te)]

            logging.info("Saved preprorecissing array")
            save_object(f=pobj,f_path=self.DTC.prefile)
            return (train_array,
                    test_array,
                    self.DTC.prefile
                    )



        except Exception as e:
            raise CustomException(e,sys)    