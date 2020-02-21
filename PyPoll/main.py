#This is where the polling data will be read
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Initialize variables to store and count the data from the file
Vote_Count = 0
Candidate_List = []
Votes_List = []
total = 0


#Create variable for file path to the datafile
csvpath = os.path.join('Resources', 'election_data.csv')


# Open the CSV
with open(csvpath, newline="",encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Skip the header line
    next(csvfile)

    
    for row in csvreader:
        
        #Adds one vote to the vote counter
        Vote_Count += 1

        #Adds the name of the candidate to a new list
        Candidate_list.append(row[2])

       

    

#Check to see if the Lists were created correctly
for i in range(10):
   print(f"{Candidate_List[i]} ")

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
print("Election Results")
print("------------------------")
print(f"Total Votes: {Vote_Count}")
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
