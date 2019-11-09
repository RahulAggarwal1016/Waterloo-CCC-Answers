"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Senior 1997 - Longest Palindrome
https://www.cemc.uwaterloo.ca/contests/computing/1997/stage2/2a-prob.html
"""

def isPalin(word):
    if word == word[::-1]:
        return True
    else:
        return False

num_of_words = int(input())

wordList = []

for i in range(1, num_of_words + 1):
    user_input = input()
    wordList.append(user_input)

for word in wordList:

    longest_palin = ""
    longest_length = 0

    for letter in word:

        master_location = word.index(letter)
        #What if there is two of the same letter????>?>?> index is messed up in that case
        new_string = word[master_location]

        while master_location + 1 <= len(word) - 1:
            master_location += 1
            new_string += word[master_location]
            if isPalin(new_string) and len(new_string) > longest_length:
                longest_palin = new_string
                longest_length = len(new_string)

    word = word.replace(letter,"", 1)
    #can't change the for loop, it's set in stone :(

    print("longest palin is:", longest_palin)
    print("it's length is", longest_length)