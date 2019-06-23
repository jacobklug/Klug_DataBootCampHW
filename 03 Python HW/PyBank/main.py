#Klug Homework: PyBank
import os 
import csv

csvpath = os.path.join('..', 'PyBank','budget_data.csv')

#variables
monthCount = 0
totalPL = 0
avgDiff = 0
maxDiff = 0
minDiff = 0

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    print(f'Financial Analysis')
    print(f'-------------------')
    
    for i in csvreader:
        month = i[0]
        total = i[1]
        
        monthCount = monthCount + 1
        totalPL += int(total)
  

      
print(f'Total months: {monthCount}')
print(f'Total Profit: ${totalPL}')
        
