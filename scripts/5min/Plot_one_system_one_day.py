# Select and plot one day of PV data from one PV system

import pandas as pd
import matplotlib.pyplot as plt

# Specify the location of your parquet file and load it as a pandas dataframe
file_dir = '/Volumes/Sara_external_drive/PhD/PIPs/OpenClimateFix/Data Huggingface/5min.parquet'
data = pd.read_parquet(file_dir, engine = 'pyarrow')

# Select data from one PV system
PV_system = 2631
PV_data = data.loc[data['ss_id'] == PV_system]

# Select data from one day (2021-04-01)
day = '2021-04-01'
following_day = '2021-04-02'
PV_data_1day = PV_data.loc[PV_data['timestamp'] > day]
PV_data_1day = PV_data_1day.loc[PV_data_1day['timestamp'] < following_day]

# Plot power generation of this PV system across this day
PV_data_1day.set_index('timestamp', inplace=True)
PV_data_1day['generation_wh'].plot()
plt.title("Power generation of PV system {PV} on day {date}".format(PV=PV_system, date=day))
plt.xlabel("time")
plt.ylabel("power generation (wh)")
hours_dataformat = pd.date_range(start="2021-04-01",end="2021-04-02", freq="3H")
hours_dataformat = hours_dataformat.strftime("%Y-%m-%d %H:%M:%S+00:00").tolist()
hours_plot = ['12 am', '3 am', '6 am', '9 am', '12 pm', '3 pm', '6 pm', '9 pm', '12 am']
plt.xticks(hours_dataformat, hours_plot, rotation=30)
plt.show()
