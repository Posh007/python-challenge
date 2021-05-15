l# Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results

# Import dependencies
import os
import csv

# Filepath to collect output data
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Define PyBank's variables
total_months = 0
total_profit_loss = 0
profit_loss_change = 0
average_profit_loss_change = []
previous_month_profit_loss = 0
current_month_profit_loss = 0

# Open and read csv file, use DictReader to allow for columns to be referenced by name instead of index numbers
with open(budget_data_csv_path) as budget:
    reader - csv.DictReader(budget_data)

    for row in csvreader:
         
        #Convert string values to integers, iterate through rows and calculate totals
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row["Profit/Loss"])

        #Calculate profit_loss_changes
        profit_loss_change = int(row["Profit/Loss"]) - previuos_profit_loss
        previous_profit_loss = int(row[Profit/Loss])
        month_of_change = month_of_change + row["Date"]

        #Calculate the average of changes in "Profit/Losses"
        profit_loss_change_list = profit_loss_change_list + [profit_loss_change]
        average_profit_loss_change = sum(profit_loss_change_list)/len(profit_loss_change_list)
                                
        #Calulate the greatest increase
        if(profit_loss_change > greatest_increase [1]):
            greatest_increase [0[ = str(row[0])
            greatest_increase [1] = change_value

        #Calculate the greatest decrease
        if(profit_loss_change) < greatest_decrease [1]:
            greatest_decrease [0] = str (row[0])
            greatest_decrease[1] =  change_value

print(f" Total Months: {total_months}")
print(f" Total: {sum(pnl_statements)}")
print(f" Average Change: {sum(pnl_statements) / total_months}")
print(f" Greatest increase in profits: {greatest_increase_month} ({greatest_increase})")
print(f" Greatest decrease in profits: {greatest_increase_month} ({greatest_decrease})")
