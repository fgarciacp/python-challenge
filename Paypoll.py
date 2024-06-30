import csv
import os

# read  CSV file
with open("Resources/election_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    total_V = 0
    candidates_Dict = {}
    winner =""
    win_vot = 0
    #    
    for row in csvreader:
        # conditional 
        if csvreader.line_num>1:
            total_V+=1
            if (candidates_Dict) == 0:
                candidates_Dict[row[2]] = 1 
            else:
                if row[2] in candidates_Dict:
                    candidates_Dict[row[2]] = candidates_Dict[row[2]] +1 
                else:
                    #Add  vote count in candidate
                    candidates_Dict[row[2]] = 1  
    print(f'total votes:{total_V}')
#Iteration to candidates for porcent to each one                     
for candidateKey in candidates_Dict.keys():    
    votes = candidates_Dict[candidateKey]
    AVG = format(votes/total_V,'.3%')     
    #Determining to winner
    if winner == "":
        winner = candidateKey
        winner_votes = votes
    else:
        if votes > winner_votes:
            #Validating candidate votes
            winner = candidateKey
            win_vot = votes

    print(f'{candidateKey}: {AVG} ({votes})') 
print(f'winner:{winner}')