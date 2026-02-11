#importing the pandas package in order to be able to use dataframes
import pandas as pd

#loading the dataset into a pandas dataframe:
data_frame = pd.read_csv("crime.csv")

#create a new colum called 'risk':
data_frame["risk"] = data_frame["ViolentCrimesPerPop"].apply(
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime"
)

#now we will group by risk and calculate the average unemployment rate:
average_unemployment_rate = data_frame.groupby("risk")["PctUnemployed"].mean()

#finally, printing the results:
for risk_level, average_rate in average_unemployment_rate.items():
    print(f"{risk_level}: {average_rate}")

