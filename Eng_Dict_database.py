# Importing required libraries
import mysql.connector
from difflib import get_close_matches

# Making the Connection object
con = mysql.connector.connect(
user = '********',
password = '*********',
host = '**********',
database = '*********'
)

# Making the Cursor object
cursor = con.cursor()

# Giving user to input word
user_input = input('Enter a word: ')
# Query from database and store the words
query = cursor.execute('select Expression from Dictionary')
results = cursor.fetchall()
# Query from database and store the words and meaning
query1 = cursor.execute('select * from Dictionary where Expression = "{}"'.format(user_input))
results1 = cursor.fetchall()
# Formatting the words result
res = [i[0] for i in results]

# For words which are there in database
if len(results1)!=0:
    for i in results1:
        print(i[1])
# To give the user similar words
elif len(get_close_matches(user_input,res,cutoff=0.7))!=0:
    user_input1 = input('You may be looking for {}. Enter Y for yes or N for no: '.format(get_close_matches(user_input,res,cutoff=0.7)[0])).lower()
    # Giving user the chance to use the recommendation
    if user_input1=='y':
        query2 = cursor.execute('select * from Dictionary where Expression = "{}"'.format(get_close_matches(user_input,res,cutoff=0.7)[0]))
        results2 = cursor.fetchall()
        for i in results2:
            print(i[1])
    elif user_input1=='n':
        print('Word not found. Please search for another word.')
    else:
        print('Could not understand your entry.')
else:
    print('Word not found. Please search for another word.')

