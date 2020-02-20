# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Initialize variables to store and count the data from the file
Date_Count = 0
Net_Total = 0
ProfitsLosses = []
MonthCounter = []
MonthlyChanges = []
total = 0


#Create variable for file path to the datafile
csvpath = os.path.join('Resources', 'budget_data.csv')


# Open the CSV
with open(csvpath, newline="",encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Skip the header line
    next(csvfile)

    # Loop through each row to get data and add them to their respective lists
    for row in csvreader:
        Date_Count += 1
        Net_Total += float(row[1])
        
        #Stores monthly financial changes in a list
        ProfitsLosses.append(float(row[1]))
        
        #Stores the month counter into a list
        MonthCounter.append(row[0])

    

#Check to see if the Lists were created correctly
#for i in range(10):
#    print(f"{ProfitsLosses[i]}  {MonthCounter[i]}")

#Tracks the monthly changes in profits/losses and stores them in a new list
for j,x in enumerate(ProfitsLosses):
    if j == 0:
        MonthlyChanges.append(0)
    else:
        pre = ProfitsLosses[j-1]
        post = ProfitsLosses[j]
        change = post - pre
        MonthlyChanges.append(change)

#Check to see if the MonthlyChanges list works

#print(f"{MonthlyChanges}")

#Finds the average of the changes in Profits/Losses over the period
for c,x in enumerate(MonthlyChanges):
    total += MonthlyChanges[int(c)]

#Finds the average, taking away 1 from the length to account for the first month not being tracked
average = total / (len(MonthlyChanges)-1)

#Looks through the average changes list and tracks which one is the greatest increase in profits, storing the value and month in variables
greatest_profit = MonthlyChanges[0]
greatest_profit_month = MonthCounter[0]
greatest_losses = MonthlyChanges[0]
greatest_losses_month = MonthCounter[0]

for i,x in enumerate(MonthlyChanges[1:]):
    if MonthlyChanges[i] > greatest_profit:
        greatest_profit = MonthlyChanges[i]
        greatest_profit_month = MonthCounter[i]

for i,x in enumerate(MonthlyChanges[1:]):
    if MonthlyChanges[i] < greatest_losses:
        greatest_losses = MonthlyChanges[i]
        greatest_losses_month = MonthCounter[i]

#Prints out the analysis to the terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {Date_Count}")
print(f"Total Profits: ${round(Net_Total)}")
print(f"Average Change: ${round(average,2)}")
print(f"Greatest Increase in Profits: {greatest_profit_month} (${round(greatest_profit)}) ")
print(f"Greatest Decrease in Profits: {greatest_losses_month} (${round(greatest_losses)}) ")

 
# Open the file using "write" mode
output_path = os.path.join("PyBankAnalysis.txt")

f = open(output_path, 'w')

f.write("Financial Analysis \n")
f.write("------------------------\n")
f.write(f"Total Months: {Date_Count}\n")
f.write(f"Total Profits: ${round(Net_Total)}\n")
f.write(f"Average Change: ${round(average,2)}\n")
f.write(f"Greatest Increase in Profits: {greatest_profit_month} (${round(greatest_profit)})\n")
f.write(f"Greatest Decrease in Profits: {greatest_losses_month} (${round(greatest_losses)})\n")

f.close()
