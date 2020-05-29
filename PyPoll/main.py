#In this code a set of pull data will read and analyzed as follows:
#- The total number of votes cast
#- complete list of candidates who received votes
#- The percentage of votes each candidate won
#- The total number of votes each candidate won
#- The winner of the election based on popular vote

#Finally, the results will be exported to text file 

## Import packages and read input file
import os 
import csv

# Path to collect data from the Resources folder
Csvpath = os.path.join("Resources/","election_data.csv")

# with open as csvfile:
with open(Csvpath,'r') as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None) # skip the header

    total_vote = 0 # Initialize the variables

    candidate_list=[] #create the list of candidate         
    candidate_vote=[] #create the list of canditates vote

#Loop through each row of data
    for row in csvreader:
        total_vote+=1 #caluclate the total number of votes
        if row[2] in candidate_list:  
            index_candidate=candidate_list.index(row[2])
            candidate_vote[index_candidate]+=1
        else:
            candidate_list.append(row[2])
            candidate_vote.append(1)
winner_index=candidate_vote.index(max(candidate_vote))
sum_list = sum(candidate_vote)

## write results to console and text file
      
print("Election Results")
print("----------------------------------------------------------")
print(f'Total Votes:{total_vote}')
print("------------------------------------------------------------")
for i in range(4):
    print(f'{candidate_list[i]}:{candidate_vote[i]/sum_list*100}% ({candidate_vote[i]})')
print("------------------------------------------------------------")
print(f'winner: {candidate_list[winner_index]}')
print("------------------------------------------------------------")

output_file=open("PyPoll.txt",'w')
output_file.write("Election Results")
output_file.write(f'\nTotal Votes:{total_vote}\n')
for i in range(4):
    output_file.write(f'{candidate_list[i]}:{candidate_vote[i]/sum_list*100}% ({candidate_vote[i]})\n')
output_file.write(f'winner: {candidate_list[winner_index]}')
output_file.close()  