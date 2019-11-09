"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2019 - Flipper
https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf
"""

lines = list(input())
one = "1"
two = "2"
third = "3"
fourth = "4"
 
horizontalflip = [3, 4, 1, 2]
verticalflip = [2, 1, 4, 3]
numberOfChanges = len(lines)
for each in lines:
  if each == "H":
    oldone = one
    oldtwo = two
    oldthird = third
    oldfourth = fourth
 
    one = one.replace(one, third)
    two = two.replace(two, fourth)
    third = third.replace(third, oldone)
    fourth = fourth.replace(fourth, oldtwo)
  if each == "V":
    oldone = one
    oldtwo = two
    oldthird = third
    oldfourth = fourth  
 
    one = one.replace(one, two)
    two = two.replace(two, oldone)
    third = third.replace(third, fourth)
    fourth = fourth.replace(fourth, oldthird)      
 
print(one + two)
print(third + fourth)