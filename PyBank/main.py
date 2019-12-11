# Importing the required Modules
import os
import csv
import sys

# Assuming CSV file and main.py files will be stored in the same directory
# Defining the file object
# os.path.join(sys.path[0] pointing to the same path as the main.py exists in
budget_data_csv = os.path.join(sys.path[0], 'budget_data.csv')

# Declaring the Vaiables and assiging initial values
total_months = 0
total_amount = 0
row_count = 0
profit_losses_value = 0
profit_losses_change = 0

time_period = []
profit_losses = []


# Opening the file for windows
with open(budget_data_csv, newline="", encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    
     #Reading the header row to skip 
    csv_header = next(csvreader)

    # Reading from second row to last row to get the expected output
    for row in csvreader:
        #Increasing the number months by 1 for each record in the file
        total_months += 1

        # Adding each row's amount
        total_amount += int(row[1])

        if row_count == 0:
            profit_losses_value = int(row[1])
        elif row_count != 0:
            profit_losses_change =int(row[1]) - profit_losses_value
            
            profit_losses.append(profit_losses_change)

            time_period.append(row[0])

            
        row_count += 1
        profit_losses_value = int(row[1])     


greatest_increase = max(profit_losses)
greatest_descrease = min(profit_losses)

greatest_increase_index = profit_losses.index(greatest_increase)
greatest_descrease_index = profit_losses.index(greatest_descrease)

greatest_increase_date = time_period[greatest_increase_index]
greatest_decrease_date = time_period[greatest_descrease_index]

avaerage_change = sum(profit_losses) / len(profit_losses)

#Printing Output to the terminal
print('Financial Analysis')
print('------------------------------------')
print(f"Total Months: {str(total_months)}")
print(f"Total Amount: {str(total_amount)}")
print(f"Avarage Change: {str(round(avaerage_change,2))}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_descrease)})")

# Exporting the data into a text file

# Defining the file name and path
output_file = os.path.join(sys.path[0], 'Financial_Analysis_Summary.txt')

# Opening the file and writing into the file
with open(output_file,"w") as output_file:
    output_file.write('Financial Analysis\n')
    output_file.write('------------------------------------\n')
    output_file.write(f"Total Months: {str(total_months)}\n")
    output_file.write(f"Total Amount: {str(total_amount)}\n")
    output_file.write(f"Avarage Change: {str(round(avaerage_change,2))}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase)})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_descrease)})\n")

# End of the program