import os

import csv

budget_csv = os.path.join('..','Resources','budget_date.csv')
    
with open(budget_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header= next(csvreader)
    
    total_months = 0
    
    total_money = 0
    
    total_change = 0
    
    prev = 0
    
    max_val = 0
    
    min_val = 0
    
    
    for row in csvreader:
        
        #print(str(row))
        
        total_months = (total_months + 1)
        
        total_money = total_money + int(row[1])
        
        if total_months > 1:
            
            total_change = total_change + int(row[1]) - prev
            
            dif = int(row[1]) - prev
            
            if dif > max_val:
                
                max_val = dif 
                
            if dif < min_val:
                
                min_val = dif
                
        prev = int(row[1])
             
    print(f"Total Months: {str(total_months)}")
    
    print(f"Total: {str(total_money)}")

    print(f"Average Change: {str(total_change/(total_months - 1))}")
    
    print(f"Greatest Increase in Profit: {str(max_val)}")
    
    print(f"Greatest Decrease in Profit: {str(min_val)}")   
    
