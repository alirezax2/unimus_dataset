import pandas as pd
import json

def json_to_dataframe(filename):
    """
    Converts a JSON file to a pandas DataFrame.
    
    Parameters:
        filename (str): The name of the JSON file to load.
    
    Returns:
        pd.DataFrame: A DataFrame containing the JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    
    return df

filename = 'photoMetadataVM.json'
df = json_to_dataframe(filename)
print(df.head())
df.to_parquet('photoMetadataVM.parquet')

df.shape
df.iloc[0:1].T



filename = 'photoMetadataUMAK.json'
df = json_to_dataframe(filename)
print(df.head())
df.to_parquet('photoMetadataUMAK.parquet')

df.shape
df.iloc[0:1].T

filename = 'photoMetadataUM.json'
df = json_to_dataframe(filename)
print(df.head())
df.to_parquet('photoMetadataUM.parquet')

df.shape
df.iloc[0:1].T

filename = 'photoMetadataUM.json'
df = json_to_dataframe(filename)
print(df.head())
df.to_parquet('photoMetadataUM.parquet')

df.shape
df.iloc[0:1].T


#######################
import os
for jsonfile in os.listdir('.'):
    if jsonfile.endswith('.json'):
        print(jsonfile)
        df = json_to_dataframe(jsonfile)
        df.to_parquet(jsonfile[:-5]+'.parquet')
        print(df.shape)
        print(df.iloc[0:1].T)
    