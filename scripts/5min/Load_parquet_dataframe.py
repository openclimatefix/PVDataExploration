# Load parquet file as a pandas dataframe

import pandas as pd

# Specify the location of your parquet file
file_dir = '/Volumes/Sara_external_drive/PhD/PIPs/OpenClimateFix/Data Huggingface/5min.parquet'
data = pd.read_parquet(file_dir, engine = 'pyarrow')

