import time
import pandas as pd 
from crawler import crawler
from sqlalchemy import create_engine
import numpy as np
import uuid
import sqlalchemy

def clean_df(df):
    columns = [
        'subject',
        'body',
        'category_name',
        'area_name',
        'region_name',
        'price',
        'rooms',
        'size',
        'ward_name',
        'direction',
        'toilets',
        'floors',
        'price_million_per_m2',
        'street_name',
        'furnishing_sell',
        'property_legal_document',
        'list_id',
        'list_time',
        'length',
        'width',
    ]
    df = df[columns]
    df.fillna(np.nan,inplace=True)
    df.drop_duplicates(subset=['list_id'], inplace=True)
    df.replace([np.nan], [None], inplace=True)
    return df

def upsert_df(df: pd.DataFrame, table_name: str, engine: sqlalchemy.engine.Engine):

    temp_table_name = f"temp_{uuid.uuid4().hex[:6]}"
    df.to_sql(temp_table_name, engine, index=False)

    headers = list(df.columns)
    headers_sql_txt = ", ".join(
        [f'"{i}"' for i in headers]
    )  # index1, index2, ..., column 1, col2, ...

    headers.remove('list_id')
    # col1 = exluded.col1, col2=excluded.col2
    update_column_stmt = ", ".join([f'"{col}" = EXCLUDED."{col}"' for col in headers])

    # Compose and execute upsert query
    query_upsert = f"""
    INSERT INTO "{table_name}" ({headers_sql_txt}) 
    SELECT {headers_sql_txt} FROM "{temp_table_name}"
    ON CONFLICT ("list_id") DO UPDATE 
    SET {update_column_stmt};
    """
    engine.execute(query_upsert)
    engine.execute(f'DROP TABLE "{temp_table_name}"')

def main(path_csv):
    area = pd.read_csv(path_csv)

    alchemyEngine = create_engine('postgresql+psycopg2://airflow:airflow@project-db:5432/airflow')
    for index, row in area.iterrows():

        start_time = time.time()
        bot = crawler.Crawler(AREA_CODE=row.area_id)
        data = bot.run()

        data = pd.DataFrame(data)
        data = clean_df(data)
        upsert_df(data, 'extract_estate_data_raw', alchemyEngine)
        print(f"Successfully-{row.area_id}- %s seconds -" % (time.time() - start_time))
    
    


