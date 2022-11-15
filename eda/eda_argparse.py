from graphs import singleday_pv_output
import argparse
import sys


parser = argparse.ArgumentParser("Random single day PV output graph")
parser.add_argument(
    "--downloads-path", 
    help="Working directory folder.",
    required=True,
    type=str
    )
parser.add_argument(
    "--metafilename", 
    help="File name of the metadata.csv.",
    required=True,
    type=str
    )
parser.add_argument(
    "--netcdffilename", 
    help="File name of the netcdf file .netcdf",
    required=True,
    type=str
    )
args = parser.parse_args()
# args = {
#     "downloads_path" : r"c:\\Users\\vardh\\OneDrive - University of Leicester\\OCF\\Git_repos\\downloads\\",
#     "metafilename" : "uk_pv_metadata.csv",
#     "netcdffilename" : "uk_pv_netcdf.netcdf"
# }     
disp = singleday_pv_output(
    downloads_path = args.downloads_path, 
    metafilename = args.metafilename, 
    netcdffilename = args.netcdffilename
    )
disp.xr_to_df()
disp.pv_singleday_output_display()
