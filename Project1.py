# Importing the required libraries
import json
from difflib import SequenceMatcher
from difflib import get_close_matches
# Loading the data
data = json.load(open('Project1data.txt'))
# Converting the keys of dict into lower case and storing it in another dict
data1 = dict((key.lower(),value) for key,value in data.items())
# User input and handling case sensitivity
user_input = input('Enter a word: ').lower()
# Function to get the meaning of english words
def meaning(user_input):
    if user_input in data1:
        return data1.get(user_input)
# To recommend the user similar words
    elif len(get_close_matches(user_input,data1.keys(),cutoff=0.7))!=0:
        user_input1 = input('You might be looking for {}. Enter Y for yes or N for no: '.format(get_close_matches(user_input,data1.keys(),cutoff=0.7)[0])).lower()
        if user_input1=='y':
            return data1.get(get_close_matches(user_input,data1.keys(),cutoff=0.7)[0])
        elif user_input1=='n':
            return 'Word not found. Please enter another word.'
        else:
            return 'Could not understand your entry.'
    else:
        return 'Word not found. Please enter another word.'

# Making the ouput clean   
output = meaning(user_input)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
