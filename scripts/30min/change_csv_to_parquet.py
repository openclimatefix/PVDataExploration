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
def main(folder: str):

    # get all file names
    files = glob.glob(folder + "/*.csv.gz")
    files = sorted(files)

    print(f"Found {len(files)} in folder {folder}")

    for file in files:
        print(f"loading {file}")
        data_df = pd.read_csv(file)

        data_df["timestamp"] = pd.to_datetime(data_df["timestamp"])
        data_df = data_df.rename(columns={"0", "value"})
        data_df = data_df[["value", "timestamp", "ss_id"]]

        file = file.replace(".csv.gz", ".parquet")
        print(f"Saving {file}")
        data_df.to_parquet(file, engine="pyarrow", index=False)


if __name__ == "__main__":
    main()
