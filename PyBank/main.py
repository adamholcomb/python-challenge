
# Open CSV
import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")
print("-----------------------------------")


# Count number of months
with open(csvpath) as csvfile:
    budget = csv.reader(csvfile,delimiter = ",")
    header = next(budget)
    rowcounter = sum(1 for row in budget)
    print(rowcounter)
    
# Sum profit and loss
with open(csvpath) as csvfile:
    budget = csv.reader(csvfile,delimiter = ",")
    header = next(budget)
    profitcounter = 0
    for row in budget:
        profit = int(row[1])
        profitcounter += profit
        #print(f"Total Months: {len(list(budget))}")
    print(f"${profitcounter}")

# Average of changes in profit over period
    