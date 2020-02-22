#This is where the polling data will be read
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv




#Initialize variables to store and count the data from the file
Vote_Count = 0
Candidate_Totals = []
Candidate_List = []
Votes_List = []
total = 0

def VotesForCandidate(candidate):
    Voters = 0
    for row in Candidate_List:
       
        if str(Candidate_List[row[0]]) == candidate:
            Voters += 1

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
        Candidate_Totals.append(row[2])

#Looks through candidate list to get the complete list of candidates and stores them in a new list
for j,x in enumerate(Candidate_Totals):
    
    #Adds the candidate in the first index to the list
    if j == 0:
        Candidate_List.append(Candidate_Totals[j])
    else:
        #Checks when the name changes on the list
        if Candidate_Totals[j-1] != Candidate_Totals[j]:
            #Checks if the candidate's name is on the new list. If it is, keep going. If not, adds the name to the list
            if Candidate_Totals[j] in Candidate_List:
                continue    
            else:
                Candidate_List.append(Candidate_Totals[j])

            
        

print(Candidate_List)


    

#Check to see if the Lists were created correctly
#for i in range(10):
#  print(f"{Candidate_List[i]} ")



#Prints out the analysis to the terminal
#print("Election Results")
#print("------------------------")
print(f"Total Votes: {Vote_Count}")
#print(f"Total Profits: ${round(Net_Total)}")
#print(f"Average Change: ${round(average,2)}")
#print(f"Greatest Increase in Profits: {greatest_profit_month} (${round(greatest_profit)}) ")
#print(f"Greatest Decrease in Profits: {greatest_losses_month} (${round(greatest_losses)}) ")

 
# Open the file using "write" mode
#output_path = os.path.join("PyBankAnalysis.txt")

#f = open(output_path, 'w')

#*f.write("Financial Analysis \n")
#f.write("------------------------\n")
#f.write(f"Total Months: {Date_Count}\n")
#f.write(f"Total Profits: ${round(Net_Total)}\n")
#f.write(f"Average Change: ${round(average,2)}\n")
#f.write(f"Greatest Increase in Profits: {greatest_profit_month} (${round(greatest_profit)})\n")
#f.write(f"Greatest Decrease in Profits: {greatest_losses_month} (${round(greatest_losses)})\n")

#f.close()
