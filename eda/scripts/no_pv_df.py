from utils.file_management import find_files, create_dir
from pathlib import Path
import pandas as pd
from typing import List, Dict
import os

class no_pv_df:
    def __init__(
        self,
        ssid_list:List,
        dates_list:List,
        csv_filename:str)->None:
        self.ssid_list = ssid_list
        self.dates_list = dates_list
        self.csv_filename = csv_filename
 
    def no_pv_df(
        self
        )-> pd.DataFrame():
        """
        This function gives a pandas dataframe that stores 
        all the SSID with corresponding dates with no PV output

        """
        no_pv_df = pd.DataFrame()
        for i in self.ssid_list:
            for j in self.dates_list:
                # xr_to_df function gives a dataframe for one ssid 
                # and its corresponsing date
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
        
        data_path = create_dir(
            working_dir = default_folder,
            dir_name = "no_pv_data"
            )
        data_file = Path(os.path.join(data_path, self.csv_filename))
        pv_df.to_csv(data_file, sep='\t', encoding='utf-8', index=False)
        return pv_df