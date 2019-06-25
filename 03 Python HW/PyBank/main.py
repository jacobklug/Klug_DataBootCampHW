#Klug Homework: PyBank
import os 
import csv

csvpath = os.path.join('..', 'PyBank','budget_data.csv')

#variables
monthCount = 0
totalPL = 0
pretotal = 0
Diff = 0
maxDiff = 0
minDiff = 0
totalDiff = 0
Diffs = []

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    print(f'Financial Analysis')
    print(f'-------------------')
    
    for i in csvreader:
        month = i[0]
        total = i[1]
        Diff = int(total) - int(pretotal)
        
        if maxDiff < Diff: 
            maxDiff = Diff
            maxDiffMonth = month
        if minDiff > Diff:
            minDiff = Diff
            minDiffMonth = month
            
        pretotal = int(total)
        
        monthCount = monthCount + 1
        totalPL += int(total)
        totalDiff += Diff

avgDiff = totalDiff / monthCount
averageDiff = round(avgDiff)
      
print(f'Total months: {monthCount}')
print(f'Total Profit: ${totalPL}')
print(f'Average Change: ${averageDiff}')
print(f'Greatest Increase in Profits: {maxDiffMonth} (${maxDiff})')
print(f'Greatest Decrease in Profits: {minDiffMonth} (${minDiff})')
