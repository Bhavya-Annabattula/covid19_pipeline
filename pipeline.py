import pandas as pd
import matplotlib.pyplot as plt


class CovidPipeline:

    def __init__(self, file):
        self.file = file
        self.df = None


    def load_data(self):
        try:
            self.df = pd.read_csv(self.file, index_col=0)
            print("Data Loaded Successfully")
            print(self.df.head())
        except FileNotFoundError:
            print(f"Error: File '{self.file}' not found. Please check the file path.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")


    
    def clean_data(self):

        
        if "time_hms" in self.df.columns:
            self.df = self.df.drop(columns=["time_hms"])

        
        self.df = self.df.dropna()

        print("Data Cleaned")


    
    def analyze_data(self):

        continent_cases = self.df.groupby("continent")["cases.total"].sum()

        print("\nTotal Cases Per Continent:")
        print(continent_cases)

        return continent_cases


    
    def visualize_data(self):

        continent_cases = self.df.groupby("continent")["cases.total"].sum()

        continent_cases.plot(kind="bar")

        plt.title("COVID-19 Total Cases by Continent")
        plt.xlabel("Continent")
        plt.ylabel("Total Cases")

        plt.show()

if __name__ == "__main__":

    pipeline = CovidPipeline("covid19_stat.csv")

    pipeline.load_data()

    pipeline.clean_data()

    pipeline.analyze_data()
    

    pipeline.visualize_data()
