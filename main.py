# Import the required library
import pandas as pd

# Load the csv file and convert it to be a pandas dataframe
df = pd.read_csv("call_logging.csv")


# How many channels are typically required for a single call? 

# Group by user
user_grp = df.groupby(["userId"])

# Get channels that were used only once by each user 
print(user_grp["channelName"].value_counts().loc[lambda x: x == 1])
