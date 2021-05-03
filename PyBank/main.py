
# Open CSV
import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
outputpath = os.path.join("Analysis", "pybank_output.txt")
textfile = open(outputpath,"w")

print("Financial Analysis")
textfile.write("Financial Analysis\n")
print("-----------------------------------")
textfile.write("--------------------------------\n")


# Count number of months
with open(csvpath) as csvfile:
    budget = csv.reader(csvfile,delimiter = ",")
    header = next(budget)
    months = len(list(budget))
    print(f"Total Months: {months}")
    textfile.write(f"Total Months: {months}\n")
    
# Sum profit and loss
with open(csvpath) as csvfile:
    budget = csv.reader(csvfile,delimiter = ",")
    header = next(budget)
    profitcounter = 0
    for row in budget:
        profit = int(row[1])
        profitcounter += profit
    print(f"Total: ${profitcounter}")
    textfile.write(f"Total: ${profitcounter}\n")

# Average of changes in profit over period
profit = []
changes = []
with open(csvpath) as csvfile:
    budget = (csv.reader(csvfile,delimiter = ","))
    header = next(budget)    

    for row in budget:
        profit.append(int(row[1]))
    rowcounter = 0
    for row in profit:
        rowcounter += row
      
    for x in range(1,len(profit)):
        changes.append(profit[x]-profit[x-1])
    changecounter = 0
    for row in changes:
        changecounter += row
    average = (changecounter)/(len(changes))
    print(f"Average change: ${round(average,2)}")
    textfile.write(f"Average change: ${round(average,2)}\n")

# Greatest increase and decrease in revenue (date and amount)
with open(csvpath) as csvfile:
    budget = (csv.reader(csvfile,delimiter = ","))
    header = next(budget)    
    maxchange = max(changes)
    minchange = min(changes)
    dates = []
    for row in budget:
        dates.append(row[0])
    maxdate = dates[1+changes.index(max(changes))]
    mindate = dates[1+changes.index(min(changes))]
    
    print(f"Greatest increase in profits: {maxdate}, ${maxchange}")
    textfile.write(f"Greatest increase in profits: {maxdate}, ${maxchange}\n")
    print(f"Greatest decrease in profits: {mindate}, ${minchange}")
    textfile.write(f"Greatest decrease in profits: {mindate}, ${minchange}\n")

textfile.close

# Export text file: added code throughout in addition to print statements
