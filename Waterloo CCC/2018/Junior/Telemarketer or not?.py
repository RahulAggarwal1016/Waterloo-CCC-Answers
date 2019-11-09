"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2018 - Telemarketer or not?
https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/juniorEF.pdf
"""

firstnumber = int(input())
secondnumber = int(input())
thirdnumber = int(input())
fourthnumber = int(input())
checker = 0

if (firstnumber == 8 or firstnumber == 9):
  checker += 1

if (fourthnumber == 8 or fourthnumber == 9):
  checker += 1

if (secondnumber == thirdnumber):
  checker += 1


if checker == 3:
  print ("ignore")
else:
  print ("This is not a telemarketing number")