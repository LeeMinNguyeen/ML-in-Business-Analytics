import pandas as pd
from numpy import nan as NA

def fill_na(data, how):
    """
    Fil; NA value with mean of each row
    
    Parameters:
    data: DataFrame
    how: string

    """
    match how:
        case "mean":
            return data.fillna(data.mean())
        case "median":
            return data.fillna(data.median())
        case "mode":
            return data.fillna(data.mode().iloc[0])


if __name__ == "__main__":
    data = pd.DataFrame([
        [1., 6.5, 3.],
        [1., NA, NA],
        [NA, NA, NA],
        [NA, 6.5, 3.]
    ])
    
    print("Original Data:")
    print(data)
    print("-" * 10)
    
    print("Filled Data")
    filled = fill_na(data, how = "mode")
    print(filled)

