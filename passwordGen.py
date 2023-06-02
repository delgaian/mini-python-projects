import random

print("\n--Password Generator--\n")
print("This program will generate a new password based on the user input")
#characters used in the generation of passwords
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\]^_`{|}~0123456789'
#gather user input of how many passwords they would like to generate
number = input('How many passwords would you like to generate?\n: ')
#typecast the input into an int
number = int(number)
#grab the length of the password
length = input('What length would you like your password(s)?\n: ')
#type cast to an int
length = int(length)
#prompt the generated passwords
print('\nYour passwords:')
#for the passwords in the range of the number of passwords to generate
for password in range(number):
    #intilize a string to add the characters
    passwords = ''
    #for each character in the length
    for c in range(length):
        #add a random character from the list of character choices
        passwords += random.choice(chars)
    #print the password generated
    print(passwords)