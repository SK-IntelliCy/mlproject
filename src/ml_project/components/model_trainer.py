import os,sys 
import numpy as np
from dataclasses import dataclass

from sklearn.ensemble import(
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree      import DecisionTreeClassifier
from xgboost import XGBClassifier

from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
from src.ml_project.utils import save_object, test_ml_algorithms

@dataclass
class trainerConfig:
    pickelf=os.path.join("artifacts","model.pkl")

class trainner:
    def __init__(self):
        self.Pf=trainerConfig().pickelf

    def initiate_MT(self,t_array,te_array):
        try:
            logging.info("Spliting input and output")
            x_t,y_t,x_te,y_te=(
                t_array[:,:-1],
                t_array[:,-1],
                te_array[:,:-1],
                te_array[:,-1]
            )
            models={
                "Random Forest" : RandomForestClassifier(),
                "Gradient Boost":GradientBoostingClassifier(),
                "logistic R"    :LogisticRegression(),
                "Nave Bayes"    :GaussianNB(),
                "Kneig"         :KNeighborsClassifier(),
                "xg Boost"      :XGBClassifier(),
                "Decision Tree" :DecisionTreeClassifier(),
                "Ada Boost"     :AdaBoostClassifier(),
                   }
            param_grid = {                   
                         "Random Forest":{
                                             # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                                              # 'max_features':['sqrt','log2',None],
                                             'n_estimators': [8,16,32,64,128,256]
                                         },
                         "Gradient Boost":{ 
                                             'n_estimators': [50, 100, 200],
                                             'learning_rate': [0.01, 0.1, 0.2],
                                             'max_depth': [3, 5, 7],
                                             },
                         "logistic R"    : {
                                             'penalty' : ['l1', 'l2', 'elasticnet', 'none'],
                                             'C' : np.logspace(-4, 4, 20),
                                             'solver' : ['lbfgs','newton-cg','liblinear','sag','saga']
                                             },
                          "Nave Bayes"   : {
                                              'var_smoothing': [1e-2, 1e-3, 1e-5, 1e-6, 1e-7, 1e-9, 1e-10, 1e-11, 1e-13, 1e-15]
                                            },
                          "Kneig"        : {
                                             'n_neighbors' : [5,7,9,11,13,15],
                                             'weights' : ['uniform','distance'],
                                             'metric' : ['minkowski','euclidean','manhattan']               
                                           },
                          "xg Boost"     : {
                                             'learning_rate' :[0.01,0.1,0.05],
                                             'n_estimators': [50, 100, 200]
                                           },    
                          "Decision Tree" :{
                                             'criterion':['log_loss', 'gini', 'entropy'],
                                           },      
                          "Ada Boost"     :{
                                             'n_estimators' : [50, 70, 90, 120, 180, 200],
                                             'learning_rate' : [0.001, 0.01, 0.1, 1, 10]
                                             },                                                     
                         }
            best_model_info= test_ml_algorithms(algorithms=models,X_train=x_t,y_train=y_t,X_test=x_te,y_test=y_te,hyperparameter_grids=param_grid)
            best_model_ji=best_model_info['model']
            best_model_name=best_model_info['model name']
            best_test_score=best_model_info['test_score']
            logging.info(f"{best_model_name} is best model with acurarcy {best_test_score}")

            model_names=list(param_grid.keys())
            actual_model=""
            for model in model_names:
                if best_model_name==model:
                    actual_model=actual_model+model
            params=param_grid[actual_model]  

             #mlflow
                
            save_object(
                f=best_model_ji,
                f_path=self.Pf
            )
            score=accuracy_score(y_te,best_model_ji.predict(x_te))
            return (score)
        except Exception as e :
            raise CustomException(e,sys)    