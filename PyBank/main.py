import os
import csv

csv_path = os.path.join("budget_data")
output_path = os.path.join("output.txt")

#Declare Variables and Lists for Data

Total_number_of_Months = 0
total_revenue = 0
change = 0






#Open CSV

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)


#Financial Analysis and Calculating Questions







#Print Results


print("Financial Analysis")
print("----------------------------")
print("Total Months: ", num_months)
print("Average  Change: $", avg_change)
print("Greatest Increase in Profits: %s (%s)" % (max_inc_month, max_inc))
print("Greatest Decrease in Profits:%s ($%s)" % (max_dec_month, max_dec))