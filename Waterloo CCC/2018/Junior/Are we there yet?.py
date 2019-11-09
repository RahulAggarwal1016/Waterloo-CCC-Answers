"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2018 - Are we there yet?
https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/juniorEF.pdf
"""

inputs = []

for i in range(1,5):
    distance = int(input())
    inputs.append(distance)

#City 1:
city1_list = [0]
total = 0
for i in range(1,5):
    total += inputs[i-1]
    city1_list.append(total)

print(city1_list)

#City 2:
city2_list = []
for i in range(1,6):
    city2_list.append(city1_list[i-1] - city1_list[1])
city2_list[0] = city1_list[1]
print(city2_list)

#City3:
city3_list = [city1_list[2]]
city3_list.append(inputs[1])
city3_list.append(0)
city3_list.append(inputs[2])
city3_list.append(inputs[2] + inputs[3])
print(city3_list)

#City4:
city4_list = [city1_list[3]]
city4_list.append(inputs[1]+inputs[2])
city4_list.append(inputs[2])
city4_list.append(0)
city4_list.append(inputs[3])
print(city4_list)

#City5:
total = city1_list[4]
city5_list = [total]
for i in range(1,4):
    total -= inputs[i-1]
    city5_list.append(total)
city5_list.append(0)
print(city5_list)   