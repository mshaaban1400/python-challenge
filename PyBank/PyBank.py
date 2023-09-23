# import the modules needed to work across systems and to work with csv files
import os
import csv

# create path to pybank.csv
csvfile = '/Users/mshaaban/Desktop/Bootcamp/Personal Repo/02-Homework/03-Python/Starter_Code/PyBank/Resources/budget_data.csv'

# create lists for date and profits/losses
date = []
profit_losses = []

# open file and create variables
with open(csvfile, 'r') as budget_data:
    csvreader = csv.reader(budget_data, delimiter= ',')
    header = next(csvreader)
    print(header)

    for row in csvreader: 
        date.append(str(row[0]))
        profit_losses.append(int(row[1]))

# create sum function
def sum(budget_data):
    sum = 0
    for number in budget_data:
        sum += number
    return sum

# use sum function to calculate total number of months
total_months = len(date)

# use sum function to calculate net total profits/losses over the entire period
net_profit = sum(profit_losses)

# create a function to find the max and min values in the profit/losses to calculate the total change,
# then take the average of the total change
def avgchange(budget_data):
    # make a loop through the profits/losses column to calculate the change in profits/losses from month to month
    difference = []
    for i in range(1, len(budget_data)):
        difference.append(budget_data[i] - budget_data[i-1])
#    first_value = budget_data[0]
#    last_value = budget_data[-1]
#    difference = max_value - min_value
    average = sum(difference) / len(difference)
    return average
    
# use the total_change function to find the average change in the profits/losses column
average_change = avgchange(profit_losses)

# create function to find the greatest increase in the profits/losses column
def greatest_increase(budget_data, budget_date):
    difference = []
    for i in range(1, len(budget_data)):
        difference.append(budget_data[i] - budget_data[i-1])
    greatest_increase_value = max(difference)
    greatestp_index = difference.index(greatest_increase_value)+1
    greatest_increase_month = budget_date[greatestp_index]
    return greatest_increase_month, greatest_increase_value

greatestp_month, greatest_profit = greatest_increase(profit_losses, date)


# create function to find the greatest decrease in the profits/losses column
def greatest_decrease(budget_data, budget_date):
    difference = []
    for i in range(1, len(budget_data)):
        difference.append(budget_data[i] - budget_data[i-1])
    greatest_decrease_value = min(difference)
    greatestd_index = difference.index(greatest_decrease_value)+1
    greatest_decrease_month = budget_date[greatestd_index]
    return greatest_decrease_month, greatest_decrease_value

greatestd_month, greatest_loss = greatest_decrease(profit_losses, date)

# print results:
print('Financial Analysis')
print('_________________________________________')
print('Total Months: ' + str(total_months))
print('Total: $' + str(net_profit))
print('Average Change: $' + str(round(average_change, 2)))
print('Greatest Increase in Profits: ' + str(greatestp_month) + '($' + str(greatest_profit) + ')')
print('Greatest Decrease in Profits: ' + str(greatestd_month) + '($' + str(greatest_loss) + ')')
      