"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2017 - Shifty Sum
https://cemc.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf
"""

user_input = int(input("Enter a number: "))
shifts = int(input("Enter number of times to shift: "))
shiftSum = 0

shiftSum += user_input

for i in range(1, shifts + 1):
    user_input *= 10 
    shiftSum += user_input
    
print(shiftSum)