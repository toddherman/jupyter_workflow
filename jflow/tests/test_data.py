from jflow.data import get_data
import pandas as pd

def test_data():
    df = get_data()
    assert all(df.columns == ['East', 'West', 'Total'])
    assert isinstance(df.index, pd.DatetimeIndex)