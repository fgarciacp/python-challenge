import csv
import os

# read CSV file
with open("Resources/budget_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader)
    
    total_mounth = 0
    total_prof_loss = 0
    change = []
    previous_profit_loss = None
    greatest_increase = 0
    greatest_decrease = 0
    # Increment number of months to gives total whit loop
    for row in csvreader:
        
        total_mounth += 1
        
        try:
            # change profit/loss value
            prof_loss = float(row[1])
            total_prof_loss += prof_loss
            
            if previous_profit_loss is not None:
                current_change = prof_loss - previous_profit_loss
                change.append(current_change)
                
                if current_change > greatest_increase:
                    greatest_increase = current_change
                    Age= row[0]
                if current_change < greatest_decrease:
                    greatest_decrease = current_change
                    Age2=row[0]
                
            previous_profit_loss = prof_loss
            
        except ValueError:
            print(f'Invalid value in row: {row}')
    
    # Calcule avarege to changes 
    average_change = sum(change) / len(change)
    
    # print to  results
    print(f'Total Months: {total_mounth}')
    print(f'Total Profit/Loss: ${total_prof_loss}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits:{Age}- ${greatest_increase}')
    print(f'Greatest Decrease in Profits:{Age2}- ${greatest_decrease}')