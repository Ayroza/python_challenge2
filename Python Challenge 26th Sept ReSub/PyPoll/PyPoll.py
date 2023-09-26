import os
import csv

# Create path for csv files
datapath = os.path.join("Resources","election_data.csv")

# Declare Variables 
total_number_votes = []
candidates_list =[]
votes_per_candidate = {}
percentage_per_candidate = {}
winner_per_election = []
greatest_decrease = ["", 0]
title = "Election Results"
#candidate_name = 

# Open csv files
with open(datapath) as ElectionData:
    reader = csv.reader(ElectionData)

    # Skips header as data to be included
    header = next(reader)
#print title
    for row in reader:
#The total number of votes cast      
        total_number_votes.append(row[0])
# A complete list of candidates who received votes
# The total number of votes each candidate won 
        candidates_list.append(row[2])
        if row[2] not in votes_per_candidate.keys():
            votes_per_candidate[row[2]] = 0
        votes_per_candidate[row[2]] += 1

    print(title)
    print("-------------------------------")
    print(f"Total votes: {len(total_number_votes)}")
    print("-------------------------------")
#The percentage of votes each candidate won
    unique_candidates = set(candidates_list)
    for k, v in votes_per_candidate.items():
        percentage_per_candidate[k] = (v / len(total_number_votes)) * 100
        print(f'{k}: {percentage_per_candidate[k]:.3f}% ({v})')

    #print(str(round{percentage_per_candidate,2})+"%")
    #print(f'{percentage_per_candidate:.2f}%')
    
# The winner of the election based on popular vote
file_to_save = os.path.join('Analysis', 'pypoll_analysis.txt')
with open(file_to_save, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------------\n')
    txtfile.write(f'Total votes: {len(total_number_votes)}\n')
    txtfile.write('-------------------------------\n')
    txtfile.write(f'{k}: {percentage_per_candidate[k]:.3f}% ({v})')    