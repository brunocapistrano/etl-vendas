import pandas as pd


def type_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the data types of the input DataFrame by performing the following operations:
    
        1. Convert column 'first_purchase_date', 'last_purchase_date' 
    and 'order_date' to datetime in the format YYYY-MM-DD.

    """
    
    df['first_purchase_date'] = pd.to_datetime(df['first_purchase_date'], format='%Y-%m-%d')
    df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'], format='%Y-%m-%d')
    df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')

    return df

if __name__ == "__main__":
    type_transform()