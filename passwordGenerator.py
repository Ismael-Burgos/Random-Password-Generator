#Import the needed libraries 
import random 
import string 

#Create a function of a desired length to generate a password
def passwordGeneration(length = 18):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

#Create a variable to store the generated password and print it
new_password = passwordGeneration()
print(new_password)