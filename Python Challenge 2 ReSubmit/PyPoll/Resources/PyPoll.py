import os
import csv

# Create path for csv files
datapath = os.path.join("Resources","election_data.csv")

# Declare Variables 
total_number_votes = []
candidates_list =[]
votes_per_candidate = []
percentage_per_candidate = ["", 0]
winner_per_election = []
greatest_decrease = ["", 0]
title = "Election Results"

# Open csv files
with open(datapath) as ElectionData:
    reader = csv.reader(ElectionData)

    # Skips header as data to be included
    header = next(reader)
#print title
    for row in reader:
# The total number of months included in the dataset        
        total_number_votes.append(row[0])
        #total_profit_loss.append(row[1])
    
    print(title)
    print("-------------------------------")
    print(f"Total votes: {len(total_number_votes)}")

# The total number of votes cast

# A complete list of candidates who received votes
    
# The percentage of votes each candidate won
    
# The total number of votes each candidate won
    
# The winner of the election based on popular vote