"""Create a dictionary and take input from 
the user and return the meaning of the word 
from the dictionary"""

ch = ""
print("The meaning you wanna know among these words:-")
print("1. Consider\n2. Minute\n3. Accord\n4. Evident")
mydict = {"Consider": "deem to be", "Minute": "infinitely or immeasurably small",
          "Accord": "concurrence of opinion", "Evident": "clearly revealed to the mind"}
print("Enter the word:")
ch = input()
print(ch.capitalize(), ": ", mydict[ch.capitalize()])
