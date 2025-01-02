from numpy import nan as NA
import pandas as pd

def delete_na(data, how = "all"):
    """
    Delete row that contain NA value
    
    Parameters:
    data: DataFrame
    how: string
        - 'all': Drop rows that are all NA
        - 'any': Drop rows that have any NA
    """
    cleaned = data.dropna(how = how)
    
    return cleaned


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
    
    print("Filtered Data")
    cleaned = delete_na(data, how = "any")
    print(cleaned)
    print("-" * 10)
    
    
    
    




