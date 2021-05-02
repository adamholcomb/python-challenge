
# Open CSV
import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    budget = csv.reader(csvfile,delimiter = ",")
    #header = next(budget)
    print("Financial Analysis")
    print("-----------------------------------")
    # Count number of months
    for row in budget:
        print(f"Total Months: {len(list(budget))}")
     
    # Sum profits/losses
        
        