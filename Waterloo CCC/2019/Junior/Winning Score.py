"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2019 - Winning Score
https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf
"""

#input
three_a= int(input())
two_a = int(input())
one_a = int(input())
three_b = int(input())
two_b = int(input())
one_b = int(input())

#processing
sum_a = (three_a*3) + (two_a*2) + (one_a*1)
sum_b = (three_b*3) + (two_b*2) + (one_b*1)

#output
if sum_a > sum_b:
  print("A")
elif sum_a < sum_b: 
  print("B")
else:
  print("T")