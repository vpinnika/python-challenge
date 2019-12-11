# Importing the required Modules
import os
import csv
import sys

# Assuming CSV file and main.py files will be stored in the same directory
# Defining the file object
# os.path.join(sys.path[0] pointing to the same path as the main.py exists in
election_data_csv = os.path.join(sys.path[0], 'election_data.csv')

# Declaring the Variables
total_votes = 0
max_votes = 0
max_votes_index = 0
candidates = []
candidate_votes = []
candidate_votes_percent =[]

# Opening the file for windows
with open(election_data_csv, newline="", encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    
     #Reading the header row to skip 
    csv_header = next(csvreader)

    # Reading from second row to last row to get the expected output
    for row in csvreader:
        # Adding 1 to total votes for each record
        total_votes += 1

        # If candidate not exists in the list then add the condiate to the candiates[] list, and add 1 to the candidate_votes[] list 
        # Else add 1 to the candidate _votes[] list for corresponding candidate        
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1

# Calculating the vote percentage
for c_votes in candidate_votes:     
    vote_percent = format(round((c_votes / total_votes)*100),'.3f') # Rounding the number and taking 3 zeeros after decimal
    candidate_votes_percent.append(vote_percent)
    
# Find out the Winner
winner_votes = max(candidate_votes) 
winner_index = candidate_votes.index(winner_votes)
winner = candidates[winner_index]

#Printing Output to the terminal
print('Election Results')
print('-------------------------')
print(f"Total Votes: {str(total_votes)}")
print('-------------------------')
for i in range(len(candidates)):
    print(f"{candidates[i]}: {candidate_votes_percent[i]}% ({candidate_votes[i]})")
print('-------------------------')
print(f"Winner: {winner}")
print('-------------------------')

# Exporting the data into a text file
# Defining the file name and path
output_file = os.path.join(sys.path[0], 'Election_Results_Summary.txt')

# Opening the file and wrting into the file
with open(output_file,"w") as output_file:    
    output_file.write('Election Results\n')
    output_file.write('--------------------------\n')
    output_file.write(f"Total Votes: {str(total_votes)}\n")
    output_file.write('--------------------------\n')
    for i in range(len(candidates)):
        output_file.write(f"{candidates[i]}: {candidate_votes_percent[i]}% ({candidate_votes[i]})\n")
    output_file.write('--------------------------\n')
    output_file.write(f"Winner: {winner}\n")
    output_file.write('--------------------------\n')

# End of the program