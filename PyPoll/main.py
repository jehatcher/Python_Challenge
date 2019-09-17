# open file
import os
import csv
import numpy as np
import pandas as pd

# Path to collect data from the Resources folder
data_poll= "Resources/election_data.csv"
data_df=pd.read_csv(data_poll)

#Voter ID,County,Candidate
voter_ID=data_df["Voter ID"]
candidate=data_df["Candidate"]

# total number of vote
vote_count=np.size(voter_ID)
# A complete list of candidates who received votes
votes=data_df.Candidate.value_counts()

# The percentage of votes each candidate won change numbers to int
Total_votes=votes/vote_count

# The winner of the election based on popular vote
winner=max(Total_votes)

# print out results

print(" Election Results")
print("-------------------------")
print(f'Count {vote_count}')
print("-------------------------")
print(round(Total_votes*100))
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")
# print to text file

