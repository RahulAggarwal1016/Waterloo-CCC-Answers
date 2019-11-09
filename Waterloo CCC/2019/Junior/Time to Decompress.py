"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2019 - Time to Decompress
https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf
"""

lines = int(input())

master_list = []

for i in range(1,lines + 1):
    user_input = input()
    master_list.append((user_input[2])*int(user_input[0]))

for j in master_list:
    print(j)