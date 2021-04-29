import os


import csv

# Assign file location with the pathlib library

with open("election_data.csv",encoding="ISO 8859-1") as csvfile:


    # Store data under the csvreader variable
    csvreader = csv.reader(csvfile,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader) 
    print (header)    
  # Declare Variables 
    
    Khan = []
    Correy = []
    Li = []
    otooley = []
    votes = []
    candidates = []
    county = []


    # Iterate through each row in the csv
    for row in csvreader :
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #VOTE COUNT
    total_votes = (len(votes))
    print (total_votes)

    #Votes by Person
    for candidate in candidates :
        if candidate == "Khan" :
            Khan.append(candidates)
            Khan_votes = len(Khan)
        elif candidate == "Correy" :
            Correy.append(candidates)
            Correy_votes = len(Correy)
        elif candidate == "Li" :
            Li.append(candidates)
            Li_votes = len(Li)
        else :
            otooley.append(candidates)
            otooley_votes = len(otooley)
    print(Khan_votes)
    print(Correy_votes)
    print(Li_votes)
    print(otooley_votes)

    #Percentages
    khan_percent = round(((Khan_votes /total_votes) * 100),2)
    correy_percent = round(((Correy_votes /total_votes) * 100),2)
    li_percent = round(((Li_votes /total_votes) * 100),2)
    otooley_percent = round(((otooley_votes /total_votes) * 100),2)
    print(khan_percent)
    print(correy_percent)
    print(li_percent)
    print(otooley_percent)

    # Winner 
    if khan_percent > max(correy_percent,li_percent,otooley_percent) :
        winner = "Khan"
    elif correy_percent > max (khan_percent,li_percent,otooley_percent) :
        winner = "correy"
    elif li_percent > max (correy_percent,khan_percent,otooley_percent) :
        winner = "li"
    else:
        winner = "otooley"

        #Print Statements

    print (f"Election Results") 
    print (f"________________________________________________________________________") 
    print (f"Total Votes : {total_votes}" + "\n")
    print (f"________________________________________________________________________") 
    print (f"Khan : {khan_percent}% ({Khan_votes})")
    print (f"correy : {correy_percent}% ({Correy_votes})")
    print (f"li : {li_percent}% ({Li_votes})") 
    print (f"otooley : {otooley_percent}% ({otooley_votes})") 
    print (f"________________________________________________________________________") 
    print(f"Winner : {winner}") 
    print (f"________________________________________________________________________")


