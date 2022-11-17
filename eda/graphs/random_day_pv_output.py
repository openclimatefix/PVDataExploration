from utils.data_loading import load_data, dates_list
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
        downloads_path:str,
        metafilename:str,
        netcdffilename:str       
        )->None:
        self.downloads_path = downloads_path
        self.metafilename = metafilename
        self.netcdffilename = netcdffilename
   
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
        pv_power_xr:xr.Dataset = None,
        ssid:str = None,
        # ssid_list:List = None
        date_oi:str = None
        # dates_lst:List = None,
        # random_choice:bool = True
        ):
        """
        converts xarray dataset into a pandas dataframe, and its values for a single random day

        """ 
        # if not random_choice:
        #     # ssid = random.choice(list(self.pv_power_xr))
        #     ssid = random.choice(list(ssid_list))
        #     # self.date_oi = random.choice(list(self.dates_lst))
        #     date_oi = random.choice(list(dates_lst))
        # else:
        #     self.ssid = ssid
        #     self.date_oi = date   
                           
        date_1 = datetime.strptime(date_oi, '%Y-%m-%d')
        on_pv_system = pv_power_xr[ssid].to_dataframe()                               
        next_day = date_1+timedelta(days=1)
        on_pv_system = on_pv_system[
            (on_pv_system.index < next_day)
            &
            (on_pv_system.index > date_1)]
        return on_pv_system

    # def pv_singleday_output_display(self)->None:
    #     """
    #     Plot the PV output of the day that is randomly selected with SSID and a date
    #     """

    #     fig = plt.figure() 
    #     plt.plot(self.on_pv_system)
    #     fig.suptitle("One-day PV output time-series", fontsize = 10)
    #     plt.ylabel('Power output KW', fontsize = 10)
    #     plt.xlabel(self.date_oi, fontsize = 10)
    #     plt.xticks([])
    #     plt.show()
    

    def no_pv_df(
        self
        )-> None:
        """
        This function gives a pandas dataframe that stores 
        all the SSID with corresponding dates with no PV output
        Args:
        ssid_list = List of the ssid's of the PV systems
        dates_list = List of the dates that are of interest
        """
        self.ssid_list = list(self.pv_power_xr)
        self.dates_list = list(self.dates_lst)

        no_pv_df = pd.DataFrame()
        for i in self.ssid_list:
            for j in self.dates_list:
                df = singleday_pv_output.xr_to_df(
                    pv_power_xr = self.pv_power_xr,
                    ssid=i,
                    date_oi=j)
                df_values = df.values
                torf = np.isnan(df_values).all()
                if torf == False:
                    continue
                temp = pd.DataFrame(
                    {
                        'ssid': i,
                        'date':j
                    }, index = [0]
                )
                no_pv_df = pd.concat([no_pv_df, temp])
            print("checking for no power in a day for PV system with ssid",i,"has been completed")
            print(len(self.ssid_list) - self.ssid_list.index(i),"systems are left")
        no_pv_df.to_csv("no_pv_output.csv", sep='\t', encoding='utf-8', index=False)
        return no_pv_df

