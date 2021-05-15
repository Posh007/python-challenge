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

# Define PyBank's variables
total_months = 0
total_profit_loss = 0
profit_loss_change = 0
average_profit_loss_change = []
previous_month_profit_loss = 0
current_month_profit_loss = 0

# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Open and read csv into dictionaries to allow for column names use instead of index numbers
with open(budget_data_csv_path) as csvfile:
    reader = csv.DictReader(csvfile)

    For row in reader: 
        #Convert string values to integers, iterate through rows and calculate totals
        total_months = total months + 1
        total_profit_loss = total profit_loss + int(row["Profit/Loss"])

        #Calculate profit_loss_changes
        profit_loss_change = int(row["Profit/Loss"]) - previuos_profit_loss
        previous_profit_loss = int(row[Profit/Loss])
        month_of_change = month_of_change + row["Date"]

        #Calulate the greatest increase
        If(revenue_change) > greatest_increase [1]:
            greatest_increase [0] = row ["Date"]
            greatest_increase [1] = profit_loss_change


