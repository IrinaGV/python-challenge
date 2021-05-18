import os
import csv
import collections


file=os.path.join('Resources','election_data.csv')
total=0
total_votes=0
count = collections.Counter()
candidate = []
voter_ID = []



with open(file,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    #print(header)
    
    for row in csvreader:
        total_votes +=1
        candidate.append(row[2])
        voter_ID.append(row[0])
    #print(total_votes)
    new_candidate = list(dict.fromkeys(candidate))
    #print(new_candidate)
    
    #new_khan = candidate.remove('Correy','Li',"O'Tooley")
    #print( len([s for s in candidate if s != 'Correy' and s != 'Li'  and s != "O'Tooley"]))
    total_number_khan = len([s for s in candidate if s != 'Correy' and s != 'Li'  and s != "O'Tooley"])
    total_number_correy = len([s for s in candidate if s != 'Khan' and s != 'Li'  and s != "O'Tooley"])
    total_number_li = len([s for s in candidate if s != 'Khan' and s != 'Correy'  and s != "O'Tooley"])
    total_number_otooley = len([s for s in candidate if s != 'Khan' and s != 'Correy'  and s != 'Li'])
  
    percent_khan = total_number_khan/total_votes*100
    print(percent_khan)