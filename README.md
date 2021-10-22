# Python Homework - Py Me Up, Charlie

## Background

The task is to complete the **two** Python Challenges, PyBank(financial analysis) and PyPoll(election analysis).

*  A folder named after each challenge contains the following:

  * A file called `main.py`, which serves as the main script to run each analysis.
  * A "Resources" folder that contains the CSV files. 
  * An "analysis" folder that contains a text file that has the analysis results.

## PyBank

The challenge was to create a Python script that analyzes financial records using the given detailed financial data [budget_data.csv](PyBank/Resources/budget_data.csv) to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* Printed analysis results are as follows:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

## PyPoll

The challenge was to help a small, rural town modernize its vote counting process by creating a Python script that analyzes votes in the given set of poll data[election_data.csv](PyPoll/Resources/election_data.csv) and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* Printed analysis results are as follows:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  