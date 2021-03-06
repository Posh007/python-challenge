# Create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# Import Dependencies 
import os
import csv

# Set the path for the CSV file to upload

election_data_csv_path = os.path.join("Resources","election_data.csv")

# Text file to store the results
output_file = "Analysis/election_analysis.txt"

# Define and initialize parameters

vote_count = 0
total_votes = 0
percent_vote = []
candidate_choices = [] #list of running or available candidates 
candidate_votes = {}
#Winning candidate and winning count list
winning_candidate = "" # will hold the name of the winner 
winning_count = 0

# Open and read the CSV using using DictReader

with open(election_data_csv_path) as election_data:
    csvreader = csv.DictReader(election_data)
    
    # Iterate through each row
    for row in csvreader:
        
        # Count and add to the total vote count
        total_votes = total_votes + 1

        # Fetch candidate names from data
        candidate_name = row["Candidate"]

        # Check if candidate does not match any existing candidates
        if candidate_name not in candidate_choices:
            
            # Add candidate to the list of candidates
            candidate_choices.append(candidate_name)

            # Record vote_count 
            candidate_votes[candidate_name] = 0

        # Add to candidate's vote count 
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print results and transfer data to a text file
with open(output_file, "w") as txt_file:

    # Print the final vote count
    election_results = (
        f"\n\nElection Results\n"
        f"--------------------------\n"
        f" Total Votes: {total_votes}\n"
        f"---------------------------\n"
    )

    print(election_results) 

    # store the final vote in a text file
    txt_file.write(election_results)

    # Identify the winner by iterating through counts
    for candidate in candidate_votes:
        
        # Pull the vote count and percentage of votes
        votes = candidate_votes.get(candidate)
        percent_vote = float(votes) / float(total_votes) * 100
        
        # Identify winning vote count and cabdidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print candidates individual voter count and percentage
        voter_output = f"{candidate}: {percent_vote: .3f}% ({votes})\n"
        print(voter_output)

        # Transfer candidates' voter count and percentage to a text file
        txt_file.write(voter_output)

    # Print the winning candidate to Terminal
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------------\n"
    )         
    print(winning_candidate_summary)

    # Store the winning cabdidate's name to the text file
    txt_file.write(winning_candidate_summary)












