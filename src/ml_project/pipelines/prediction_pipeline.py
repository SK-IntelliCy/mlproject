import sys
import pandas as pd 
from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
from src.ml_project.utils import load_object

class predict_pipeline:
    def __init__(self):
        pass
    def predict(self,feature):
        try:
            model_path='artifacts\model.pkl'
            preprocer_path='artifacts\preprocer.pkl'
            preprocer=load_object(file_path=preprocer_path)
            model=load_object(file_path=model_path)
            Transf_Data=preprocer.transform(feature)
            predic=model.predict(Transf_Data)
            return predic
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,
        gender : str,
        hypertension :int,
        heart_disease:int,
        ever_married: str,
        work_type :str,
        Residence_type :str,
        smoking_status :str,
        avg_glucose_level :int,
        age:int,
        bmi:int,):
        self.gender=gender
        self.hypertension=hypertension
        self.heart_disease=heart_disease
        self.ever_married=ever_married
        self.work_type=work_type
        self.Residence_type=Residence_type
        self.smoking_status=smoking_status
        self.avg_gulucose_level=avg_glucose_level
        self.age=age
        self.bmi=bmi
    def Data_as_df(self):
        try:
            CustomDataInput={ "gender":[self.gender],
                          "hypertension":[self.hypertension],
                          "heart_disease":[self.heart_disease],
                          "ever_married":[self.ever_married],
                          'work_type':[self.work_type],
                          "Residence_type":[self.Residence_type],
                          "smoking_status":[self.smoking_status],
                          "avg_gulucose_level":[self.avg_gulucose_level],
                          "age":[self.age],
                          "bmi":[self.bmi]
                         }
            return pd.DataFrame(CustomDataInput)
        except Exception as e :
            raise CustomException(e,sys)
            
        
        