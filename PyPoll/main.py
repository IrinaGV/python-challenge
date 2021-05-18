import os
import csv
import collections


file=os.path.join('Resources','election_data.csv')
total=0
total_votes=0
count = collections.Counter()
candidate = []
voter_ID = []
data = []


with open(file,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    
    
    for row in csvreader:
        total_votes +=1
        candidate.append(row[2])
        voter_ID.append(row[0])
    
    new_candidate = list(dict.fromkeys(candidate))
        
    
    
    total_number_khan = len([s for s in candidate if s != 'Correy' and s != 'Li'  and s != "O'Tooley"])
    total_number_correy = len([s for s in candidate if s != 'Khan' and s != 'Li'  and s != "O'Tooley"])
    total_number_li = len([s for s in candidate if s != 'Khan' and s != 'Correy'  and s != "O'Tooley"])
    total_number_otooley = len([s for s in candidate if s != 'Khan' and s != 'Correy'  and s != 'Li'])
  
    percent_khan = total_number_khan/total_votes*100
    percent_li = total_number_li/total_votes*100
    percent_correy = total_number_correy/total_votes*100
    percent_otooley = total_number_otooley/total_votes*100
    
    new_list = [percent_khan,percent_correy,percent_li,percent_otooley]
    data.append([new_candidate,new_list])
    
    
    winner = new_candidate[new_list.index(max(new_list))]
    
    
    print('Election Results')
    print('-------------------------')
    print('Total Votes: ' + str(total_votes))
    print('-------------------------')
    print('Khan: ' + '{:,.3f}%'.format(percent_khan) +"  "+'({})'.format(total_number_khan))
    print('Correy: ' + '{:,.3f}%'.format(percent_correy) +"  "+'({})'.format(total_number_correy))
    print('Li: ' + '{:,.3f}%'.format(percent_li) +"  "+'({})'.format(total_number_li))
    print("O'Tooley " +'{:,.3f}%'.format(percent_otooley) +"  "+'({})'.format(total_number_otooley))
    print('-------------------------')  
    print("Winner: " + winner)  
    print('-------------------------') 
    
    output_file = os.path.join("analysis","analysis.txt")
    with open(output_file, "w") as text_file:
    
      text_file.write('Election Results' + "\n")
      text_file.write('-------------------------' + "\n") 
      text_file.write('Total Votes: ' + str(total_votes) + "\n" )
      text_file.write('-------------------------' +"\n"  )
      text_file.write('Khan: ' + '{:,.3f}%'.format(percent_khan) +"  "+'({})'.format(total_number_khan)+"\n")
      text_file.write('Correy: ' + '{:,.3f}%'.format(percent_correy) +"  "+'({})'.format(total_number_correy)+"\n")
      text_file.write('Li: ' + '{:,.3f}%'.format(percent_li) +"  "+'({})'.format(total_number_li)+ "\n")  
      text_file.write("O'Tooley " +'{:,.3f}%'.format(percent_otooley) +"  "+'({})'.format(total_number_otooley) + "\n")
      text_file.write('-------------------------' + "\n")
      text_file.write("Winner: " + winner + "\n")  
      text_file.write('-------------------------' + "\n")
    