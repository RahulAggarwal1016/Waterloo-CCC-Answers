"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2013 - Time on Task
https://www.cemc.uwaterloo.ca/contests/computing/2013/stage1/juniorEn.pdf
"""

availMin = int(input())
numChores = int(input())

chores = []

for i in range(1, numChores + 1):
    temp = int(input())
    chores.append(temp)

counter = 0

while availMin > 0:
    lowest_number = min(chores)
    if availMin - lowest_number >= 0:
        counter += 1
        availMin -= lowest_number
        chores.remove(lowest_number)

print(counter)