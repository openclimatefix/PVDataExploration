python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2010/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2011/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2012/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2013/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2014/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2015/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2016/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2017/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2018/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2019/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2020/
python3 -u change_csv_to_parquet.py --folder=../../Data/30min/2021/

python3 -u reformat.py --folder=../../Data/30min/2010/
python3 -u reformat.py --folder=../../Data/30min/2011/
python3 -u reformat.py --folder=../../Data/30min/2012/
python3 -u reformat.py --folder=../../Data/30min/2013/
python3 -u reformat.py --folder=../../Data/30min/2014/
python3 -u reformat.py --folder=../../Data/30min/2015/
python3 -u reformat.py --folder=../../Data/30min/2016/
python3 -u reformat.py --folder=../../Data/30min/2017/
python3 -u reformat.py --folder=../../Data/30min/2018/
python3 -u reformat.py --folder=../../Data/30min/2019/
python3 -u reformat.py --folder=../../Data/30min/2020/
python3 -u reformat.py --folder=../../Data/30min/2021/

python3 -u merge_all_parquet.py --folder=../../Data/30min/2010/ --filename=../../Data/30min/Yearly_data/2010_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2011/ --filename=../../Data/30min/Yearly_data/2011_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2012/ --filename=../../Data/30min/Yearly_data/2012_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2013/ --filename=../../Data/30min/Yearly_data/2013_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2014/ --filename=../../Data/30min/Yearly_data/2014_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2015/ --filename=../../Data/30min/Yearly_data/2015_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2016/ --filename=../../Data/30min/Yearly_data/2016_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2017/ --filename=../../Data/30min/Yearly_data/2017_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2018/ --filename=../../Data/30min/Yearly_data/2018_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2019/ --filename=../../Data/30min/Yearly_data/2019_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2020/ --filename=../../Data/30min/Yearly_data/2020_30min_newformat.parquet
python3 -u merge_all_parquet.py --folder=../../Data/30min/2021/ --filename=../../Data/30min/Yearly_data/2021_30min_newformat.parquet

python3 -u merge_all_parquet.py --folder=../../Data/30min/Yearly_data/ --filename=../../Data/30min/Yearly_data/all.parquet
