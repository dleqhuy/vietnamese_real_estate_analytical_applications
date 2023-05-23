import pandas as pd 
from crawler import crawler
from sqlalchemy import create_engine
import numpy as np

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
    df = df.fillna(np.nan)
    df = df.drop_duplicates(subset=['list_id'])
    df = df.replace([np.nan], [None])
    return df

def main(path_csv):
    area = pd.read_csv(path_csv)

    alchemyEngine = create_engine('postgresql://postgres:postgres@localhost:5052/postgres')
    
    for index, row in area.iterrows():
        data = []
        bot = crawler.Crawler(AREA_CODE=row.area_id)
        data.extend(bot.run())
        print(f" Successfully-{row.area_id}-{row.area_name}")
        data = pd.DataFrame(data)
        data = clean_df(data)
        data.to_sql('extract_estate_data_raw', alchemyEngine,if_exists='append', index=False)


if __name__ == '__main__':
    main('crawler/area.csv') 