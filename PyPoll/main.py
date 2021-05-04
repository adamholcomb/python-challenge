# Open CSV
import os
import csv
csvpath = os.path.join("Resources","election_data.csv")

# Create dictionary to store data
polldict = {}

with open(csvpath) as csvfile:
    polldata = csv.reader(csvfile, delimiter=",")
    csv_header = next(polldata)

    # Add data to dictionary
    polldict = {rows[2]:rows[1] for rows in polldata}

# Print Headers
print("Election Results")
print("---------------------------")

# Total Votes
print(f"Total Votes: {len(polldict)}")
print("---------------------------")

# List of Vote-Recieving Candidates

for candidate,county in polldict.items():
    print(candidate)