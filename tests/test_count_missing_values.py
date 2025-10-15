import sys
import math

from data_analysis.count_missing_values import count_missing_values


def test_list_of_lists():
    data = [
        [1, None, 3],
        [None, 2, float('nan')],
        [3, 4, 5],
    ]
    result = count_missing_values(data)
    assert result == {0: 1, 1: 1, 2: 1}


def test_list_of_dicts():
    data = [
        {'A': 1, 'B': None},
        {'A': None, 'B': 2},
        {'A': 3, 'B': 4},
    ]
    result = count_missing_values(data)
    assert result == {'A': 1, 'B': 1}


def test_pandas_dataframe():
    try:
        import pandas as pd
    except Exception:
        # skip pandas-specific assert if pandas not available
        return
    df = pd.DataFrame({
        'A': [1, None, 3],
        'B': [None, 2, 3],
    })
    result = count_missing_values(df)
    assert result == {'A': 1, 'B': 1}
