#python3 -u change_csv_to_parquet.py --folder=../../Data/2min/Yearly_data/
python3 -u megre_parquet_files.py --folder=../../Data/2min/2016/ --filename=../../Data/2min/Yearly_data/2016.parquet
python3 -u megre_parquet_files.py --folder=../../Data/2min/2017/ --filename=../../Data/2min/Yearly_data/2017.parquet
python3 -u megre_parquet_files.py --folder=../../Data/2min/2018/ --filename=../../Data/2min/Yearly_data/2018.parquet
python3 -u megre_parquet_files.py --folder=../../Data/2min/2019/ --filename=../../Data/2min/Yearly_data/2019.parquet
python3 -u megre_parquet_files.py --folder=../../Data/2min/2020/ --filename=../../Data/2min/Yearly_data/2020.parquet
python3 -u megre_parquet_files.py --folder=../../Data/2min/2021/ --filename=../../Data/2min/Yearly_data/2021.parquet

python3 -u merge_all_parquet.py --folder=../../Data/2min/Yearly_data/ --filename=../../Data/2min/Yearly_data/2min.parquet
