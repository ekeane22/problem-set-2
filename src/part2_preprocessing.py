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

import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path


data_directory = Path('../data')

def load(): 
    '''
    Loading data from the data directory as csv files.
    Reads the csv as pandas dataframes. 
    
    Returns:
        tuple: contains two dataframes, pred_universe_raw and arrests_events_raw. 
         
    '''
    pred_universe_raw = pd.read_csv(data_directory / 'pred_universe_raw.csv')
    arrest_events_raw = pd.read_csv(data_directory / 'arrest_events_raw.csv')
    
    return pred_universe_raw, arrest_events_raw

def dates(pred_universe_raw, arrest_events_raw): 
    '''
    This converts two columns to datetime format. 
    
    Parameters: 
        pred_universe_raw (DF): contains predictive universe data.
        arrest_events_raw (DF): contains the arrest event data.
        
    Returns: 
        tuple: Contains the updated dataframes. 

    '''
    pred_universe_raw['arrest_date_univ'] = pd.to_datetime(pred_universe_raw['arrest_date_univ'])
    arrest_events_raw['arrest_date_event'] = pd.to_datetime(arrest_events_raw['arrest_date_event'])
    
    #pred_universe_raw['arrest_date_univ'] = pd.to_datetime(pred_universe_raw['filing_date'])
    #arrest_events_raw['arrest_date_event'] = pd.to_datetime(arrest_events_raw['filing_date'])
    return (pred_universe_raw, arrest_events_raw)
    
def merge(pred_universe_raw, arrest_events_raw):
    '''
    Completes a full outer join on "person_id" to create df_arrests.
    
    Parameters: 
        arrest_events_raw (df): contains predictive universe data.
        arrest_events_raw (DF): contains the arrest event data.
        
    Returns: 
        New dataframe: df_arrests. 
    '''
    df_arrests = pd.merge(pred_universe_raw, arrest_events_raw, on='person_id', how='outer')
    df_arrests.reset_index(drop=True, inplace=True)
    
    return df_arrests
  
def finding_felony(arrest_events_raw, row):
    '''
    Going through row by row to see if a person was re-arrested for a felony within a year (365 days) after their original arrest date.
    
    Parameters: 
        arrest_events_raw (df): contains the arrest event data.
        row (series): rows from df_arrests (the merged dataframe).
        
    Returns 
        int: 1 if the person was re-arrested for a felony within a year after their original arrest, otherwise 0. 
    '''
    person_id = row["person_id"]
    arrest_date_univ = row["arrest_date_univ"]
    
    first = arrest_date_univ + timedelta(days=1)
    year_later = arrest_date_univ + timedelta(days=365)
    
    search_for_felony = arrest_events_raw[
        (arrest_events_raw["person_id"] == person_id) &
        (arrest_events_raw["arrest_date_event"] >= first) &
        (arrest_events_raw["arrest_date_event"] <= year_later) &
        (arrest_events_raw["charge_degree"] == "felony")
    ]
    
    return 1 if not search_for_felony.empty else 0

def num_fel_arrests_last_year(row, arrest_events_raw): 
    '''
    Counts the number of arrests in the previous year to the persons current arrest. 
    
    Parameters: 
        arrest_events_raw (df): contains the arrest event data.
        row (series): rows from df_arrests (the merged dataframe).
        
    Returns 
        int: The number of felony arrests in the previous year before the current charge/arrest.
    
    '''
    person_id = row["person_id"]
    arrest_date_event = row["arrest_date_event"]
    min = arrest_date_event - timedelta(days=365)
    max = arrest_date_event
    
    last_year_fel = arrest_events_raw[arrest_events_raw
                    (arrest_events_raw["person_id"] == person_id) &
                    (arrest_events_raw["arrest_date_event"] >= min) & 
                    (arrest_events_raw["arrest_date_event"] < max) &
                    (arrest_events_raw["charge_degree"] == "felony") 
                ]
    return last_year_fel.shape[0]
  

def add_columns_and_fix(df_arrests, arrest_events_raw):
    '''
    Adding the necessary columns and printing the requirements. 
    
    Parameters: 
        df_arrests (DF): The merged dataframe. 
        arrest_events_raw (Df): Contains the arrest event data.
        
    Returns: 
        df_arrests(df): The updated dataframe with new information. 
    
    '''
    df_arrests["y"] = df_arrests.apply(lambda row: finding_felony(arrest_events_raw, row), axis=1)
    df_arrests["current_charge_felony"] = df_arrests["charge_degree"].apply(lambda x: 1 if x == 'felony' else 0)
    df_arrests["num_fel_arrests_last_year"] = df_arrests.apply(lambda row: num_fel_arrests_last_year(row, arrest_events_raw), axis=1)
    
    felony = df_arrests["y"].mean() * 100 
    current_felony = df_arrests["current_charge_felony"].mean() * 100 
    avg_felony = df_arrests["num_fel_arrests_last_year"].mean()
    
    print(f" What share of arrestees in the `df_arrests` table were rearrested for a felony crime in the next year? {felony:.2f}%")
    print(f"What share of current charges are felonies? {current_felony: .2f}%")
    print(f"What is the average number of felony arrests in the last year? {avg_felony:.2f} ")
    
    return df_arrests

def main(): 
    '''
    The main function for preprocessing. 
    
    '''
    arrest_events_raw, pred_universe_raw = load()
    arrest_events_raw, pred_universe_raw = dates(arrest_events_raw, pred_universe_raw)
    df_arrests = merge(arrest_events_raw, pred_universe_raw)
    df_arrests = add_columns_and_fix(df_arrests, arrest_events_raw)
    
    print(df_arrests.head())
    
    df_arrests.to_csv(data_directory / 'df_arrests.csv', index=False)
    
if __name__ == "__main__": 
    main()
    
