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

# Add winner
#winner = (dict((v,k) for k,v in polldict.items()).get(max(polldict.values())))
    winner_count = 0
    for key in polldict.keys():
        if polldict[key] > winner_count:
            winner = key
            winner_count = polldict[key]
    print(f"Winner: {winner}")  
    print("---------------------------")

# Write output file
    outpath = os.path.join("Analysis","pypoll_output.txt")
    output = open(outpath,"w")
    output.write("Election Results\n")
    output.write("---------------------------\n")
    output.write(f"Total Votes: {totalvotes}\n")
    output.write("---------------------------\n")
    for key, value in polldict.items():
            output.write(f"{key}: {round(value/totalvotes*100,2)}%, {value} votes\n")
    output.write("---------------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write("---------------------------\n")
    
