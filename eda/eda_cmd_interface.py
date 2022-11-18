from graphs import singleday_pv_output
import click

@click.command()
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

def display_graph(downloads_path,metafilename, netcdffilename, nopvdata):
    disp = singleday_pv_output(
        downloads_path = downloads_path, 
        metafilename = metafilename, 
        netcdffilename = netcdffilename)
    disp.loading_xr_netcdf()
    disp.pv_singleday_output_display(
        no_pv_df_path = nopvdata)

if __name__ == "__main__":
    display_graph()

