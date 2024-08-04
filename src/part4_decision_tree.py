'''
PART 4: Decision Trees
- Read in the dataframe(s) from PART 3
- Create a parameter grid called `param_grid_dt` containing three values for tree depth. (Note C has to be greater than zero) 
- Initialize the Decision Tree model. Assign this to a variable called `dt_model`. 
- Initialize the GridSearchCV using the logistic regression model you initialized and parameter grid you created. Do 5 fold crossvalidation. Assign this to a variable called `gs_cv_dt`. 
- Run the model 
- What was the optimal value for max_depth?  Did it have the most or least regularization? Or in the middle? 
- Now predict for the test set. Name this column `pred_dt` 
- Return dataframe(s) for use in main.py for PART 5; if you can't figure this out, save as .csv('s) in `data/` and read into PART 5 in main.py
'''

# Import any further packages you may need for PART 4
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import StratifiedKFold as KFold_strat
from sklearn.tree import DecisionTreeClassifier as DTC

from pathlib import Path


data_directory = Path('../data')

def load_from_3(): 
    '''
    Loading data from the data directory as csv files.
    Reads the csv as pandas dataframes. 
    
   Returns: 
        df_3: dataframe from part 3. 
         
    '''
    df_3 = pd.read_csv(data_directory / 'df_3.csv')
    
    return df_3


def gridl(): 
    '''
    Instantializes the GridSearchCV for the decision tree with a parameter grid for the max_depth. 
    
    Returns: 
        GridSearchCV: instance for decision tree. 
    
    '''
    param_grid_dt = {"max_depth": [3,7,15]}
    dt_model = DTC()
    #i figured out this row from the GridSearchCv hyperlink from importing it 
    gs_cv_dt = GridSearchCV(estimator=dt_model, param_gride=param_grid_dt, cv=5)
    
    return gs_cv_dt 

def run_grid(gs_cv_dt, X_train, y_train): 
    '''
    This function is supposed to run the GridSearchCv for the Decision Tree. 
    
    Parameters: 
        gs_cv_dt (GridSeaerchCV): GridSearchCV instance for the Decision Tree.
        X_train (df): training feature data.
        y_train (series): training target data 
        
    Returns: 
        GridSearchCV
    
    '''
    gs_cv_dt.fit(X_train, y_train)
    return gs_cv_dt



#the dataframe from this section will hypothetically be called df_4



