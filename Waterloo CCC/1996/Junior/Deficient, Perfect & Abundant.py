"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 1996 - Deficient, Perfect, Abundant
https://www.cemc.uwaterloo.ca/contests/computing/1996/stage1/a-prob.html
"""

numInputs = int(input())
inputsList = []

for i in range(1, numInputs + 1):
    user_input = int(input())
    inputsList.append(user_input)

for i in inputsList:
    divSum = 0
    for w in range (1,i):
        if i % w == 0:
            divSum += w
    if divSum == i:
        print(i,'is a perfect number')
    elif divSum < i:
        print(i, "is a deficient number")
    else:
        print(i, "is an abundant number")