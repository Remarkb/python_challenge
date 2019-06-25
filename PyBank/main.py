import os
import csv

# create file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# empty variables for months and prof_loss, empty list for delta
months = 0
prof_loss = 0
delta = []

# Read in CSV file using CSV module
with open(csvpath, newline = '') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # variables for increase/decrease calculation
    previous_rev = 0
    greatest_increase = 0
    greatest_decrease = 0

    for row in csvreader:
        revenue = int(row[1])
        months += 1
        prof_loss += revenue
        revDelta= int(row[1]) - previous_rev
        delta.append(revenue - previous_rev)
        previous_rev = revenue
        
        if(revDelta > greatest_increase):
            greatest_increase = revDelta
            greatestIncDate = row[0]
        if(revDelta < greatest_decrease):
            greatest_decrease = revDelta
            greatestDecDate = row[0]
    
    sum_delta = sum(delta)
    avg_delta = round(((sum_delta-867884)/(months-1)), 2)

# Create analysis output
analysis = (
f"Financial Analysis\n"
f"-----------------------------------\n"
f"Total Months: {months}\n"
f"Total Profit: ${prof_loss}\n"
f"Average Change: ${avg_delta}\n"
f"Greatest Increase in Profits: {greatestIncDate}  (${greatest_increase})\n"
f"Greatest Decrease in Profits: {greatestDecDate}  (${greatest_decrease})\n")

print(analysis)

output_analysis = os.path.join("output_analysis.txt")

#  Open the output file
with open("output_analysis.txt", "w", newline = '', encoding = 'utf-8') as txt_file:
    txt_file.write(analysis)


