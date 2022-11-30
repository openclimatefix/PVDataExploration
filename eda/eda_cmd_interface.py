from graphs import singleday_pv_output
from utils import find_files
import click
import os
from pathlib import Path

@click.command()
@click.option(
    "--downloads-path",
    prompt = " Path to the download folder",
    type= click.STRING,
    help = "Provide a absolute path to the folder without the paranthesis"
    )
@click.option(
    "--metafilename",
    prompt = "Write the name of the metadata file",
    type = click.STRING,
    help = "Provide the name of the metadata file without the paranthesis"
    )
@click.option(
    "--netcdffilename",
    prompt = "Write the name of the netcdf file",
    type = click.STRING,
    help = "Provide the name of the netcdf file without the paranthesis"
    )

def display_graph(
    downloads_path:str,
    metafilename:str, 
    netcdffilename:str):
    disp = singleday_pv_output(
        downloads_path = downloads_path, 
        metafilename = metafilename, 
        netcdffilename = netcdffilename)
    disp.loading_xr_netcdf()
    disp.pv_singleday_output_display()

if __name__ == "__main__":
    display_graph()

