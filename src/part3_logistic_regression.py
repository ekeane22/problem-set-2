'''
PART 3: Logistic Regression
- Read in `df_arrests`
- Use train_test_split to create two dataframes from `df_arrests`, the first is called `df_arrests_train` and the second is called `df_arrests_test`. Set test_size to 0.3, shuffle to be True. Stratify by the outcome  
- Create a list called `features` which contains our two feature names: pred_universe, num_fel_arrests_last_year
- Create a parameter grid called `param_grid` containing three values for the C hyperparameter. (Note C has to be greater than zero) 
- Initialize the Logistic Regression model with a variable called `lr_model` 
- Initialize the GridSearchCV using the logistic regression model you initialized and parameter grid you created. Do 5 fold crossvalidation. Assign this to a variable called `gs_cv` 
- Run the model 
- What was the optimal value for C? Did it have the most or least regularization? Or in the middle? Print these questions and your answers. 
- Now predict for the test set. Name this column `pred_lr`
- Return dataframe(s) for use in main.py for PART 4 and PART 5; if you can't figure this out, save as .csv('s) in `data/` and read into PART 4 and PART 5 in main.py
'''

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib as plt 
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import StratifiedKFold as KFold_strat
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression as lr

data_directory = Path('../data') 

def load_from_2(): 
    '''
    Loading the df_arrests csv from the data directory. 
    
    Returns: 
        DF: the pandas dataframe from part 2 called df_arrests.
    
    '''
    df_arrests = pd.read_csv(data_directory / 'df_arrests.csv')
    return df_arrests

def split(df_arrests): 
    '''
    Splitting the df_arrests dataframe into a training and testing set. 
    
    Args:
        df_arrests (dataframe); The dataframe from part 2 containing arrest data. 
        
    Returns: 
        tuple: Which contains: X_train, X_test, y_train, y_test
    
    '''
    feature = ["pred_universe", "num_fel_arrests_last_year"]
    target = "outcome"
    
    X = df_arrests[feature]
    y = df_arrests[target]
    
    X_train, X_test, y_test, y_train = train_test_split(
        X, y, test_size=0.3, shuffle=True, stratify=y)
    
    df_arrests_train = X_train.copy()
    df_arrests_train(target) = y_train
    
    
    Return X_train, X_test, y_test, y_train
    
def train(X_train, y_train):
    '''
    Training the regression model with grid seaerch.
    
    Args: 
        X_train (df): training features
        y_train (series): training target 
        
    Returns: 
        DF: An updated dataframe. 
    
    '''
    param_grid = {"C": [2, 4, 6, 8, 10, 12]}
    lr_model = lr
    gs_cv = GridSearchCV(lr_model, param_grid, cv=5, scoring="accuracy")

    gs_cv.fit(X_train, y_train)
    
    return gs_cv

def running_the_model(gs_cv, X_test, y_test):
    '''
    The goal of this function is to run the model and return a new/updated dataframe with 
    
    Args
        gs_cv (GridSearchCV): updated dataframe 
        X_train (df): training features
        y_train (series): training target 
        
    Returns: 
        Dataframe: A new dataframe with predictions 
    '''
    #Print(f" The optional value for C is: ")

#return df_3

def main(): 
    '''
    This would be the main function if everything worked. 
    
    '''
    df_arrests = load_from_2()
    X_train, X_test, y_train, y_test = split(df_arrests)
    df_3 = running_the_model(gs_cv, X_test, y_test)
    
    df_3.to_csv(data_directory / 'df_3.csv', index=False)
    
    if __name__ == "__main__":
        main()

