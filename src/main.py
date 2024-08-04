'''
You will run this problem set from main.py, so set things up accordingly
'''
#from src import etl and so on and so on i think 
import pandas as pd
from pathlib import Path
import etl
import preprocessing
import logistic_regression
import decision_tree
import calibration_plot

data_directory = Path('../data') 

def main():
    '''
    If my functions did run, this is how I would imagine I would call them here. 
    
    '''
    # PART 1: Instanciate etl, saving the two datasets in `./data/`
pred_universe_raw = pd.read_csv(data_directory / 'pred_universe_raw.csv')
arrest_events_raw = pd.read_csv(data_directory / 'arrest_events_raw.csv')
    
    # PART 2: Call functions/instanciate objects from preprocessing
df_arrests = pd.read_csv(data_directory / 'df_arrests.csv')
'''
Here I would instantiate the objects from preprocessing. 
'''
    # PART 3: Call functions/instanciate objects from logistic_regression
df_3 = pd.read_csv(data_directory / 'df_3.csv')
'''
Here I would instantiate the objects from logistic_regression.
'''
    # PART 4: Call functions/instanciate objects from decision_tree
df_4 = pd.read_csv(data_directory / 'df_4.csv')
'''
Here I would instantiate the objects from the decision_tree.

'''
    # PART 5: Call functions/instanciate objects from calibration_plot
df_5 = pd.read_csv(data_directory / 'df_5.csv')
    
'''
Here I would call the calibration plot functions from part 5. 
'''

if __name__ == "__main__":
    main()