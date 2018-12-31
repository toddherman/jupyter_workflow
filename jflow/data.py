import os
from urllib.request import urlretrieve
import pandas as pd

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

#only download if it isn't already here.
def get_data(filename='fremont.csv', url=URL, force_download=False):
    """ Download and cache the fremont data

    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data

    Returns
    -------
    data : pandas.DataFrame
        The fremont bridge data
    """
    
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, filename)
    df = pd.read_csv(filename, index_col='Date')
    # much faster to avoid parsing date in read, move it below with asserting the format.
    try:
        df.index = pd.to_datetime(df.index, format='%m/%d/%Y %I:%M:%S %p')
    except TypeError:
        df.index = pd.to_datetime(df.index)
    df.columns=['East', 'West'] #column names were verbose 
    df['Total'] = df['West'] + df['East']
    return df