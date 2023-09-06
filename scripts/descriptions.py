import pandas as pd

def get_descriptions_table(var):
    
    if var == 'aviation':
        metadata = pd.read_csv('../monthly_figures_on_aviation_income_households/Metadata/monthly_aviation_metadata.csv')

        metadata.drop(metadata.columns[[0, 1, 2, 3, 7, 8, 10, 11]], axis=1, inplace=True)
        metadata = metadata[metadata["Key"].notna()].reset_index(drop=True)

        key=[]
        description = []

        key = metadata["Key"].unique().tolist()
        description = metadata["Description"].tolist()
        description = ['no info' if pd.isna(x) else x for x in description]

        removable = str.maketrans('', '', "';")
        description = [s.translate(removable).replace('\n',' ') for s in description]

        res = {key[i]: description[i] for i in range(len(key))}

    if var == 'income_households':
        metadata = pd.read_csv('../monthly_figures_on_aviation_income_households/Metadata/Income_households_metadata.csv')

        metadata.drop(metadata.columns[[0, 1, 2, 3, 7, 8, 10, 11]], axis=1, inplace=True)
        metadata = metadata[metadata["Key"].notna()].reset_index(drop=True)

        key=[]
        description = []

        key = metadata["Key"].unique().tolist()
        description = metadata["Description"].tolist()
        description = ['no info' if pd.isna(x) else x for x in description]

        removable = str.maketrans('', '', "';")
        description = [s.translate(removable).replace('\n',' ') for s in description]

        res = {key[i]: description[i] for i in range(len(key))}

    elif var == 'airports':
        metadata = pd.read_csv('../monthly_figures_on_aviation_income_households/Metadata/monthly_aviation_metadata-Airports.csv')

        key=[]
        description = []

        key = metadata["Key"].unique().tolist()
        description = metadata["Title"].tolist()
        res = {key[i]: description[i] for i in range(len(key))}

    return res
