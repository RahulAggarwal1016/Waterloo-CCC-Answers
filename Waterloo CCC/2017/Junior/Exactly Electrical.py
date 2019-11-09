"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2017 - Exactly Electrical
https://cemc.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf
"""

starting = input()
ending = input()
charge = int(input())

starting = starting.split(" ")
ending = ending.split(" ")

x_coordinates = [int(starting[0]), int(ending[0])]
y_coordinates = [int(starting[1]), int(ending[1])]

units_away = (max(x_coordinates) - min(x_coordinates)) + (max(y_coordinates) - min(y_coordinates))


if units_away == charge or charge % units_away == 0:
    print("Y")
else:
    print("N")