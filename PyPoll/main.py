# Open CSV
import os
import csv
csvpath = os.path.join("Resources","election_data.csv")

# Create dictionary to store data
polldict = {}

with open(csvpath) as csvfile:
    polldata = csv.reader(csvfile, delimiter=",")
    csv_header = next(polldata)
    