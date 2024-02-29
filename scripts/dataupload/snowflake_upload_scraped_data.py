from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy.engine import URL
import pandas as pd
import numpy as np

load_dotenv()

TABLE_NAME_WEB_SCRAPED = 'web_scraped_data'
DATABASE_NAME = 'cfa'
WAREHOUSE_NAME = 'cfa_wh'


base_url = URL.create(
    "snowflake",
    username=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASS'),
    host=os.getenv('SNOWFLAKE_ACC_ID'),
)

# Creating database for storing cfa data
create_cfa_database_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};"


# Creating table for scraped data
create_scraped_data_table_query = f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME_WEB_SCRAPED} (
    topic STRING,
    year INTEGER,
    level STRING,
    introduction TEXT,
    learning_outcomes TEXT,
    summary TEXT,
    link_summary STRING,
    link_pdf STRING, 
    PRIMARY KEY (link_summary)
)
"""

# Creating warehouse for the cfa databases
create_cfa_warehouse_query = f"""CREATE WAREHOUSE IF NOT EXISTS {WAREHOUSE_NAME} WITH
    WAREHOUSE_SIZE = 'X-SMALL'
    AUTO_SUSPEND = 180
    AUTO_RESUME = TRUE
    INITIALLY_SUSPENDED = TRUE; 
"""

def execute_ddl_queries(connection):
    connection.execute(create_cfa_warehouse_query)
    connection.execute(create_cfa_database_query)
    connection.execute(f'USE WAREHOUSE {WAREHOUSE_NAME};')
    connection.execute(f'USE DATABASE {DATABASE_NAME};')
    connection.execute(create_scraped_data_table_query)

def upload_into_web_scraped_db(connection):
    copy_into_webscraped_db = f"""COPY INTO {DATABASE_NAME}.PUBLIC.{TABLE_NAME_WEB_SCRAPED}
        FROM '@{DATABASE_NAME}.PUBLIC.%{TABLE_NAME_WEB_SCRAPED}'
        FILES = ('urlclass_data.csv.gz')
        FILE_FORMAT = (
            TYPE=CSV,
            SKIP_HEADER=1,
            FIELD_DELIMITER=',',
            TRIM_SPACE=FALSE,
            FIELD_OPTIONALLY_ENCLOSED_BY='"',
            REPLACE_INVALID_CHARACTERS=TRUE,
            DATE_FORMAT=AUTO,
            TIME_FORMAT=AUTO,
            TIMESTAMP_FORMAT=AUTO
        )
        ON_ERROR=ABORT_STATEMENT
        PURGE=TRUE
    """
    connection.execute(f"PUT file://../clean_csv/urlclass_data.csv @{DATABASE_NAME}.PUBLIC.%{TABLE_NAME_WEB_SCRAPED};")
    connection.execute(copy_into_webscraped_db)


def execute_insertion(values_str, id):
    try:
        print("Started upload")
        connection.execute("BEGIN")
        connection.execute(f"""INSERT INTO {TABLE_NAME_WEB_SCRAPED}
                            VALUES
                            {values_str};""")
        connection.execute("COMMIT")
        print(f"Upload successful till record count: {id+1}")
    except Exception as e:
        connection.execute("ROLLBACK")
        print("Exception inserting rows into db. Rolling back! "+str(e))

engine = create_engine(base_url)

try:
    connection = engine.connect()
    execute_ddl_queries(connection=connection)
    upload_into_web_scraped_db(connection=connection)

except Exception as e:
    print(e)
finally:
    connection.close()
    engine.dispose()
