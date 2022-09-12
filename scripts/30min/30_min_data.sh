python3 -u change_csv_to_parquet.py --folder=../../data/30min/2010/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2011/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2012/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2013/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2014/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2015/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2016/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2017/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2018/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2019/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2020/
python3 -u change_csv_to_parquet.py --folder=../../data/30min/2021/

python3 -u merge_all_parquet.py --folder=../../data/30min/2010/ --filename=../../data/30min/Yearly_data/2010_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2011/ --filename=../../data/30min/Yearly_data/2011_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2012/ --filename=../../data/30min/Yearly_data/2012_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2013/ --filename=../../data/30min/Yearly_data/2013_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2014/ --filename=../../data/30min/Yearly_data/2014_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2015/ --filename=../../data/30min/Yearly_data/2015_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2016/ --filename=../../data/30min/Yearly_data/2016_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2017/ --filename=../../data/30min/Yearly_data/2017_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2018/ --filename=../../data/30min/Yearly_data/2018_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2019/ --filename=../../data/30min/Yearly_data/2019_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2020/ --filename=../../data/30min/Yearly_data/2020_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../data/30min/2021/ --filename=../../data/30min/Yearly_data/2021_30min_newformat.parquet

python3 -u merge_all_parquet.py --folder=../../data/30min/Yearly_data/ --filename=../../data/30min/Yearly_data/all.parquet
