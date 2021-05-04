# Open CSV
import os
import csv
csvpath = os.path.join("Resources","election_data.csv")

# Create dictionary to count total votes
polldict = {}
with open(csvpath) as csvfile:
    polldata = csv.reader(csvfile, delimiter=",")
    csv_header = next(polldata)
    for row in polldata:
        if row[2] in polldict:
            polldict[row[2]] += 1
        else:
            polldict[row[2]] = 1
    print("Election Results")
    print("---------------------------")
    totalvotes = sum(polldict.values())
    print(f"Total Votes: {totalvotes}")
    print("---------------------------")

    for key, value in polldict.items():
        print(f"{key}: {round(value/totalvotes*100,2)}%, {value} votes")
    print("---------------------------")

