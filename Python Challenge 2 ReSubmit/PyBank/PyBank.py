import os
import csv

# Create path for csv files
datapath = os.path.join("Resources","budget_data.csv")

# Declare Variables 
total_number_months = []
profit_loss_changes =[]
total_profit_loss = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
title = "Financial Analysis"

# Open csv files
with open(datapath) as BudgetData:
    reader = csv.reader(BudgetData)

    # Skips header as data to be included
    header = next(reader)
#print title
    for row in reader:
# The total number of months included in the dataset        
        total_number_months.append(row[0])
        total_profit_loss.append(row[1])
    
    print(title)
    print("----------------------------")
    print(f"Total Months: {len(total_number_months)}")
   

# The net total amount of "Profit/Losses" over the entire period
    total_profit_loss = [int(x)for x in total_profit_loss]
    total_profit_amount = (sum(total_profit_loss))
    print(f"Total: ${total_profit_amount}")
 

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(len(total_profit_loss)-1):
        #profit_loss_changes.append
        profit_loss_changes.append(total_profit_loss[i+1]-total_profit_loss[i])
    print(f"Average Change: {sum(profit_loss_changes) / len(profit_loss_changes)}")
  
#The greatest increase in profits (date and amount) over the entire period
    for month, change in zip(total_number_months[1:], profit_loss_changes):
        if change > greatest_increase[1]:
            greatest_increase[1] = change
            greatest_increase[0] = month
        if change < greatest_decrease[1]:
            greatest_decrease[1] = change
            greatest_decrease[0] = month
   
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
     

#The greatest decrease in profits (date and amount) over the entire period   
       
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")   
