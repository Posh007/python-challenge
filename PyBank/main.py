# Create a Python script that analyzes the PyBank records to calculate each of the following:
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

output_file = "Analysis/budget_analysis.txt"

# Define PyBank's variables
total_months = 0 # total number of months
total_profit_loss = 0 # variable to hold the total profit or loss
greatest_decrease = ["", 0] # variable to hold greatest loss with date
greatest_increase = ["", 0] # variable to hold greatest profit with date

# Open and read csv file, use DictReader to gnore skip row and to allow for columns to be 
# referenced by name instead of index numbers

with open(budget_data_csv_path) as budget_data:
    
    csvreader = csv.DictReader(budget_data)

    for row in csvreader:
        
        #Convert string values to integers, iterate through rows and calculate totals
        total_months = total_months + 1
        current_profit_loss = int(row["Profit/Losses"])
        total_profit_loss = total_profit_loss + current_profit_loss
        
        # Calculate the greatest increase in profit/loss
        if(current_profit_loss > greatest_increase [1]):
            greatest_increase [0] = row["Date"]
            greatest_increase [1] = current_profit_loss

        #Calculate the greatest decrease
        if(current_profit_loss < greatest_decrease [1]):
            greatest_decrease [0] = row["Date"]
            greatest_decrease[1] =  current_profit_loss
        
        current_profit_loss = None

#Calculate the average of changes in Profit/Losses
average_profit_loss_change = round(total_profit_loss/total_months)

# Print Analysis Summary

output = (
    f"\nFinancial Analysis\n"
    f"--------------------------\n"
    f" Total Months: {total_months}\n"
    f" Total Profit/Loss: ${total_profit_loss}\n"
    f" Average Profit/Loss Change: ${average_profit_loss_change}\n"
    f" Greatest Increase in Profit/Loss: {greatest_increase [0]} (${greatest_increase[1]})\n"
    f" Greatest Decrease in Profit/Loss: {greatest_decrease [0]} (${greatest_decrease[1]})\n"
)

# Print Output
print("RESULT \n", output)

#Transfer analysis results to text file
with open(output_file, "w") as text_file:
    text_file.write(output)
