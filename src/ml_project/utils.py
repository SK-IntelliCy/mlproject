import os,sys
from src.ml_project.exception import CustomException
from src.ml_project.logger    import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql
import pickle
import time
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

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
    

import time
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

def test_ml_algorithms(algorithms, hyperparameter_grids, X_train, y_train, X_test, y_test, cv=2):
    results = {}
    best_model_name = None
    best_test_score = float('-inf')  # Initialize with negative infinity

    for algorithm_name, algorithm in algorithms.items():
        start_time = time.time()

        # Check if hyperparameter grid is provided
        if algorithm_name not in hyperparameter_grids:
            print(f"Warning: No hyperparameter grid provided for {algorithm_name}. Using default parameters.")
            hyperparameter_grid = {}
        else:
            # Create the hyperparameter grid as a list of dictionaries (corrected)
            hyperparameter_grid = [
                {key: value for key, value in hyperparameter_grids[algorithm_name].items()}
            ]  # Convert dict to list containing a single dict
            

        # Choose appropriate hyperparameter tuning method (GridSearchCV or RandomizedSearchCV)
        search_method = GridSearchCV if len(hyperparameter_grid) > 0 else RandomizedSearchCV

        # Create and fit the search object
        search = search_method(estimator=algorithm, param_grid=hyperparameter_grid, scoring='accuracy', cv=cv)
        search.fit(X_train, y_train)

        # Extract results
        best_model = search.best_estimator_
        best_params = search.best_params_
        train_score = search.cv_results_['mean_test_score'][search.best_index_]

        # **Use X_test and y_test for final evaluation**
        test_score = accuracy_score( y_test,search.predict(X_test))  # Or any other desired metric

        if test_score > best_test_score:  # Update best model if current score is higher
            best_model_name = algorithm_name
            best_test_score = test_score
            best_model_ji=best_model
            fit_time_ji = time.time() - start_time

            best_model_info = {  # Create a dictionary to store best model information
            'model name':best_model_name,    
            'model': best_model_ji,
            'test_score': best_test_score,
            'fit_time': fit_time_ji
        }

        fit_time = time.time() - start_time
        results[algorithm_name] = {
                'model': best_model,
                'params': best_params,
                'train_score': train_score,
                'test_score': test_score,
                'fit_time': fit_time
            }   

    return best_model_info  # Return results dictionary and a tuple with best model information

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
