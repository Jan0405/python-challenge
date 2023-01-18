import os 
import csv

elction_file = os.path.join("Resources","election_data.csv")

with open(elction_file) as csvfile:
     reader = csv.reader(csvfile, delimiter = ',')
     header = next(csvfile)

    # List comprihension to get candidates 
     candidate_list= [candidate[2] for candidate in reader]
    # Calculating Total Votes
     total_votes = len(candidate_list)
   
    # List comprihension to count votes for each candidate from set and then 
    # Used sorted() to get the sorted data
     each_candidate_votes = sorted([[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)])
     
    # Used max() with lambda function to run on index[1] of each_candidate_votes list to get max votes
     winner = max(each_candidate_votes, key = lambda x:x[1])
     
     
# Printing Results to Terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in each_candidate_votes:
        percent_votes = round((candidate[1]/total_votes)*100,3)
        print(f'{candidate[0]}: {percent_votes}% ({candidate[1]})')
print("-------------------------")
print(f'Winner: {winner[0]}')
print("-------------------------")

# Printing to results.txt

textfile_out = os.path.join( "Analysis","results.txt")
with open(textfile_out, "w") as text_file:
   
    print("Election Results", file = text_file)
    print("-------------------------", file = text_file)
    print(f"Total Votes: {total_votes}", file = text_file)
    print("-------------------------", file = text_file)
    for candidate in each_candidate_votes:
            percent_votes = round((candidate[1]/total_votes)*100,3)
            print(f'{candidate[0]}: {percent_votes}% ({candidate[1]})',file = text_file)

    print("-------------------------", file = text_file)
    print(f'Winner: {winner[0]}', file = text_file)
    print("-------------------------", file = text_file)