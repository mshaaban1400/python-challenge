# import the modules needed to work across systems and to work with csv files
import os
import csv

# create path to pypoll.csv
csvfile = '/Users/mshaaban/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv'

# create lists for columns
ballot_id = []
county = []
candidate = []

# set counters
candidate_1_votes = 0
candidate_2_votes = 0
candidate_3_votes = 0

# open file and create variables
with open(csvfile, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter= ',')
    header = next(csvreader)

    for row in csvreader: 
        ballot_id.append(int(row[0]))
        county.append(str(row[1]))
        candidate.append(str(row[2]))
    
    candidate_no_duplicates = tuple(set(candidate))

# find total number of votes
total_votes = len(ballot_id)

# create function to calculate number of votes per candidate
def votes(parameter1, parameter2):
    sum = 0
    for row in parameter1:
        if row == parameter2:
            sum +=1
    return sum

candidate_1_votes = votes(candidate, candidate_no_duplicates[0])
candidate_2_votes = votes(candidate, candidate_no_duplicates[1])
candidate_3_votes = votes(candidate, candidate_no_duplicates[2])

# create dictionary with stats
election_results = dict()
election_results = {str(candidate_no_duplicates[0]): int(candidate_1_votes),
            str(candidate_no_duplicates[1]): int(candidate_2_votes),
            str(candidate_no_duplicates[2]): int(candidate_3_votes),}

# create function to determine percentage of votes per candidate
def percent_votes(holder):
    votes = (holder / total_votes) * 100
    return round(votes, 3)

percent_votes_1 = percent_votes(candidate_1_votes)
percent_votes_2 = percent_votes(candidate_2_votes)
percent_votes_3 = percent_votes(candidate_3_votes)

# find the winner
highest_votes = max(election_results.values())
winner = max(election_results, key=election_results.get)
print(f'{winner}: {highest_votes}')

#  print results
print('Election Results')
print('_________________________________________')
print('Total Votes: ' + str(total_votes))
print('_________________________________________')
print(f'{candidate_no_duplicates[0]} {percent_votes_1}% ({candidate_1_votes})')
print(f'{candidate_no_duplicates[1]} {percent_votes_2}% ({candidate_2_votes})')
print(f'{candidate_no_duplicates[2]} {percent_votes_3}% ({candidate_3_votes})')
print('_________________________________________')
print(f'Winner: {winner}')

# specify file to write to
output_path = '/Users/mshaaban/Desktop/Bootcamp/python-challenge/PyPoll/Analysis/PyPoll_Analysis.txt'

# create output file
with open(output_path, 'w') as PyPoll_Analysis:

    # Write the rest of the rows
    PyPoll_Analysis.write('Election Results\n')
    PyPoll_Analysis.write('---------------------------------------\n')
    PyPoll_Analysis.write(f'Total Votes: {total_votes} \n')
    PyPoll_Analysis.write('---------------------------------------\n')
    PyPoll_Analysis.write(f'{candidate_no_duplicates[0]}: {percent_votes_1}% ({candidate_1_votes})\n')
    PyPoll_Analysis.write(f'{candidate_no_duplicates[1]}: {percent_votes_2}% ({candidate_2_votes})\n')
    PyPoll_Analysis.write(f'{candidate_no_duplicates[2]}: {percent_votes_3}% ({candidate_3_votes})\n')
    PyPoll_Analysis.write('---------------------------------------\n')
    PyPoll_Analysis.write(f'Winner: {winner}\n')
    PyPoll_Analysis.write('---------------------------------------\n')
