from utils.data_loading import load_data, dates_list, no_pv_df_to_dict
from pathlib import Path
import xarray as xr
import random
import pandas as pd
import numpy as np
from typing import Union, List, Dict
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
from alive_progress import alive_bar
import time


class singleday_pv_output:
    def __init__(
        self,
        downloads_path:Path[Union,str],
        metafilename:str,
        netcdffilename:str,
        random_choice:bool = None       
        )->None:
        self.downloads_path = downloads_path
        self.metafilename = metafilename
        self.netcdffilename = netcdffilename
        self.random_choice = random_choice
   
    def loading_xr_netcdf(
        self
        )-> None:

        self.pv_power_meta, self.pv_power_xr = load_data(
            downloads_path = self.downloads_path, 
            metafilename = self.metafilename, 
            netcdffilename = self.netcdffilename)
        
        self.dates_lst = dates_list(
            pv_power_xr = self.pv_power_xr) 
    
    @staticmethod
    def xr_to_df(
        pv_power_xr:xr.Dataset,
        ssid:str ,
        date_oi:str
        )-> pd.DataFrame():
        """
        converts xarray dataset into a pandas dataframe, and its values for a single day

        """                            
        date_1 = datetime.strptime(date_oi, '%Y-%m-%d')
        on_pv_system = pv_power_xr[ssid].to_dataframe()                               
        next_day = date_1+timedelta(days=1)
        on_pv_system = on_pv_system[
            (on_pv_system.index < next_day)
            &
            (on_pv_system.index > date_1)]
        return on_pv_system
    

    def pv_singleday_output_display(
        self,
        no_pv_df_path: Path[Union, str])->None:
        """
        Plot the PV output of the day that is randomly selected with SSID and a date
        """
        status = True
        ssid_list = list(self.pv_power_xr)
        dates_list = list(self.dates_lst) 
        ssid = random.choice(ssid_list)
        date_oi = random.choice(list(self.dates_lst))               
        # no_pv_dict = no_pv_df_to_dict(
        #     no_pv_df_path = no_pv_df_path)
    
        # if not self.random_choice:
            # ssid = random.choice(list(self.pv_power_xr))
            # ssid = random.choice(ssid_list)
            # date_oi = random.choice(list(self.dates_lst))
            # while status:
            #     date_oi = random.choice(dates_list)
            #     if date_oi not in no_pv_dict[np.float(ssid)]:
            #         break
        print("Randomly selected ssid is", ssid)
        print("Randomly selected date for that ssid is", date_oi)
        
        on_pv_sys = singleday_pv_output.xr_to_df(
            pv_power_xr = self.pv_power_xr, 
            ssid = ssid, 
            date_oi = date_oi)
        
        fig = plt.figure() 
        plt.plot(on_pv_sys)
        fig.suptitle("One-day PV output time-series", fontsize = 10)
        plt.ylabel('Power output KW', fontsize = 10)
        plt.xlabel(date_oi, fontsize = 10)
        plt.xticks([])
        plt.show()