# Libraries
import os
import random
from datetime import datetime, date, timedelta
from typing import Dict, List, Tuple, Union
from pathlib import Path
import pandas as pd
import xarray as xr
from utils.file_management import find_files



def load_data(
    downloads_path:Path[Union, str],
    metafilename:str,
    netcdffilename:str):
    """
    Args:
    downloads_path = Set the path where the downloaded meta and netcdf files are
    metafilename = input the metadata file name inclusing extension(.csv)
    netcdffilename = as suggested above including the extension(.netcdf)
    """        
    _, uk_pv_meta_path = find_files(
        filename = metafilename,
        search_path = downloads_path
    )

    _, uk_pv_netcdf_path = find_files(
        filename = netcdffilename,
        search_path = downloads_path
    )

    metadata_df = pd.read_csv(uk_pv_meta_path)
    pv_power_xr = xr.open_dataset(uk_pv_netcdf_path, engine="h5netcdf")
    print("\nLoading of both meta and netcdf files is finished successfully\n")
    return metadata_df, pv_power_xr

def dates_list(
    pv_power_xr: xr.Dataset
    )->List:
    """
    Converts dates as coordinates from xarray dataset to a list
    """
    dates_lst = pv_power_xr["datetime"].values
    dates_lst = [pd.to_datetime(str(i))for i in dates_lst]
    dates_lst = [i.strftime('%Y-%m-%d') for i in dates_lst]
    dates_lst = list(set(dates_lst))
    return dates_lst

def no_pv_df_to_dict(
    no_pv_df_path: Path[Union, str]
    )-> Dict:
    """
    Function that takes a csv file with ssid and dates of
    pv systems with no data and converts that into a dictionary
    """
    df = pd.read_csv(no_pv_df_path, sep = "\t")
    no_pv_dict = {}
    for i in df['ssid'].unique().tolist():
        df_slice = df[df['ssid'] == i]
        no_pv_dict[i] = df_slice['date'].tolist()
    return no_pv_dict

# no_pv_df_path = r"C:\Users\vardh\OneDrive - University of Leicester\OCF\Git_repos\PVDataExploration\PVDataExploration\no_pv_output.csv"
# dict1 = no_pv_df_to_dict(
#     no_pv_df_path = no_pv_df_path)
# print(dict1[6630])