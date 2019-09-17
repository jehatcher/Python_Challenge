import os
import csv
import numpy as np
import pandas as pd

# Path to collect data from the Resources folder
bank_data= "Resources/budget_data.csv"
bank_data_df=pd.read_csv(bank_data)

date_df=bank_data_df["Date"]
budget_df=bank_data_df["Profit/Losses"]

mounths_count=np.size(date_df)

# total budget
budget_total=np.sum(budget_df)
# average Change
budget_average=round(np.mean(budget_df))

# Greatest Increase in Profits
#budget_max=pd.max(bank_data_df)
budget_max=np.max(budget_df)
 #Greatest Decrease in Profits
budget_min=np.min(budget_df)

    # print script
print("Financial Analysis")
print("------------------")
print(f'Total Months: {mounths_count}')
print(f'Total: {budget_total}')
print(f'Average  Change: {budget_average}')
print(f'Greatest Increase in Profits: {budget_max}')
print(f'Greatest Decrease in Profits: {budget_min}')