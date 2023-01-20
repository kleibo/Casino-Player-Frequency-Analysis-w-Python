import pandas as pd
from sklearn.cluster import KMeans

# Load in player data
player_data = pd.read_csv("player_data.csv")

# Create a new column for visit frequency within the last three months
player_data["visit_frequency"] = player_data["visits_3_months"] / 90

# Create a new column for total theo within the last three months
player_data["total_theo"] = player_data["lpd3_TotalTheo"]

# Define x and y for KMeans
x = player_data[["visit_frequency", "total_theo"]]

# Define the number of clusters (2 for high-freq and low-freq)
num_clusters = 2

# Create a KMeans model
kmeans = KMeans(n_clusters=num_clusters)


# Fit the model to the data
kmeans.fit(x)


# Add a new column to the player data for the cluster label
player_data["cluster"] = kmeans.labels_

# Separate the data into two clusters: high frequency players and low frequency players
high_frequency_players = player_data[player_data["cluster"] == 0]
low_frequency_players = player_data[player_data["cluster"] == 1]

# Print the number of players in each cluster
print("Number of high frequency players: ", len(high_frequency_players))
print("Number of low frequency players: ", len(low_frequency_players))