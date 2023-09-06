import os
from sqlalchemy import create_engine
from call_api import *

def get_snowflake_engine(snowflake_database, snowflake_schema):

    # Retrieve the connection details
    snowflake_account = os.environ.get('SNOWFLAKE_ACCOUNT')
    snowflake_user = os.environ.get('SNOWFLAKE_USER')
    snowflake_password = os.environ.get('SNOWFLAKE_PASSWORD')
    snowflake_role = os.environ.get('SNOWFLAKE_ROLE')
    snowflake_warehouse = os.environ.get('SNOWFLAKE_WAREHOUSE')
    snowflake_database = snowflake_database
    snowflake_schema = snowflake_schema

    # conn_string = f"snowflake://{snowflake_user}:{snowflake_password}@{snowflake_account}/{snowflake_database}/{snowflake_schema}?role={snowflake_role}&warehouse={snowflake_warehouse}"
    conn_string = f"snowflake://{snowflake_user}:{snowflake_password}@{snowflake_account}/{snowflake_database}/{snowflake_schema}"
    engine = create_engine(conn_string)

    return engine