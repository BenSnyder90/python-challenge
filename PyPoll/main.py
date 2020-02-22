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
Vote_Percentage = []

#Creates a function that runs through the votes and assigns them to
#the candidate they voted for
def VotesForCandidate(candidate):
    #Sets the voter count to 0
    Voters = 0

    for i in Candidate_Totals:
       #Looks through the list of votes and compares it to the given candidate
       #If the names match, one vote is added to the count
        if i == candidate:
            Voters += 1
 
    return Voters


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

#Get the vote totals for a specific candidate and adds to a list            
for x in Candidate_List:
    Votes_List.append(VotesForCandidate(x))

#Gets the percentage of total votes for each candidate and stores it in a list
for x in Votes_List:
    Votes = round((x / Vote_Count) * 100,0)
    Vote_Percentage.append(Votes)


Winner = Votes_List[0]
Winner_Name = Candidate_List[0]

for x in range(len(Candidate_List)):
    if Votes_List[x] > Winner:
        Winner = Votes_List[x]
        Winner_Name = Candidate_List[x]
#print(Votes_List)
#print(Vote_Percentage)

#Prints out the analysis to the terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {Vote_Count}")
print("------------------------")
for x in range(len(Candidate_List)):
    print(f"{Candidate_List[x]}: {Vote_Percentage[x]}% ({Votes_List[x]}) ")
print("------------------------")
print(f"Winner: {Winner_Name}")
print("------------------------")   


 
# Open the file using "write" mode
output_path = os.path.join("Output","PyPollAnalysis.txt")

f = open(output_path, 'w')

f.write("Election Results \n")
f.write("------------------------\n")
f.write(f"Total Votes: {Vote_Count}\n")
f.write("------------------------\n")
for x in range(len(Candidate_List)):
    f.write(f"{Candidate_List[x]}: {Vote_Percentage[x]}% ({Votes_List[x]})\n")
f.write("------------------------\n")
f.write(f"Winner: {Winner_Name}\n")
f.write("------------------------\n") 

f.close()