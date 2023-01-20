import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class PlayerClustering:
    def __init__(self, player_data_file):
        self.player_data = pd.read_csv(player_data_file)
        self.model = None

    def createClusters(self):
        # Create a new column for visit frequency within the last three months
        self.player_data["visit_frequency"] = self.player_data["visits_3_months"] / 90

        # Create a new column for total theo within the last three months
        self.player_data["total_theo"] = self.player_data["theo_3_months"]

        # Define x and y for KMeans
        x = self.player_data[["visit_frequency", "total_theo"]]

        # Create a KMeans model (2 clusters for high-freq and low-freq)
        self.model = KMeans(n_clusters=2)
        # Fit the model to the data
        self.model.fit(x)   
        # Add a new column to the player data for the cluster label
        self.player_data["cluster"] = self.model.labels_


    def getClusters(self):
        # Separate the data into two clusters: high frequency players and low frequency players
        high_frequency_players = self.player_data[self.player_data["cluster"] == 0]
        low_frequency_players = self.player_data[self.player_data["cluster"] == 1]
        return high_frequency_players, low_frequency_players

    def plotClusters(self):
        high_frequency_players, low_frequency_players = self.get_clusters()

        plt.scatter(high_frequency_players["visit_frequency"], high_frequency_players["total_theo"], c='red', label = 'High Frequency')
        plt.scatter(low_frequency_players["visit_frequency"], low_frequency_players["total_theo"], c='blue', label = 'Low Frequency')

        plt.xlabel("Visit Frequency (Visits per Day)")
        plt.ylabel("total Theo (USD)")
        plt.legend()
        plt.show()