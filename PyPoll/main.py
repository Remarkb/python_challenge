import os
import csv

# create file path
csvpath = os.path.join('Resources', 'election_data.csv')

# empty variables for the vote count and candidate list
votes_cast = 0
candidates = []
candidate_vote = {}

# Read in CSV file using CSV module
with open(csvpath, newline = '') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:
        votes_cast = row[0]
        candidates = row[2]
        if candidates in candidate_vote:
            candidate_vote[row[2]].append(row[0])
        else:
            candidate_vote[row[2]] = [row[0]]
        
khan_vote = len(candidate_vote['Khan'])
correy_vote = len(candidate_vote['Correy'])
li_vote = len(candidate_vote['Li'])
otooley_vote = len(candidate_vote["O'Tooley"])


total_votes = (khan_vote+correy_vote+li_vote+otooley_vote)


khan_prct = round(((len(candidate_vote['Khan'])/total_votes)*100), 4)
correy_prct = round(((len(candidate_vote['Correy'])/total_votes)*100), 4)
li_prct = round(((len(candidate_vote['Li'])/total_votes)*100), 4)
otooley_prct = round(((len(candidate_vote["O'Tooley"])/total_votes)*100), 4)

# This is not working, may not be correctly done
greatest_count = 0

def key_for_value(candidate_vote, value):
    for key, value in candidate_vote.items():
        if (len([item for item in value if item]) > greatest_count):
                greatest_count = (len([item for item in value if item]))
                if value == greatest_count:
                   return key
  
print(greatest_count)


analysis = (
f"Election Results\n"
f"-----------------------------------\n"
f"Total Votes: {total_votes}\n"
f"-----------------------------------\n"
f"Khan: {khan_prct}% ({khan_vote})\n"
f"Correy: {correy_prct}% ({correy_vote})\n"
f"Li: {li_prct}% ({li_vote})\n"
f"O'Tooley: {otooley_prct}% ({otooley_vote})\n"
)

print(analysis)

output_analysis = os.path.join("output_analysis.txt")

#  Open the output file
with open("output_analysis.txt", "w", newline = '', encoding = 'utf-8') as txt_file:
    txt_file.write(analysis)
