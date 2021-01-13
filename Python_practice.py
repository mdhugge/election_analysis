


import csv
import os

## Open file to read
file_to_load = 'Analysis_Projects/Election_Analysis/Resources/election_results.csv'
with open(file_to_load) as election_data:
    print(election_data)
## Create Text file
file_to_save = 'Analysis_Projects/Election_Analysis/Analysis/election_analysis.txt'
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n ---------------------------\nArapahoe\nDenver\nJefferson")

