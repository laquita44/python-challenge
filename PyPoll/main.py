import os
import csv
import collections
from collections import Counter

# variables in list
candidate_votes = []
candidate_selection = []


# set File path
file_path = os.path.join("..", "Resources", "election_data.csv")

# set path for reader
with open(file_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
   # read the header row first
    csv_header = next(csv_reader)
   
    # loop through each row 
    for row in csv_reader:
        candidate_votes.append(row[2])


    # change list to ascending order
    list = sorted(candidate_votes)
        
    # arrange the sorted list
    arrange_list = list


    # count votes per candidate in ascending order to append to list
    candidate_count = Counter (arrange_list) 
    candidate_selection.append(candidate_count.most_common())


    # calculate the percentage of votes per candidate
    for choice in candidate_selection:
       
        holder_one = format((choice[0][1])*100/(sum(candidate_count.values())),'.3f')
        holder_two = format((choice[1][1])*100/(sum(candidate_count.values())),'.3f')
        holder_three = format((choice[2][1])*100/(sum(candidate_count.values())),'.3f')
        holder_four = format((choice[3][1])*100/(sum(candidate_count.values())),'.3f')


      
#   Print values, sum, and percentages position
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(candidate_count.values())}")
print("-------------------------")
print(f"{candidate_selection[0][0][0]}: {holder_one}% ({candidate_selection[0][0][1]})")
print(f"{candidate_selection[0][1][0]}: {holder_two}% ({candidate_selection[0][1][1]})")
print(f"{candidate_selection[0][2][0]}: {holder_three}% ({candidate_selection[0][2][1]})")
print(f"{candidate_selection[0][3][0]}: {holder_four}% ({candidate_selection[0][3][1]})")
print("-------------------------")
print(f"Winner:  {candidate_selection[0][0][0]}")
print("-------------------------")

# -->>  Export results to text file 
election_file = os.path.join("Output", "out_pypoll.txt")
with open(election_file, "w") as txt_file:

    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes:  {sum(candidate_count.values())}\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"{candidate_selection[0][0][0]}: {holder_one}% ({candidate_selection[0][0][1]})\n")
    txt_file.write(f"{candidate_selection[0][1][0]}: {holder_two}% ({candidate_selection[0][1][1]})\n")
    txt_file.write(f"{candidate_selection[0][2][0]}: {holder_three}% ({candidate_selection[0][2][1]})\n")
    txt_file.write(f"{candidate_selection[0][3][0]}: {holder_four}% ({candidate_selection[0][3][1]})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner:  {candidate_selection[0][0][0]}\n")
    txt_file.write("-------------------------\n")   

# -->>  Export results to text file 
# election_file = os.path.join("Output", "outputpypoll.txt")
# with open(outputpypoll.txt, "w") as txt_file:

# -->>  Export a text file with the results
# election_file = os.path.join("outputpypoll.txt")
# with open(election_file, "w") as outfile:


#     outfile.write("Election Results\n")
#     outfile.write("-------------------------\n")
#     outfile.write(f"Total Votes:  {sum(candidate_count.values())}\n")
#     outfile.write("-------------------------\n")
#     outfile.write(f"{candidate_selection[0][0][0]}: {holder_one}% ({candidate_selection[0][0][1]})\n")
#     outfile.write(f"{candidate_selection[0][1][0]}: {holder_two}% ({candidate_selection[0][1][1]})\n")
#     outfile.write(f"{candidate_selection[0][2][0]}: {holder_three}% ({candidate_selection[0][2][1]})\n")
#     outfile.write(f"{candidate_selection[0][3][0]}: {holder_four}% ({candidate_selection[0][3][1]})\n")
#     outfile.write("-------------------------\n")
#     outfile.write(f"Winner:  {candidate_selection[0][0][0]}\n")
#     outfile.write("-------------------------\n")    
