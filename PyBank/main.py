import csv

 # create variables

total = 0 # allows future functions to assign a value; for instance count + 1 = needs something to go by
max_profit = None # omparing None to anything will always return False except None itself
max_loss = None # omparing None to anything will always return False except None itself
count = 0 # allows future functions to assign a value; for instance count + 1 = needs something to go by

# calculations

heading = None # deletes headers from data set
with open("Resources/budget_data.csv")as file:
    budget = csv.reader(file)

    for record in budget: # creating loop
        if heading is None:
            heading = record
        else:
            amount = int(record[1]) # setting value for amount
            count = count + 1
            total = total + amount
            if max_profit is None or amount > max_profit[1]: # using short circuited evaulation to evaulating the left hand side of it
                max-profit = (record[0], amount) # max_profit holds both date and amount, max profit so far
            if max_loss is None or amount < max_loss[1]:
                max_loss = (record[0], amount)

# print results and using empty strings

print("Financial Analysis")
print("----------------------------")
print("Total Months: ", count)
print("Average  Change: $", total, sep="")
print("Greatest Increase in Profits: ", max_profit[0], " ($" , max_profit[1], ")",sep="") 
print("Greatest Decrease in Profits: ", max_loss[0], " ($", max_loss[1], ")",sep="")






