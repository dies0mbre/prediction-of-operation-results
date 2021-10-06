import pandas as pd
import numpy as np


def read_excel_sheets(path : str = '') -> tuple[list, dict[str, list[pd.DataFrame]]]:
    temp = pd.read_excel(path, sheet_name=None)
    return list(temp.keys()), temp

# print(read_excel_sheets('./data/data.xls'))