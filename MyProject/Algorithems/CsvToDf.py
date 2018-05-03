import pandas as pd


def Run(path):
    # READ CSV
    print("Reading csv file..")
    df = pd.read_csv(path)
    print("Finish to read csv file")

    # DROP UNNECESSARY COLUMNS
    keep_col=[]
    df=df[keep_col]

    return df