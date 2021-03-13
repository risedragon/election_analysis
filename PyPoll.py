import os, csv


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

data = []
with open(file_to_load,'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        data.append(row)

totalNumber = len(data)
