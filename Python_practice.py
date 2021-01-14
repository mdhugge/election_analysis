#import random
#print("Let's Play Rock Paper Scissors!")
#options = ['r', 'p', 's']
#computer_choice = random.choice(options)
#user_choice = input('Make your choice:(r)ock, (p)aper, (s)cissors?')
#print("Computer chose: " + computer_choice)

#if user_choice == computer_choice:
    #print("tie")
#elif user_choice == "r" and computer_choice == 'p':
        #print("you lose")
#elif user_choice == 'r' and computer_choice == 's':
        #print("you win")
#elif user_choice == 'p' and computer_choice == 'r':
        #print("you win")
#elif user_choice == 'p' and computer_choice == 's':
        #print("you lose")
#elif user_choice == 's' and computer_choice == 'p':
        #print("you lose")
#elif user_choice == 's' and computer_choice == 'r':
        #print("you lose")

import os
import csv

video = input('What show or movie are you looking for?')

csvpath = os.path.join('netflix.csv')
txtpath = os.path.join('netflix_data.txt')

found = False

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            # Bonus - Step 2: Set the variable created in Step 1 to confirm we have found the video
            found = True

            # Bonus - Step 3: Stop at first results to avoid duplicates
            with open(txtpath, 'w') as textfile:
                netflix_data = (
                    f'Title: {row[0]}\n'
                    f'Rating Level: {row[1]}\n'
                    f'Rated: {row[5]}\n'
                    )
                textfile.write(netflix_data)

                print(netflix_data)
            
            break

    # Bonus - Step 4:  If the video is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")


    
    




    