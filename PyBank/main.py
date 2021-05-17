import os
import csv
import collections
#import subprocess

file=os.path.join("Resources","budget_data.csv")
#"C:\\","users","igasnikova","Desktop","python-challenge",
#"PyBank","Resources","budget_data.csv")
profit_losses =[]
date=[]
total=0
totalrows=0
data = []
count = collections.Counter()
#change = []
with open(file,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
     
    
    for row in csvreader:
      
     totalrows += 1
     total += int(row[1])
          
     profit_losses.append(row[1])
     profit_losses = list(map(int, profit_losses))
     date.append(row[0])
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ', totalrows)
    print('Total: ', total) 
    
    for x,y in zip(profit_losses[0::], profit_losses[1::]):
               
     count[y-x] +=1
         
              
    change=[(y-x) for x,y in zip(profit_losses[0::], profit_losses[1::]) ]
    
    change.append
    average = round((sum(change)/85),2)
    print('Average  Change: ','${:,.2f}'.format(average))
    data.append([date, change])  
    change_max = max(change)
    change_min = min(change)
    print('Greatest Increase in Profits: ',date[(change.index(max(change)))+1],'$({})'.format(change_max))    
    print('Greatest Decrease in Profits: ',date[(change.index(min(change)))+1],'$({})'.format(change_min))
    
    output_file = os.path.join("/../analysis","analysis.txt")
    with open("analysis.txt", "w") as output_file:
      #subprocess.check_call(["python", "main.py"], stdout=f)
      output_file.write("Financial Analysis" + "\n")
      output_file.write("----------------------------" + "\n") 
      output_file.write("Total Months: " +str(totalrows) + "\n" )
      output_file.write("Total: " + str(total) +"\n"  )
      output_file.write("Greatest Increase in Profits: " +str(date[(change.index(max(change)))+1]) +" "+str('$({})'.format(change_max))+"\n")
      output_file.write("Greatest Decrease in Profits: " +str(date[(change.index(min(change)))+1]) +" "+str('$({})'.format(change_min))+"\n")