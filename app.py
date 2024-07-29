from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import sys
from src.ml_project.components.data_ingestion import DataIngention
from src.ml_project.components.data_ingestion import DataIngentionConfig
from src.ml_project.components.data_transformation import dataTransformationConfig
from src.ml_project.components.data_transformation import dataTrans
from src.ml_project.components.model_trainer import trainner, trainerConfig
import os

if __name__=="__main__":
    logging.info("started")

    try :
        DIC=DataIngentionConfig()
        DI=DataIngention()
        DI.IniitiateData()
    except Exception as e:
        logging.info("CUSTOM EXCEPTION")
        raise CustomException(e,sys)
#     try:
#         # dtc=dataTransformationConfig()
#         t=os.path.join("artifacts","train.csv")
#         te=os.path.join("artifacts","test.csv")
#         dt=dataTrans()
#         train_array,test_array,pre_processor=dt.iniate(t,te)

#         print(trainner().initiate_MT(t_array=train_array,te_array=test_array))

#     except Exception as e:
#         raise CustomException(e,sys)



# from flask import Flask,render_template,request
# import numpy as np
# import pandas as pd 
# from sklearn.preprocessing import StandardScaler
# from src.ml_project.pipelines.prediction_pipeline import CustomData,predict_pipeline
# aplication=Flask(__name__)
# app=aplication

# @app.route("/")
# def Home_p():
#     return render_template('index.html')

# @app.route("/predict",methods=['GET','POST'])
# def predict():
#     if request.method=="GET":
#        return render_template('collect.html')
#     elif request.method=='POST':
#         data = CustomData(
#                           gender=request.form.get('gender'),
#                           hypertension=float(request.form.get('hypertension')),
#                           heart_disease=float(request.form.get('heart_disease')),
#                           ever_married=request.form.get('ever_married'),
#                           work_type=request.form.get('work_type'),
#                           Residence_type=request.form.get('Residence_type'),
#                           smoking_status=request.form.get('smoking_status'),
#                           age=float(request.form.get('age')),
#                           bmi=float(request.form.get('bmi')),
#                           avg_glucose_level=float(request.form.get('avg_glucose_level')),
#                           )
                          
#         pred_df=data.Data_as_df()
#         predic_pipeline=predict_pipeline()
#         results=predic_pipeline.predict(pred_df)
#         return render_template('collect.html',results=results[0])
# if __name__=="__main__":
#     app.run(debug=True)   