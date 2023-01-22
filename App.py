from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PlayerClustering

class Main:
    def __init__(self):
        self.filepath = ""

    
    # Open a file dialog to select the player data file
    def openFileDialog(self):
        root = Tk()
        root.withdraw()
        filepath = askopenfilename()
        # Check if the user selected a file
        if not self.filepath:
            print("No file selected. Exiting program.")
            exit()   

    def runClustering(self):
        clustering = PlayerClustering.PlayerClustering(self.filepath)
        # Create a PlayerClustering object and cluster the players
        clustering.create_clusters()
        # Plot the clusters
        clustering.plot_clusters()
        # Save Results
        clustering.saveResults()

if __name__ == "__main__":
    main = Main()
    main.openFileDialog()
    main.runClustering()