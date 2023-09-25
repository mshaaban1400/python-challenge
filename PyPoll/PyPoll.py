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
    print(header)

    for row in csvreader: 
        ballot_id.append(int(row[0]))
        county.append(str(row[1]))
        candidate.append(str(row[2]))
    
    candidate_no_duplicates = list(set(candidate))
    print(candidate_no_duplicates)
    for word in candidate_no_duplicates:
        print(word)

    # create loop and conditional to determine number of votes per candidate
    for row in election_data:
        if candidate == candidate_no_duplicates:
            candidate_1_votes += 1
        elif candidate == candidate_no_duplicates[1]:
            candidate_2_votes += 1
        elif candidate == candidate_no_duplicates[2]:
            candidate_3_votes += 1

    print(f'{candidate_no_duplicates[0]}: {candidate_1_votes}')
    print(f'{candidate_no_duplicates[1]}: {candidate_2_votes}')
    print(f'{candidate_no_duplicates[2]}: {candidate_3_votes}')

# create sum function
def sum(election_data):
    sum = 0
    for number in election_data:
        sum += number
    return sum

# use sum function to calculate total number of votes
total_votes = len(ballot_id)
print(total_votes)

# create function to determine percentage of votes
def percent_votes(holder):
    votes = holder / len(ballot_id)
    return votes
# use function to determine percentage of votes per candidate
percent_votes_1 = percent_votes(candidate_1_votes)
percent_votes_2 = percent_votes(candidate_2_votes)
percent_votes_3 = percent_votes(candidate_3_votes)

print(round(percent_votes_1, 0))
print(round(percent_votes_2, 0))
print(round(percent_votes_3, 0))

# print results:
print('Election Results')
print('_________________________________________')
print('Total Votes: ' + str(total_votes))
print('_________________________________________')
print(str(candidate[0]) + ': ' + str(votes[0]))
print(str(candidate[1]) + ': ' + str(votes[1]))
print(str(candidate[2]) + ': ' + str(votes[2]))
print('Greatest Decrease in Profits: ' + str(greatestd_month) + '($' + str(greatest_loss) + ')')