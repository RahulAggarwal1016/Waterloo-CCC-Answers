"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2018 - Occupy Parking
https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/juniorEF.pdf
"""

parking_spots = int(input("Enter a number: "))

first_row = []

for i in range(1, parking_spots + 1):
    temp = input("First Row: ")
    first_row.append(temp)

second_row = []

for i in range(1, parking_spots + 1):
    temp = input("Second Row:")
    second_row.append(temp)

print(first_row)
print(second_row)

shared_spaces = 0

counter = 0

while counter < parking_spots:
    if first_row[counter] == "C" and second_row[counter] == "C":
        shared_spaces += 1
    counter += 1

print(shared_spaces)