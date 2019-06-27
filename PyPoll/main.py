import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
 
    
    candidates = {}
    count = 0
    votes_cast = 0
    vote_percentage = 0
    most_votes = 0
    most_voted = ""
    
    for row in csvreader:
        
        candidate = row[2]
        count = count + 1
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    
    print("Election Results")
    print("----------------------------------------")
    print(f"Total Votes: {count}")
    print("----------------------------------------")
    
    
    for candidate in candidates:
        votes_cast += candidates[candidate]
    
        vote_percentage = (candidates[candidate])/(count) * (100)
        print(f"{candidate}: {int(percent_of_votes)}% {votes_cast}")
        
        if candidates[candidate] > most_votes:
            most_voted = candidate
            most_votes = candidates[candidate]
        
    print("----------------------------------------")
    
    print(f"Winner: {Most_Voted}")
    
    print("----------------------------------------")

with open("budget_analysis.txt", "w") as text_file:
    print("Election Results"\n
          "----------------------------------------"\n
          f"Total Votes: {count}"\n
          "----------------------------------------"\n
          f"{candidate}: {int(percent_of_votes)}% {votes_cast}"\n  
          "----------------------------------------"\n
          f"Winner: {Most_Voted}"\n
          "----------------------------------------", file = text_file)
