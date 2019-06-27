import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

total_months = []
net_profit_loss = []
difference = []
greatest_inc_date = ""
greatest_dec_date = ""
    
for row in csvreader:
    total_months.append(int(row[0]))   
    net_profit_loss.append(int(row[1]))

    print("Financial Analysis")
    print("---------------------------------------------------")
    print("Total Months: " + len(total_months))
    print("Net Total: $" + sum(net_profit_loss))
    
for x in range(1, len(net_profit_loss)):
        
    difference.append(net_profit_loss[x] - net_profit_loss[x-1])
        
    average_change = sum(difference) / len(difference)
        
    greatest_inc = max(difference)
    greatest_inc_date = str(total_months[differences.index(max(differences))])
        
    greatest_dec = min(difference)
    greatest_dec_date = str(total_months[differences.index(min(differences))])
        
    
    print("Average Change: $", round(average_change))  
    print("Greatest Increase: ", greatest_inc_date, "($", greatest_inc,")")
    print("Greatest Decrease: ", greatest_dec_date, "($", greatest_dec,")")

with open("budget_analysis.txt", "w") as text_file:
    print("Financial Analysis"\n
          "---------------------------------------------------"\n
          "Total Months: " + len(total_months)\n
          "Net Total: $" + sum(net_profit_loss)\n
          "Average Change: $", round(average_change)\n  
          "Greatest Increase: ", greatest_inc_date, "($", greatest_inc,")"\n
          "Greatest Decrease: ", greatest_dec_date, "($", greatest_dec,")", file = text_file)
