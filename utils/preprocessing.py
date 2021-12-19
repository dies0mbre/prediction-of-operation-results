import pandas as pd
import numpy as np


def read_excel_sheets(path : str = '') -> tuple[list, dict[str, list[pd.DataFrame]]]:
    if '.csv' in path:
        temp = pd.read_csv(path)
    if '.xls'in path:
        temp = pd.read_excel(path, sheet_name=None)
    return list(temp.keys()), temp
