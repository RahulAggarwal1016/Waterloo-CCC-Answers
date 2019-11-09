"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2018 - Sunflowers
https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/juniorEF.pdf
"""

num_of_plants = int(input())

master_list = []

for i in range(1, num_of_plants + 1):
    user_input = input()
    user_input = user_input.split(" ")
    master_list.append(user_input)

print(" ")

#360 degrees
loop = True

for i in master_list:
    temp = i.copy()
    temp.sort()
    if temp != i:
        loop = False

a_list = []

for i in master_list:
    a_list.append(i[0])

a_listCopy = a_list.copy()
a_listCopy.sort()

if a_listCopy != a_list:
    loop = False

#Print Correct Answer
if loop == True:
    print("Original data was rotated 360 degrees")
    print(" ")
    for i in master_list:
        big_string= ""
        for a in i:
            big_string += str(a) + " "
        print(big_string)

#180 degrees

loop2 = True

for i in master_list:
    temp2 = i.copy()
    temp2.sort()
    if temp2[::-1] != i:
        loop2 = False

b_list = []

for i in master_list:
    b_list.append(i[0])

b_listCopy = b_list.copy()
b_listCopy.sort()

if b_listCopy[::-1] != b_list:
    loop2 = False

if loop2 == True:
    print("Oringial data was rotated 180 degrees")
    print(" ")

    master_list.reverse()

    for i in master_list:
        i2 = i.copy()
        i2.reverse()
        blank_space = ""
        for b in i2:
            blank_space += str(b) + " "
        print(blank_space)

#90 degrees left

loop3 = True

for i in master_list:
    temp3 = i.copy()
    temp3.sort()
    if temp3 != i:
        loop3 = False

c_list = []

for i in master_list:
    c_list.append(i[0])

c_listCopy = c_list.copy()
c_listCopy.sort()
if c_listCopy[::-1] != c_list:
    loop3 = False

if loop3 == True:
    print("The original data was rotated 90 degrees to the left")
    print(" ")

    limit = len(master_list[0]) - 1

    new_masterlist = []
    counter = 0

    while counter <= limit:
        sub_list = []
        for i in master_list:
            sub_list.append(i[counter])
        new_masterlist.append(sub_list)
        counter += 1

    for i in new_masterlist:
        i3 = i.copy()
        i3.reverse()
        white = ""
        for d in i3:
            white += str(d) + " "
        print(white)

#90 degrees right

loop4 = True

for i in master_list:
    temp4 = i.copy()
    temp4.sort()
    temp4.reverse()
    if temp4 != i:
        loop4 = False

e_list = []

for i in master_list:
    e_list.append(i[0])

e_listcopy = e_list.copy()
e_listcopy.sort()

if e_listcopy != e_list:
    loop4 = False

if loop4 == True:
    print("Original was rotated 90 degrees right")
    print(" ")

    limit = len(master_list[0]) - 1

    new_masterlist = []
    counter = 0

    while counter <= limit:
        sub_list = []
        for i in master_list:
            sub_list.append(i[counter])
        new_masterlist.append(sub_list)
        counter += 1

    new_masterlist.reverse()

    for i in new_masterlist:
        white2 = ""
        for e in i:
            white2 += str(e) + " "
        print(white2)

if loop == False and loop2 == False and loop3 == False and loop4 == False:
    print("There was no rotation")