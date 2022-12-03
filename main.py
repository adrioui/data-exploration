# Import the required library
import pandas as pd


# Load the csv file and convert it to be a pandas dataframe
df = pd.read_csv("call_logging.csv")
df["time"] = pd.to_datetime(df["time"], unit="s")


# How many channels are typically required for a single call? 

# Count the channels used for each customer
# Deactivate multiindexing for easier use
channels_used = df.groupby(["userId"], as_index=False)["channelName"].value_counts()

# Count how many channels that were used only once for each customer
counts_of_channels_used_only_once = channels_used.groupby(["userId"]).sum()

# Convert groupby series to dataframe and reset the index
user_df = pd.DataFrame(counts_of_channels_used_only_once).reset_index()

# Rename one of its columns
user_df.rename(columns={"count": "counts_of_channels_used_only_once"}, inplace=True)

# Channels typically used for a single call
# Use arithmetic mean because there is no outlier
answer_1 = channels_typically_required_for_a_single_call = int(user_df["counts_of_channels_used_only_once"].mean(numeric_only=True).round())