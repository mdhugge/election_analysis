# Election Analysis

## Overview of Election Audit
Perform an election audit for the Colorado congressional election using Python. The Colorado Board of Elections has requested the following information:
1. Total number of votes cast
2. List of candidates that received votes
3. Number of votes received by each candidate
4. Percentage of votes each candidate won
5. Winner of the election based on popular vote
6. Voter turnout for each county
7. Percentage of votes from each county out of the total count
8. The county with the highest turnout

## Resources
Data Source: [election_results](https://github.com/mdhugge/election_analysis/blob/main/Resources/election_results.csv)

Software: Python 3.7.6, Visual Studio Code 1.52

## Election Audit Results
![Election_Analysis](https://github.com/mdhugge/election_analysis/blob/main/Analysis/Election_Analysis.png)

- Number of votes cast in this congressional election

Each row in [election_results](https://github.com/mdhugge/election_analysis/blob/main/Resources/election_results.csv) represents one vote, so to calculate the total number of votes cast I needed to calculate how many rows there are.

```
for row in reader:
  total_votes = total_votes + 1
```

![Total_Votes](https://github.com/mdhugge/election_analysis/blob/main/Resources/Total%20Votes.png)

- Breakdown of the number of votes and the percentage of total votes for each county in the precinct

The county name is the second column in [election_results](https://github.com/mdhugge/election_analysis/blob/main/Resources/election_results.csv), so using an index I was able to obtain the name of each county and add it to a list of all counties. An if statement was used to ensure that each county was only included once in the list and to begin tracking the number of votes cast in each county. A for loop was used to calculate the total number of votes for each county and precentage of votes each county cast. 

```
for row in reader:
  county_name = row[1]
  
  if county_name not in county_options:
    county_options.append(county_name)
    county_votes[county_name] = 0
  
  county_votes[county_name] += 1

for county_name in county_votes:
  votes_percounty = county_votes[county_name]
  vote_percentage_county = float(votes_percounty) / float(total_votes) * 100
```

![County_Votes](https://github.com/mdhugge/election_analysis/blob/main/Resources/County%20Votes.png)

- County with the largest number of votes

An if statement was used to determine the county with the largest turnover. 

```
for county_name in county_votes:

  if (votes_percounty > county_count):
    county_count = votes_percounty
    winning_county = county_name 
```

![County_Turnover](https://github.com/mdhugge/election_analysis/blob/main/Resources/County%20Turnover.png)

- Breakdown of the number of votes and the percentage of the total votes each candidate received

The candidate name is the third column in [election_results](https://github.com/mdhugge/election_analysis/blob/main/Resources/election_results.csv), so using an index I was able to obtain the candidate name and add it to a list of all candidates. An if statement was used to ensure that each candidate was only included once in the list and to begin tracking the number of votes for each candidate. A for loop was used to calculate the total number of votes for each candidate and precentage of votes each candidate won. 

```
for row in reader:
  candidate_name = row[2]
  
  if candidate_name not in candidate_options:
    candidate_options.append(candidate_name)
    candidate_votes[candidate_name] = 0
  
  candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
  votes = candidate_votes.get(candidate_name)
  vote_percentage = float(votes) / float(total_votes) * 100
```

![Candidate](https://github.com/mdhugge/election_analysis/blob/main/Resources/Candidate.png)

- Winning candidate, their vote count, and their percentage of the total votes

An if statement was used to determine the winning candidate, the number of votes they recieved and the percentage of total votes they received. 

```
for candidate_name in candidate_votes:

  if (votes > winning_count) and (vote_percentage > winning_percentage):
    winning_count = votes
    winning_candidate = candidate_name
    winning_percentage = vote_percentage 
```

![Winner](https://github.com/mdhugge/election_analysis/blob/main/Resources/Winner.png)

## Election Audit Summary
This code uses variables and indexing to reference candidates and counties from [election_results](https://github.com/mdhugge/election_analysis/blob/main/Resources/election_results.csv). Since, the names of candidates and counties are not fixed in the code, it makes it easy to use the same code for other congressional elections with different candidates and counties as long as the data file follows a similar structure.

The data that was used to create this code only included the county location of each candidate. If the data included other information such as the district each voter resides in the code could be modified to determine the number of votes cast in each district and the district with the highest turnover. This new code would be very similar to the code that was written to determine county specific statistics in this election. This code could also be modified to look at the winning candidate for each county, by determining the number of votes cast for each candidate in every county. 
