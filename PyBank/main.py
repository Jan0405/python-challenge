import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

budget_data = []

with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        budget_data.append({"Month": row["Date"], "Amount": int(row["Profit/Losses"]), "Change": 0})
        #print(row)

    # Total Months
    total_months = len(budget_data)
    # print(total_months)

    # Total Amount
    total_amount = sum(row["Amount"] for row in budget_data)
    # print(total_amount)

    # Calculate Change
    prev_amount = budget_data[0]["Amount"]
    # print(prev_amount)
    for i in range(len(budget_data)):
        budget_data[i]["Change"] = budget_data[i]["Amount"] - prev_amount
        prev_amount = budget_data[i]["Amount"]
        # print(budget_data[i]["Change"])


    # Calculate Average Change
    total_change = sum(row["Change"] for row in budget_data)
    ave_change = round(total_change/(total_months-1),2)
    # print(ave_change)

    # Calculate Greatest Increase
    great_incr = max(budget_data, key = lambda x:x["Change"])
    print(great_incr)

    # Calculate Greatest Decrease
    great_decr = min(budget_data, key = lambda x:x["Change"])
    print(great_decr)


    # Printing Analysis to Terminal
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_amount}')
    print(f'Average Change: ${ave_change}')
    print(f'Greatest Increase in Profits: {great_incr["Month"]} (${great_incr["Change"]})')
    print(f'Greatest Decrease in Profits: {great_decr["Month"]} (${great_decr["Change"]})')


# Printing to analysis.txt

textfile_out = os.path.join("Analysis", "analysis.txt")

with open(textfile_out, "w") as text_file:
    print('Financial Analysis', file = text_file)
    print('----------------------------', file = text_file)
    print(f'Total Months: {total_months}', file = text_file)
    print(f'Total: ${total_amount}', file = text_file)
    print(f'Average Change: ${ave_change}', file = text_file)
    print(f'Greatest Increase in Profits: {great_incr["Month"]} (${great_incr["Change"]})', file = text_file)
    print(f'Greatest Decrease in Profits: {great_decr["Month"]} (${great_decr["Change"]})', file = text_file)