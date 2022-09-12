import pandas as pd
import click
import glob


default_folder = "../../Data/30min/Yearly_data"


@click.command()
@click.option(
    "--folder",
    default=default_folder,
    type=click.STRING,
    help="The folder to look in, to change the parquet files.",
)
def main(folder: str):

    # get all file names
    files = glob.glob(folder + "/*.parquet")
    files = sorted(files)

    print(f"Found {len(files)} files in {folder}")

    for file in files:
        print(f"Reading file {file}")
        data = pd.read_parquet(file)

        # unstack
        print("Formating")
        data_unstacked = data.unstack()

        # join
        data_unstacked = data_unstacked.reset_index()
        data["level_1"] = data.index
        data_reduce = data[["ss_id", "date"]]
        data_joined = data_unstacked.join(data_reduce, on="level_1")

        # filter
        data_joined = data_joined[data_joined["level_0"] != "ss_id"]
        data_joined = data_joined[data_joined["level_0"] != "date"]

        # format datetime
        data_joined["level_0"] = data_joined["level_0"].str[1:].astype(int)
        data_joined["minutes"] = (data_joined["level_0"] - 1) * 30
        data_joined["minutes"] = pd.to_timedelta(data_joined["minutes"], unit="m")
        data_joined["datetime"] = data_joined["minutes"] + pd.to_datetime(data_joined["date"])

        # final format
        data_joined = data_joined.rename(columns={0: "generation_wh"})
        data_joined = data_joined[["datetime", "generation_wh", "ss_id"]]

        print("Save file")
        data_joined.to_parquet(file)


if __name__ == "__main__":
    main()
