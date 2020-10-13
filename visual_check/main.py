import pandas as pd
from visual import *

if __name__ == '__main__':
    df = pd.read_excel("sources/metric1000.xlsx")
    df = df.rename(columns={"Column1": "address"})
    df = df.fillna("")
    df = df.sample(n=10)
    df = df.reset_index()

    interface(df)
