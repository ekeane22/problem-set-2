'''
PART 1: ETL the two datasets and save each in `data/` as .csv's
'''

import pandas as pd
from pathlib import Path
#import requests  

pred_universe_raw = pd.read_csv('https://www.dropbox.com/scl/fi/69syqjo6pfrt9123rubio/universe_lab6.feather?rlkey=h2gt4o6z9r5649wo6h6ud6dce&dl=1')
arrest_events_raw = pd.read_csv('https://www.dropbox.com/scl/fi/wv9kthwbj4ahzli3edrd7/arrest_events_lab6.feather?rlkey=mhxozpazqjgmo6qqahc2vd0xp&dl=1')
pred_universe_raw['arrest_date_univ'] = pd.to_datetime(pred_universe_raw.filing_date)
arrest_events_raw['arrest_date_event'] = pd.to_datetime(arrest_events_raw.filing_date)
pred_universe_raw.drop(columns=['filing_date'], inplace=True)
arrest_events_raw.drop(columns=['filing_date'], inplace=True)


data_directory = Path('/Users/erinkeane/Desktop/414 Problem-set-2/problem-set-2/data')

pred_universe_raw.to_csv(data_directory / 'pred_universe_raw.csv', index=False)
arrest_events_raw.to_csv(data_directory / 'arrest_events_raw.csv', index=False)


# Save both data frames to `data/` -> 'pred_universe_raw.csv', 'arrest_events_raw.csv'

'''
wtf is this: File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py", line 1351, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)>
'''


'''
openssl@3 is already up to date, it says to do this instead: 

import pandas as pd 
import requests 
from pathlib import Path 

def read(): 
pred_universe_raw = pd.read_csv('https://www.dropbox.com/scl/fi/69syqjo6pfrt9123rubio/universe_lab6.feather?rlkey=h2gt4o6z9r5649wo6h6ud6dce&dl=1')
arrest_events_raw = pd.read_csv('https://www.dropbox.com/scl/fi/wv9kthwbj4ahzli3edrd7/arrest_events_lab6.feather?rlkey=mhxozpazqjgmo6qqahc2vd0xp&dl=1')

#create data directory if it doesnt exist
cant i do this in my terminal?

data_directory = Path('data')
data_directory.mkdir(parents=True, exist_ok=True)


 # Paths to save the fetched data -- wtf is that 
    path_universe = data_directory / 'universe_lab6.feather'
    path_arrest = data_directory / 'arrest_events_lab6.feather'

#it told me to disable ssl verification 
pred_uni = requests.get(pred_universe_raw, verify=False)
arrest_events = requests.get(arrest_events_raw, verify=False)

note: i have the same error as i did with the last lab, can not get the error to go away. 
'''
