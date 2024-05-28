import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] < '2020-01-01')]
    orders = orders.groupby('buyer_id').size().reset_index(name = 'count')
    df = users.merge(orders, left_on = 'user_id', right_on = 'buyer_id',how = 'left').fillna(0)

    return df[['user_id','join_date','count']].rename(
        columns = {'user_id':'buyer_id','count':'orders_in_2019'})
