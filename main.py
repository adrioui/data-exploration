import pandas as pd

df = pd.read_csv("call_logging.csv")


# How many channels are typically required for a single call? 
some_cols = df.groupby("channelName")

filter = (df["userId"].value_counts() == 1)

print(filter)