"""data_analysis.count_missing_values

Utility to count missing values per column.

The function prefers pandas DataFrame input but also accepts a sequence-of-sequences
or a list-of-dicts and will return a dict mapping column names (or indices) to
missing counts.
"""
from typing import Any, Dict, Iterable, List


try:
    import pandas as pd
except Exception:  # pragma: no cover - fallback path
    pd = None


def count_missing_values(df: Any) -> Dict[Any, int]:
    """Count missing values per column.

    Accepts:
    - pandas.DataFrame -> returns pandas.Series-like dict (column -> missing count)
    - list of dicts -> keys are column names
    - list of lists/tuples -> columns indexed by integer

    Returns a dict mapping column name/index to missing count.
    """
    if pd is not None and isinstance(df, pd.DataFrame):
        # Use pandas fast path and convert to dict
        return df.isna().sum().to_dict()

    # Convert list-of-dicts to a column-oriented mapping
    if isinstance(df, list) and df and isinstance(df[0], dict):
        cols = {}
        for row in df:
            for k, v in row.items():
                cols.setdefault(k, []).append(v)
        # Count NAs (None or float('nan'))
        result: Dict[Any, int] = {}
        for k, vals in cols.items():
            result[k] = sum(1 for x in vals if x is None or (isinstance(x, float) and x != x))
        return result

    # If it's a list of lists/tuples or any iterable of iterables
    # treat columns by index
    try:
        rows = list(df)
    except TypeError:
        raise TypeError("Unsupported input type for count_missing_values")

    if not rows:
        return {}

    if all(isinstance(r, (list, tuple)) for r in rows):
        ncols = max(len(r) for r in rows)
        result = {i: 0 for i in range(ncols)}
        for r in rows:
            for i in range(ncols):
                try:
                    val = r[i]
                except IndexError:
                    # missing column value
                    result[i] += 1
                    continue
                if val is None or (isinstance(val, float) and val != val):
                    result[i] += 1
        return result

    raise TypeError("Unsupported input type for count_missing_values")
