import os
import csv
file_path = os.path.join("data", "budget_data.csv")
# print(file_path)
total_months= 0
with open(file_path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader)
    print(csv_header)
    print("Hello")
    # # List of all profits/Losses
    # # with open (FileName) as csvfile:
    # ProfitsnLosses = []
    # total = 0
    # months = 0
    # avgChange = 0

    
    # # for row in reader:
    # #     total_months +=1
    # #     # print(row[0])
        
print(reader)