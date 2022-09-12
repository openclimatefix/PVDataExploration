python3 -u change_csv_to_parquet.py --folder=../../Data/5min/2018/
python3 -u change_csv_to_parquet.py --folder=../../Data/5min/2019/
python3 -u change_csv_to_parquet.py --folder=../../Data/5min/2020/
python3 -u change_csv_to_parquet.py --folder=../../Data/5min/2021/

python3 -u merge_parquet_files.py --folder=../../Data/5min/2018/ --filename=../../Data/5min/Yearly_data/2018.parquet
python3 -u merge_parquet_files.py --folder=../../Data/5min/2019/ --filename=../../Data/5min/Yearly_data/2019.parquet
python3 -u merge_parquet_files.py --folder=../../Data/5min/2020/ --filename=../../Data/5min/Yearly_data/2020.parquet
python3 -u merge_parquet_files.py --folder=../../Data/5min/2021/ --filename=../../Data/5min/Yearly_data/2021.parquet

python3 -u merge_parquet_files.py --folder=../../Data/5min/Yearly_data/ --filename=../../Data/5min/Yearly_data/5min.parquet
