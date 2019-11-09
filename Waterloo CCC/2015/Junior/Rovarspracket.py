"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2015 - RovarSpraket
https://cemc.uwaterloo.ca/contests/computing/2015/stage%201/juniorEn.pdf
"""

word = input("Enter a word: ")
alph = "abcdefghjiklmnopqrstuvwxyz"
transword = ""

for letter in word:
    if letter in "aeiou":
        transword += letter
    
    else:
        transword += letter
        if letter in "bcyz":
            transword += "a"
        elif letter in "dfg":
            transword += "e"
        elif letter in "hjkl":
            transword += "i"
        elif letter in "mnpqr":
            transword += "o"
        elif letter in "stuvwx":
            transword += "u"
        location = alph.find(letter) + 1
        if location == 26:
            location = 0
        while alph[location] in "aeiou":
            location += 1
        transword += alph[location]

print(transword)