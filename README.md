# Election Analysis

## Overview of Election Audit
Perorm an elction audit for the Colorado congressional election using Python. The Colorado Board of Elections has requested the following information:
1. Total number of votes cast
2. List of candidates that received votes
3. Number of votes received by each candidate
4. Percentage of votes each candidate won
5. Winner of the election based on popular vote
6. Voter turnout for each county
7. Percentage of votes from each county out of the total count
8. The county with the highest turnout

## Election-Audit Results
![Election_Analysis](https://github.com/mdhugge/election_analysis/blob/main/Analysis/Election_Analysis.png)

- Number of votes cast in this congressional election
Each row in [Election_results](docs/election_results.csv) represents one vote, so to calculate the total number of votes cast I needed to calculate how many rows there are.
```
for row in reader:
  total_votes = total_votes + 1
```
- Breakdown of the number of votes and the percentage of total votes for each county in the precinct
The candidate name is the third column in 
- County with the largest number of votes

- Breakdown of the number of votes and the percentage of the total votes each candidate received

- Wiinning candidate, their vote count, and their percentage of the total votes

## Election-Audit Summary
