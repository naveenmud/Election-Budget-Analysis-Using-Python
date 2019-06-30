import os
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    total_months = []
    net_profit_loss = []
    difference = []
    greatest_inc_date = ""
    greatest_dec_date = ""
    
    for row in csvreader:
        total_months.append(row[0])
        net_profit_loss.append(int(row[1]))

    print("Financial Analysis")
    print("---------------------------------------------------")
    print("Total Months: ", len(total_months))
    print("Net Total: $", sum(net_profit_loss))
    
    for x in range(1, len(net_profit_loss)):
        difference.append(net_profit_loss[x] - net_profit_loss[x-1])
        average_change = sum(difference) / len(difference)
        greatest_inc = max(difference)
        greatest_inc_date = str(total_months[difference.index(max(difference))])
        greatest_dec = min(difference)
        greatest_dec_date = str(total_months[difference.index(min(difference))])
        
    
    print("Average Change: $", round(average_change))  
    print("Greatest Increase: ", greatest_inc_date, "($", greatest_inc,")")
    print("Greatest Decrease: ", greatest_dec_date, "($", greatest_dec,")")

with open("budget_analysis.txt", "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("---------------------------------------------------", file = text_file)
    print("Total Months: ", len(total_months), file = text_file)
    print("Net Total: $", sum(net_profit_loss), file = text_file)
    print("Average Change: $", round(average_change), file = text_file)  
    print("Greatest Increase: ", greatest_inc_date, "($", greatest_inc,")", file = text_file)
    print("Greatest Decrease: ", greatest_dec_date, "($", greatest_dec,")", file = text_file)

