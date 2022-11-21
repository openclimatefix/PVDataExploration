from graphs import singleday_pv_output
from no_pv_output_singleday import no_pv_df
from utils.data_loading import *
import click

@click.command()
@click.option(
    "--option-func",
    prompt= "Option to choose a function",
    help = "Write which function  you want to execute"
)
@click.option(
    "--downloads-path",
    prompt = " Path to the download folder",
    help = "Provide a absolute path to the folder"
    )
@click.option(
    "--metafilename",
    prompt = "Write the name of the metadata file",
    help = "Provide the name of the metadata file"
    )
@click.option(
    "--netcdffilename",
    prompt = "Write the name of the netcdf file",
    help = "Provide the name of the netcdf file"
    )
@click.option(
    "--nopvdata",
    prompt = "Path to the no pv data csv",
    help = "Provied the path to the no pv data csv file"
    )
@click.option(
    "--csv-filename",
    prompt = "Name of the csv file",
    help = "Provide a name of the csv file with .csv extension"
)

# class run_all:
#     def __init__(
#         self,
#         option_func:str,
#         downloads_path:Path[Union, str], 
#         metafilename:str, 
#         netcdffilename:str,
#         csv_filename:str = None,
#         nopvdata:Path[Union, str] = None,
#         random_choice:bool = None     
#         )-> None:
#         self.option_func = option_func
#         self.downloads_path = downloads_path
#         self.metafilename = metafilename
#         self.netcdffilename = netcdffilename
#         self.csv_filename = csv_filename
#         self.nopvdata = nopvdata
#         self.random_choice = random_choice
    
def multi_fun(option_func):
    if option_func == "nopvdata":
        def no_pv_data(
            downloads_path, 
            metafilename, 
            netcdffilename, 
            csv_filename):
            pv_df, pv_xr = load_data(
                downloads_path = downloads_path, 
                metafilename = metafilename, 
                netcdffilename = netcdffilename)
            dates_list = list(dates_list(
                pv_power_xr = pv_xr))
            ssid_list = list(pv_xr)
            nopvdf = no_pv_df(
                ssid_list = ssid_list,
                dates_list = dates_list,
                csv_filename = csv_filename
            )
    elif option_func == "display":
        def display_graph(
            downloads_path,
            metafilename, 
            netcdffilename,
            random_choice):
            disp = singleday_pv_output(
                downloads_path = downloads_path, 
                metafilename = metafilename, 
                netcdffilename = netcdffilename,
                random_choice = random_choice)
            disp.loading_xr_netcdf()
            # disp.pv_singleday_output_display(
            #     no_pv_df_path = nopvdata
            #     )

if __name__ == "__main__":
    multi_fun()
    # run = run_all(
    #     option_func = option_func,
    #     downloads_path = downloads_path,
    #     metafilename = metafilename,
    #     netcdffilename = netcdffilename,
    #     csv_filename = csv_filename,
    #     nopvdata = nopvdata
    #     )
    # run.multi_fun()

