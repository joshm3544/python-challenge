import os

import csv

poll_csv = os.path.join('..','Resources','election_data.csv')

with open(poll_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header= next(csvreader)
    
    total_votes = 0
    
    Khan = 0
    
    Correy = 0
    
    Li = 0
    
    OTooley = 0
    
    for row in csvreader:
        
        #print(str(row))
        
        total_votes= total_votes + 1
        
        if row[2] == "Khan":
            Khan = Khan + 1
            
        if row[2] == "Correy":
            Correy = Correy + 1
            
        if row[2] == "Li":
            Li = Li + 1
            
        if row[2] == "O'Tooley":
            OTooley = OTooley + 1
       
print(f"Total Votes: {str(total_votes)}")
        
print(f"Khan: {str((Khan / total_votes) * 100)}% ({str(Khan)})")

print(f"Correy: {str((Correy / total_votes) * 100)}% ({str(Correy)})")

print(f"Li: {str((Li / total_votes) * 100)}% ({str(Li)})")

print(f"O'Tooley: {str((OTooley / total_votes) * 100)}% ({str(OTooley)})")

if Khan > Correy:
    print("Winner: Khan")
else:
    print("Winner: Correy")
