import os, csv


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate option and candidate votes
canditates = []
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load,'r') as f:
    reader = csv.reader(f)
    # Read the header row.
    next(reader)

    # each row in the CSV file
    for row in reader:
        #count total vote count
        total_votes += 1
        #candidate name of current row
        canditate = row[2]
        # if this candidate is not in candidates option, then add it in the list and candidate votes list 
        if canditate not in canditates:
            candidate_votes[canditate] = 0
            canditates.append(canditate)
        #current candidate vote number plus one
        candidate_votes[canditate] += 1

#Save results to file
with open(file_to_save,"w") as f:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        )
    print(election_results, end="")
    f.write(election_results)

# Track the winning candidate, vote count, and percentage
    winner = []
    winner_votes = 0
    winner_percentage = 0

    # read each canditate and vote number
    for canditate in canditates:
        votes = candidate_votes[canditate]
        percentage = votes/total_votes
        candidate_result = f"{canditate}: {percentage:.2%} {votes:,}\n"
        print(candidate_result)
        f.write(candidate_result)
        #print(canditate, f'{percentage:.2%}\n')

        #Determine winner
        if votes > winner_votes:
            winner = canditate
            winner_votes = votes
            winner_percentage = percentage

    #Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winner_votes}\n"
    f"Winning Percentage: {winner_percentage:.2%}\n"
    f"-----------------------------"
    )
    print(winning_candidate_summary)
    f.write(winning_candidate_summary)

