import os
import csv


# Declare Path

csvpath = os.path.join("PyBank", "budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and See Rows

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

# Create Variables

total = 0 # allows future functions to assign a value, for instance(+ 1) - acts as a starting point
count = 0 # allows future functions to assign a value, for instance(+ 1) - acts as a starting point
max_profit = 0
max_loss = 0

# Create Calculations 

# Total Number of Months in the dataset








