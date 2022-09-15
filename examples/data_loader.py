"""

You need to install ocf_datapipes

for example
pip install -e ../ocf_datapipes --no-deps

you can get the dat files from
https://huggingface.co/datasets/openclimatefix/uk_pv/blob/main/pv.netcdf

and use pv.netcdf and metadata.csv.
Good to rename metadata.csv as metadata_passiv.csv
and changed 'latitude_rounded' column to 'latitude'

Loading all the PV data can take ~10 minutes.
To solve this we could can reduce the dataset when developing

import pandas as pd
pv_df = pd.read_parquet('5min.parquet',  engine='fastparquet')
pv_df = pv_df[pv_df['ss_id'] <= 2620]
pv_df.to_parquet('5min_test.parquet',  engine='fastparquet')

"""
import logging
import pandas as pd

from ocf_datapipes.training.simple_pv import simple_pv_datapipe
from ocf_datapipes.utils.consts import BatchKey

# set up logging
logging.basicConfig(
    level=getattr(logging, 'DEBUG'),
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
)


# make iterattor
simple_pv = simple_pv_datapipe('examples/test.yaml')
simple_pv = iter(simple_pv)

# get a batch
batch = next(simple_pv)

# this gives the time stamps for pv systems
print(batch[BatchKey.pv_time_utc])
print(pd.to_datetime(batch[BatchKey.pv_time_utc][0], unit='s'))

# this gives the normalized power values
print(batch[BatchKey.pv])

# this is how you get the history and future datatime.
# Idea is you use the history + other variables to try to predict the future.
history = batch[BatchKey.pv][:,:batch[BatchKey.pv_t0_idx]]
future = batch[BatchKey.pv][:,batch[BatchKey.pv_t0_idx]:]
