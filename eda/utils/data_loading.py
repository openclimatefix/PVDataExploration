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
    print("\nLoading of both meta and netcdf files are finished successfully\n")
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

# if __name__ == "__main__":
#     downloads_path = r"c:\\Users\\vardh\\OneDrive - University of Leicester\\OCF\\Git_repos\\downloads\\huggingface_uk_pv"
#     metafilename = "uk_pv_metadata.csv"
#     netcdffilename = "uk_pv_netcdf.netcdf"
#     dops = dataops(
#         downloads_path = downloads_path,
#         metafilename = metafilename,
#         netcdffilename = netcdffilename        
#     )
#     dops.load_data()
#     dops.dates_list()