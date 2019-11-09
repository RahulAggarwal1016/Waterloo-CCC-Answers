"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 1998 - Censor
https://www.cemc.uwaterloo.ca/contests/computing/1998/stage1/1998CCCStage1Contest.pdf
"""

num_of_lines = int(input())

phraseList = []

for i in range(1, num_of_lines + 1):
    user_input = input()
    phraseList.append(user_input)

for sentence in phraseList:

    sentence = sentence.split(" ")

    for word in sentence:
        if len(word) == 4:
            sentence[sentence.index(word)] = "****"
    
    temp = ""

    for j in sentence:
        temp += j
        temp += " "

    print(temp)
    print("")