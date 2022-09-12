import glob
import pandas as pd
import click

default_folder = "../../Data/30min/Yearly_data"


@click.command()
@click.option(
    "--folder",
    default=default_folder,
    type=click.STRING,
    help="The folder to look in, to change the parquet files.",
)
@click.option(
    "--filename",
    default="all.parquet",
    type=click.STRING,
    help="The output filename (should end in .parquet)",
)
def main(folder: str, filename: str):

    # get all file names
    files = glob.glob(folder + "/*.parquet")
    files = sorted(files)

    print(f"Found {len(files)} files in {folder}")

    data_all_df = []
    for file in files:
        print(f"loading {file}")
        data_df = pd.read_parquet(file)
        data_all_df.append(data_df)

    print("merging file")
    data_all_df = pd.concat(data_all_df)
    data_all_df["timestamp"] = pd.to_datetime(data_all_df["timestamp"])
    data_all_df.reset_index(inplace=True)
    print(data_all_df.head())

    print(f"Saving")
    data_all_df.to_parquet(filename, engine="pyarrow", index=False)


if __name__ == "__main__":
    main()
