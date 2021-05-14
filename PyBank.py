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
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

        csv_reader = csv.reader(csvfile, delimiter=",")

        # Read the header row first
        csv_header = next(csvfile)

        # print(f"Header: {csv_header}")
        # This prints -->> Header: Date, Profit/Losses
                                
        # Read through each row of data after the header
        for row in csv_reader:

