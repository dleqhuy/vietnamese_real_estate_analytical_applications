
create_estate_data_table='''
CREATE TABLE IF NOT EXISTS public.extract_estate_data_raw
(
    list_id bigint primary key,
    subject text,
    body text,
    category_name text,
    area_name text,
    region_name text,
    price double precision,
    rooms double precision,
    size double precision,
    ward_name text,
    direction double precision,
    toilets double precision,
    floors double precision,
    price_million_per_m2 double precision,
    street_name text,
    furnishing_sell double precision,
    property_legal_document double precision,
    list_time double precision,
    length double precision,
    width double precision
);
'''
