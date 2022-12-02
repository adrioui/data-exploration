# Import the required library
import pandas as pd

# Load the csv file and convert it to be a pandas dataframe
df = pd.read_csv("call_logging.csv")
# Change the time format in dataframe to make the process easier
df["time"] = pd.to_datetime(df["time"],unit="s")


# How many channels are typically required for a single call? 

filter = (df["userId"].value_counts() == 1)
print(filter)
