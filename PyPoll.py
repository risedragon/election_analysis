import os, csv


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
canditates = []
candidate_votes = {}

with open(file_to_load,'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        canditate = row[2]
        total_votes += 1
        if canditate not in canditates:
            candidate_votes[canditate] = 0
            canditates.append(row[2])
        candidate_votes[canditate] += 1

winner = []
winner_votes = 0
winner_percentage = 0


for canditate in canditates:
    votes = candidate_votes[canditate]
    percentage = votes/total_votes
    if votes > winner_votes:
        winner = canditate
        winner_votes = votes
        winner_percentage = percentage
    print(canditate, f'{percentage:.2%}\n')


winning_candidate_summary = f'''
----------------------------\n
Winner: {winner}\n
Winning Vote Count: {winner_votes}\n
Winning Percentage: {winner_percentage:.2%}\n
-----------------------------
'''

print(winning_candidate_summary)

with open(file_to_save,"w") as f:
    f.write(winning_candidate_summary)
