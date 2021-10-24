import os
import csv

# Set File path
file_path = os.path.join("..", "Resources", "budget_data.csv")
# print(file_path)

# set path for  reader 
with open(file_path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader)
    print(reader)
    print(csv_header)


    # List of all the Profits/Losses
    ProfitsnLosses = []
    total = 0
    months = 0
    avgChange = 0

    for row in reader:
        months += 1
        if months !=1:
            change = int(row[1]) - ProfitsnLosses
            avgChange += change
            if months == 2:
                highest = change
                highestMonth = row[0]
                lowest = change
                lowestMonth = row[0]
            elif change > highest:
                 highest = ProfitsnLosses
                 highestMonth = row[0]
            elif change < lowest:
                lowest = ProfitsnLosses
                lowestMonth = row[0]
        ProfitsnLosses = int(row[1])

        total += ProfitsnLosses
        

    avgChange = round(avgChange / (months - 1), 2)
    print("Financial Analysis")
    print("----------------")
    print("Total Months:", months)
    print("Total: $", total, sep='')
    print('Average Change: $', avgChange, sep='')
    print('Greatest Increase in Profits:', highestMonth,' ($', highest, ') ',
    sep = '')
    print('Greatest Decrease in Profits:', lowestMonth,'  ($', lowest, ') ',
    sep = '')
    
    # set path for Output to text 

    print("Financial Analysis", file=open("outputpybank1.txt", "a"))   
    print("----------------" ,file=open("outputpybank1.txt", "a"))
    print("Total Months:", months, file=open("outputpybank1.txt", "a"))
    print("Total: $", total, sep='', file=open("outputpybank1.txt", "a"))
    print('Average Change: $', avgChange, sep='', file=open("outputpybank1.txt", "a"))
    print('Greatest Increase in Profits:', highestMonth,' ($', highest, ') ',
    sep = '', file=open("outputpybank1.txt", "a"))
    print('Greatest Decrease in Profits:', lowestMonth,'  ($', lowest, ') ',
    sep = '', file=open("outputpybank1.txt", "a"))




    
        

   

    
    
    
    
    
