import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.drop_duplicates('num', keep = False).max()
    return pd.DataFrame([df], columns = ['num'])
