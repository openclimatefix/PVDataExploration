# Select and plot one year of PV data from ten PV systems

import pandas as pd
import matplotlib.pyplot as plt

# Specify the location of your parquet file and load it as a pandas dataframe
file_dir = '/Volumes/Sara_external_drive/PhD/PIPs/OpenClimateFix/Data Huggingface/5min.parquet'
data = pd.read_parquet(file_dir, engine = 'pyarrow')

# Extract data of 10 PV systems
PV_data = pd.DataFrame(columns = ["generation_wh","timestamp","ss_id"])
PV_systems = [13308, 13057, 7548, 7542, 10589, 6891, 9369, 11438, 18989, 7243]
for i in range(10): 
    PV = PV_systems[i]    
    PV_data = PV_data.append(data.loc[data['ss_id'] == PV])
    
# Select data from one year
start_day = '2020-01-01'
end_day = '2021-01-01'
PV_data_1year = PV_data.loc[PV_data['timestamp'] > start_day]
PV_data_1year = PV_data_1year.loc[PV_data_1year['timestamp'] < end_day]

# Plot data of these 10 PV systems for one year (2020)
plt.plot(PV_data_1year['timestamp'], PV_data_1year['generation_wh']) 
plt.title("Power generation of 10 PV systems during 2020")
plt.xlabel("month")
plt.ylabel("power generation (wh)")
hours_dataformat = pd.date_range(start="2020-01-01",end="2020-12-31", freq="MS")
hours_dataformat = hours_dataformat.strftime("%Y-%m-%d %H:%M:%S+00:00").tolist()
hours_plot = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(hours_dataformat, hours_plot, rotation=30) 
plt.show()

