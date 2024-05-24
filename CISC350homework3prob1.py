#!/usr/bin/python

# imports hashlib for use
import hashlib

# stores the txt files into passwords and hashes to work with
passwords = open("xato-net-10-million-passwords.txt", "r")
hashes = open("hashes.txt", "r")

# creates two empty arrays to put the values of the hashed passwords and the strings of the passwords into.
hashed = []
password = []

# puts the hashed passwords into a list along with putting the string of the passwords into the list as well
for line in passwords.readlines():
    line = line.strip()
    password.append(line)
    hashed.append(hashlib.sha1(line.encode()).hexdigest())

# takes the two lists and checks the hashes that are given with the hashes of the password list
# prints out the current password it is checking the hash of along with the given hash if they match
count = 1
for check in hashes.readlines():
    looking = check.strip()
    count = count + 1
    x = 0
    while x < len(hashed):
        if hashed[x] == looking:
            print("found for" + str(count) + ": " + check + "\t the password is: " + password[x])
            break
        x = x + 1




