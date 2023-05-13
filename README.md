# vietnamese_real_estate_analytical_applications
Vietnamese_Real_Estate_Advertisement_Posts_and_Analytical_Applications

Processing real estate in HCMC, raw data after scraping from nhatot.vn is put into Postgres, then transform and load into postgres data warehouse. BI tool for data using Superset.

## Architecture

![](docs/Architecture.drawio.png)

## Run

    git clone https://github.com/dleqhuy/vietnamese_real_estate_analytical_applications.git
    cd vietnamese_real_estate_analytical_applications

And finally, we launch all the services:

```sh
docker-compose up
```

After running them, you can crawl the data put into the database. We do this:

```sh
python extract_estate_data.py
```
![](docs/extract_estate_data.png)

you can transfrom the data to visualization. We do this:
```sh
python transform_estate_data.py
```
superset

![](docs/superset.png)

### Web services

*   [pgAdmin](http://localhost:5050)
*   [Superset](http://localhost:5054)

### Other services available to the host

*   warehouse-postgres: [localhost:5052](\[localhost:5052])

Database address (for pgAdmina): `warehouse-postgres:5432`

Database configuration and pgAdmin:

```text
POSTGRES_USER: postgres
POSTGRES_PASSWORD: postgres
POSTGRES_DB: postgres
PGADMIN_DEFAULT_EMAIL: admin@admin.com
PGADMIN_DEFAULT_PASSWORD: admin
```


