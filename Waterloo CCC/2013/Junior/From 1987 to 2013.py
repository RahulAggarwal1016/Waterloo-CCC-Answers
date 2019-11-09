"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2013 - From 1987 to 2013 (Distinctive Digits)
https://www.cemc.uwaterloo.ca/contests/computing/2013/stage1/juniorEn.pdf
"""

starting_number = int(input("Enter a starting year: "))
starting_year = starting_number 

loop = True

while loop:
    digit_list = []
    
    for digit in str(starting_year):
        digit_list.append(digit)

    total = 0

    for i in digit_list:
        total += digit_list.count(i)

    if total == 4 and starting_year != starting_number:
        loop = False
    else:
        starting_year += 1

print(starting_year)