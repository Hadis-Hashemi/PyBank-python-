#This code read the data from a csv file and analyzes the records to calculate the following parameters:
#total months
#total net profit/loss
#max changes in profit/loss
#min changes in profit/loss
#finally, the results are exported to a text file

##Import packages and read input file
import os
import csv

# Path to collect data from the Resources folder
Csvpath = os.path.join("Resources/","budget_data.csv.csv")

## Evaluation
# with open as csvfile:
with open(Csvpath,'r') as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None) # skip the header
    
# Initialize the variables
    total=0 #total amount of Profit/Loss
    lastrow=0 # earlier reported date than current date
    totaldelta=0 # sum of change in Profit/Loss
    max_delta=0 # max. of change in Profit/Loss
    min_delta=0 # min. of change in Profit/Loss
    delta=0 # change in Profit/Loss
    
# Loop through each row of data
    for i, row in enumerate(csvreader):
        total += float(row[1]) #caluclate the net total amount of Profit/Loss
        #caluclate the changes in profit/loss
        if i>0:
            delta=float(row[1])-lastrow
        lastrow=float(row[1])
        totaldelta += delta
        # calculate the max of changes in profit/loss
        if delta> max_delta:
            max_delta=delta
            index_max=row[0]      
        
        # calculate the max of changes in profit/loss
        if delta < min_delta:
            min_delta=delta
            index_min=row[0]

##write results to console and text file
   
print(f'Total months: {i+1}')
print(f'Total: ${total}') 
print(f'Average Change:${totaldelta/(i)}')
print(f'Greatest Increase in Profits:{index_max}(${max_delta})')
print(f'Greatest Decrease in Profits: {index_min}(${min_delta})')

output_file=open("newPybank.txt",'w')
output_file.write(f'Total months:{i+1}\nTotal:${total}\nAverage Change: $({totaldelta/(i)}\n')
output_file.write(f'Greatest Increase in Profits:{index_max}${max_delta}\nGreatest Decrease in Profits:{index_min}(${min_delta})')
output_file.close()                  
                   