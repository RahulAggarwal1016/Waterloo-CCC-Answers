"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 1998 - Cross-Number Puzzle
https://www.cemc.uwaterloo.ca/contests/computing/1998/stage1/1998CCCStage1Contest.pdf
"""

perNumbers = []

for number in range(1000, 9999+1):

    totalSum = 0

    for i in range(1, number):
        if number % i == 0:
            totalSum += i
    
    if totalSum == number:
        perNumbers.append(number)

print("Perfect Numbers:" , perNumbers)

print("")

print("Sum of Digits Cubed Numbers: ")
for i in range(100, 999):

    i = str(i)

    if int(i[0])**3 + int(i[1])**3 + int(i[2])**3 == int(i):
        print(i)

print("")

print("Perfect Squares: ")

import math

for i in range(1000, 9999 + 1):
    if math.sqrt(i) % 1 == 0:
        print(i, math.sqrt(i))

print("")

print("Prime numbers: ")

for i in range(10, 99 + 1):

    factors = 0
    for x in range(1, i + 1):

        if i % x == 0:
            factors +=1

    if factors == 2:
        print(i)

print("")

print("palindrome numbers: ")

for i in range(1000,9999 + 1):
    i = str(i)
    
    if i == i[::-1]:
        print(i)

#8128
# 1 2
#8118
# 371
    