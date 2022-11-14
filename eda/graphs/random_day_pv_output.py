import sys
sys.path.append(".")

from eda.utils.data_loading import load_data, dates_list
import random
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
          
def xr_to_df(
    downloads_path: str,
    metafilename:str,
    netcdffilename:str):
    """
    converts xarray dataset into a pandas dataframe, and its values for a single random day

    """
    # self.date_oi = "2021-10-24" 
    _, pv_power_xr = load_data(
        downloads_path = downloads_path, 
        metafilename = metafilename, 
        netcdffilename = netcdffilename)
    
    dates_lst = dates_list(
        pv_power_xr = pv_power_xr)
    
    ssid = random.choice(list(pv_power_xr))
    date_oi = random.choice(list(dates_lst))        
    date_1 = datetime.strptime(date_oi, '%Y-%m-%d')
    next_day = date_1+timedelta(days=1)
    on_pv_system = pv_power_xr[ssid].to_dataframe()
    xr_to_df.on_pv_system = on_pv_system[(on_pv_system.index < next_day)&(on_pv_system.index > date_1)]
    xr_to_df.date_oi = date_oi
    return on_pv_system

def pv_singleday_output_display():
    """
    Plot the PV output of the day that is randomly selected with SSID and a date
    """

    fig = plt.figure()
    plt.plot(xr_to_df.on_pv_system)
    fig.suptitle("One-day PV output time-series", fontsize = 10)
    plt.ylabel('Power output KWh', fontsize = 10)
    plt.xlabel(xr_to_df.date_oi, fontsize = 10)
    plt.xticks([])
    plt.show()
