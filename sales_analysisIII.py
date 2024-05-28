import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    first_quarter = sales[(sales['sale_date']>= '2019-01-01') & (sales['sale_date']<='2019-03-31')]
    other_quarter = sales[(sales['sale_date']< '2019-01-01') | (sales['sale_date']>'2019-03-31')]
    p_id = first_quarter[~first_quarter['product_id'].isin(other_quarter['product_id'])]['product_id']
    df = product[(product['product_id'].isin(p_id))]
    return df[['product_id','product_name']]
    
