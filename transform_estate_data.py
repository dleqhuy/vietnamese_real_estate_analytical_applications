import pandas as pd 
from sqlalchemy import create_engine
import numpy as np
def transform(df):

    df = df.replace('', None)
    df = df.dropna()
    df['list_time'] = df['list_time'].astype('float')
    df['price'] = df['price'].astype('float')
    
    df['list_time'] = df['list_time'].astype('int')

    df['list_time'] = pd.to_datetime(df['list_time'],unit='ms').dt.date

    return df

def select_df(con):
    columns = '''category_name,
    area_name,
    region_name,
    price,
    ward_name,
    street_name,
    list_id,
    list_time
    '''
    df = pd.read_sql_query(f"select {columns} from extract_estate_data_raw", con=con)
    return df

def main():

    alchemyEngine = create_engine('postgresql://postgres:postgres@localhost:5052/postgres')
    df = select_df(alchemyEngine)
    df = transform(df)
    df.to_sql('extract_estate_data_clean', alchemyEngine,if_exists='replace', index=False)

if __name__ == '__main__':
    main() 