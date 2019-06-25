#Klug Homework: PyPoll
import os
import csv

csvpath = os.path.join("..","PyPoll","election_data.csv")

#variables
totalVotes = 0
totalVoteKhan = 0
totalVoteCorrey = 0
totalVoteLi = 0
totalVoteTooley = 0

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    print(f'Election Results')
    print(f'--------------------')
    
    for v in csvreader:
        voter = v[0]
        county = v[1]
        candidate = v[2]
        
        totalVotes = totalVotes + 1
        
        if candidate == "Khan":
            totalVoteKhan = totalVoteKhan + 1
        if candidate == "Correy":
            totalVoteCorrey = totalVoteCorrey + 1
        if candidate == "Li": 
            totalVoteLi = totalVoteLi + 1
        if candidate == "O'Tooley":
            totalVoteTooley = totalVoteTooley + 1
            
percentKhan = round((totalVoteKhan / totalVotes) * 100,3)
percentCorrey = round((totalVoteCorrey / totalVotes) * 100,3)
percentLi = round((totalVoteLi / totalVotes) * 100,3)
percentTooley = round((totalVoteTooley / totalVotes) * 100,3) 

print(f'Total Votes: {totalVotes}')
print(f'--------------------')
print(f'Khan: {percentKhan}% ({totalVoteKhan})')
print(f'Correy: {percentCorrey}% ({totalVoteCorrey})')
print(f'Li: {percentLi}% ({totalVoteLi})')
print(f"O'Tooley: {percentTooley}% ({totalVoteTooley})")
print(f'--------------------')

if totalVoteKhan > totalVoteCorrey and totalVoteKhan > totalVoteLi and totalVoteKhan > totalVoteTooley:
    print(f'Winner: Khan')   
elif totalVoteCorrey > totalVoteKhan and totalVoteCorrey > totalVoteLi and totalVoteCorrey > totalVoteTooley:
    print(f'Winner: Correy')
elif totalVoteLi > totalVoteKhan and totalVoteLi > totalVoteCorrey and totalVoteLi > totalVoteTooley:
    print(f'Winner: Li')
else:
    print(f"Winner: O'Tooley")
print(f'--------------------')