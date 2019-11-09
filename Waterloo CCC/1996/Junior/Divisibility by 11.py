"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 1996 - Divisibility by 11
https://www.cemc.uwaterloo.ca/contests/computing/1996/stage1/b-prob.html
"""

user_input = input("Enter a number: ")
print(user_input)

while len(user_input) != 2:
    list_of_num = list(user_input)
    unitDigit = int(list_of_num.pop())
    reattach = ""
    for i in list_of_num:
        reattach += i
    reattach = int(reattach)
    user_input = str(reattach - unitDigit)
    print(user_input)

if user_input == "11":
    print(user_input, "is dvisible by 11")
else:
    print(user_input, "is not divisible by 11")