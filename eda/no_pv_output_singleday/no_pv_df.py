class no_pv_df:
    def __init__(self)->None:
        """"""
        pass
    
    def no_pv_df(
        self
        )-> pd.DataFrame():
        """
        This function gives a pandas dataframe that stores 
        all the SSID with corresponding dates with no PV output

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