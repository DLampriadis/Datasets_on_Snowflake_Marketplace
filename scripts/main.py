import time
from call_api import*
from snowflake_connector import*
from transformation import*
from descriptions import get_descriptions_table

def main():
    tic = time.perf_counter()

    snowflake_database = 'MARKETPLACE'
    snowflake_schema = 'PUBLIC'

    # Dataset Monthly_figures_on_aviation
    df_monthly_figures_on_aviation = get_data_as_dataframe('https://opendata.cbs.nl/ODataFeed/odata/37478eng/UntypedDataSet?%24format=json')
    df_monthly_figures_on_aviation = transform_figures_on_aviation(df_monthly_figures_on_aviation)
    write_table(df=df_monthly_figures_on_aviation, snowflake_database=snowflake_database, snowflake_schema=snowflake_schema, snowflake_table='monthly_figures_on_aviation_in_NL')
    comments_monthly_aviation = get_descriptions_table('aviation')
    add_column_comments(snowflake_database=snowflake_database, snowflake_schema=snowflake_schema, snowflake_table='monthly_figures_on_aviation_in_NL', column_comments=comments_monthly_aviation)

    # Dataset Airport codes
    airport_codes = {'Key':['A045844','A043590','A043596','A043591','A043595','A043593'],
                    'Title':['Totaal Dutch airports','Amsterdam Airport Schiphol','Rotterdam The Hague Aiport','Eindhoven Airport','Maastricht Aachen Airport','Groningen Airport Eelde']
                     }
    
    airports=pd.DataFrame.from_dict(airport_codes)
    write_table(df=airports, snowflake_database=snowflake_database, snowflake_schema=snowflake_schema, snowflake_table='NL_Airports')
    comments_airports = get_descriptions_table('airports')
    add_column_comments(snowflake_database=snowflake_database, snowflake_schema=snowflake_schema, snowflake_table='NL_Airports', column_comments=comments_airports)
    

    # Dataset income of households
    df_income_households = get_data_as_dataframe('https://opendata.cbs.nl/ODataFeed/odata/84103ENG/UntypedDataSet?%24format=json')
    df_income_households = transform_income_households(df_income_households)
    write_table(df=df_income_households, snowflake_database=snowflake_database, snowflake_schema=snowflake_schema, snowflake_table='income_accounts_households_in_NL')
    comments_income_accounts = get_descriptions_table('income_households')
    add_column_comments(snowflake_database=snowflake_database, snowflake_schema=snowflake_schema, snowflake_table='income_accounts_households_in_NL', column_comments=comments_income_accounts)

    toc = time.perf_counter()
    print(f"Executed in {toc - tic:0.4f} seconds")

if __name__ == "__main__":
    main()