'''
PART 2: Pre-processing
- Take the time to understand the data before proceeding
- Load `pred_universe_raw.csv` into a dataframe and `arrest_events_raw.csv` into a dataframe
- Perform a full outer join/merge on 'person_id' into a new dataframe called `df_arrests`
- Create a column in `df_arrests` called `y` which equals 1 if the person was arrested for a felony crime in the 365 days after their arrest date in `df_arrests`. 
- - So if a person was arrested on 2016-09-11, you would check to see if there was a felony arrest for that person between 2016-09-12 and 2017-09-11.
- - Use a print statment to print this question and its answer: What share of arrestees in the `df_arrests` table were rearrested for a felony crime in the next year?
- Create a predictive feature for `df_arrests` that is called `current_charge_felony` which will equal one if the current arrest was for a felony charge, and 0 otherwise. 
- - Use a print statment to print this question and its answer: What share of current charges are felonies?
- Create a predictive feature for `df_arrests` that is called `num_fel_arrests_last_year` which is the total number arrests in the one year prior to the current charge. 
- - So if someone was arrested on 2016-09-11, then you would check to see if there was a felony arrest for that person between 2015-09-11 and 2016-09-10.
- - Use a print statment to print this question and its answer: What is the average number of felony arrests in the last year?
- Print the mean of 'num_fel_arrests_last_year' -> pred_universe['num_fel_arrests_last_year'].mean()
- Print pred_universe.head()
- Return `df_arrests` for use in main.py for PART 3; if you can't figure this out, save as a .csv in `data/` and read into PART 3 in main.py
'''


# import the necessary packages
import pandas as pd
from datetime import datetime, timedelta ########turns a date string into a data object 
from pathlib import Path

# do i need to add all this: ?????? 
data_directory = Path('/Users/erinkeane/Desktop/414 Problem-set-2/problem-set-2/data')

def load(): 
    pred_universe_raw = pd.read_csv(data_directory / 'pred_universe_raw.csv')
    arrest_events_raw = pd.read_csv(data_directory / 'arrest_events_raw.csv')
    return pred_universe_raw, arrest_events_raw

def from_etl_to_dates(pred_universe_raw, arrest_events_raw):
    pred_universe_raw['arrest_date_univ'] = pd.to_datetime(pred_universe_raw['filing_date'])
    arrest_events_raw['arrest_date_event'] = pd.to_datetime(arrest_events_raw['filing_date'])
    pred_universe_raw.drop(columns=['filing_date'], inplace=True)
    arrest_events_raw.drop(columns=['filing_date'], inplace=True)
    return pred_universe_raw, arrest_events_raw 

def merge_and_prediction(pred_universe_raw, arrest_events_raw):
    df_arrests = pd.merge(pred_universe_raw, arrest_events_raw, on='person_id', how='outer')
    df_arrests['y'] = df_arrests.apply(lambda row: check_felony(row, arrest_events_raw), axis=1)
    
    
    #the predictive features 
    df_arrests['current_charge_felony'] = df_arrests['charge_type_event'].apply(lambda x: 1 if x == 'Felony' else 0)
    df_arrests['num_fel_arrests_last_year'] = df_arrests.apply(lambda row: num_fel_arrests_last_year(row, arrests_events_raw), axis=1)
    
    print_statistics(df_arrests)
    
    #df_arrests.to_csv(data_directory / 'df_arrests.csv', index=False)
    
    return df_arrests 

def find_felony(row, arrest_events_raw):
    



#OLD
#def check_felony(row): 
    #if (row['charge_type_event'] == 'Felony' and 
        #row['arrest_date_event'] > row['arrest_date_univ'] and 
        #row['arrest_date_event'] <= row ['arrest_date_univ'] + pd.Timedelta(days=365)):
        #return 1 
    #else: 
        #return 0 