import os

# import module for reading csv files
import csv

# Total net profit/loss  over the entire period
Sum_profit = 0
Sum_Loss = 0
TotalPL = 0
profit = 0
row_count = 0
Average_change = 0
first_record = 0
previous_month = 0
change_in_profit = 0
total_change_in_profit = 0
Greatest_increase_in_profit = 0
Greatest_decrease_in_profit = 0
increase_date = ''
decrease_date = ''
data_list = []
# path to collect data from tne csv file
#csvpath = os.path.join("Instructions\Resources", "budget_data.csv")
# csvpath = os.path.join(r"C:\Users\Okyere\RUT-SOM-VIRT-DATA-PT-03-2021-U-C\02-Homework\03-Python\Instructions\PyBank\budget_data.csv")
# os.chdir("Resources")

with open('budget_data.csv',encoding="ISO 8859-1") as csvfile:

# read in the csv file
#with open(csvpath, "r") as csvfile:

# Split the data on commas
    csvreader = csv.reader(csvfile,delimiter=",")

#Read the header on row first 
    csv_header = next(csvreader)
    for row in csvreader :
        data_list.append(row)

    #print(f"Header: {csv_header}")

#Total number of months in the dataset
#row_count =  sum(1 for row in csvreader)


    for row in data_list: 
    
        if first_record  == 0 :
            previous_month =int(row[1])
            row_count = row_count +1
            first_record = 1
            profit = profit + int(row[1])
        else :
            profit = profit + int(row[1])
            row_count = row_count +1
            change_in_profit = int(row[1]) - previous_month
            total_change_in_profit = total_change_in_profit + change_in_profit
            previous_month = int(row[1])
            
    for row in data_list:   
        if  int(row[1]) > Greatest_increase_in_profit :
            Greatest_increase_in_profit = int(row[1])
            increase_date = row[0],[0] 
        elif int(row[1]) < Greatest_decrease_in_profit  :
            Greatest_decrease_in_profit = int(row[1])
            decrease_date = row[0],[0]


Average_change = total_change_in_profit/(row_count-1)

#print(f"Total:{TotalPL}")

print("Financial Analysis")
print("......................................")
print(f"Total Months : {row_count}")
print(f"Average_change:{Average_change}")
print (f"Total :{profit}")
print(f"Greatest_increase_in_profit : {Greatest_increase_in_profit}")
print(f"Greatest_decrease_in_profit : {Greatest_decrease_in_profit}")



    










