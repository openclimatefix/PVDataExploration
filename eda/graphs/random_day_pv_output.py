from utils.data_loading import load_data, dates_list
import random
from typing import Union, List, Dict
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

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
   
    def xr_to_df(
        self)-> None:
        """
        converts xarray dataset into a pandas dataframe, and its values for a single random day

        """
        # self.date_oi = "2021-10-24" 
        _, self.pv_power_xr = load_data(
            downloads_path = self.downloads_path, 
            metafilename = self.metafilename, 
            netcdffilename = self.netcdffilename)
        
        self.dates_lst = dates_list(
            pv_power_xr = self.pv_power_xr)
        

        self.ssid = random.choice(list(self.pv_power_xr))
        self.date_oi = random.choice(list(self.dates_lst))
        self.date_1 = datetime.strptime(self.date_oi, '%Y-%m-%d')
        self.on_pv_system = self.pv_power_xr[self.ssid].to_dataframe()                         
        
        self.next_day = self.date_1+timedelta(days=1)
        self.on_pv_system = self.on_pv_system[
            (self.on_pv_system.index < self.next_day)
            &
            (self.on_pv_system.index > self.date_1)]

    def pv_singleday_output_display(self)->None:
        """
        Plot the PV output of the day that is randomly selected with SSID and a date
        """

        fig = plt.figure()
        plt.plot(self.on_pv_system)
        fig.suptitle("One-day PV output time-series", fontsize = 10)
        plt.ylabel('Power output KWh', fontsize = 10)
        plt.xlabel(self.date_oi, fontsize = 10)
        plt.xticks([])
        plt.show()


