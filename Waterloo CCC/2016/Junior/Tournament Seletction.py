"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2016 - Tournament Selection
https://www.cemc.uwaterloo.ca/contests/computing/2016/stage%201/juniorEn.pdf
"""

loopCounter = 0
winCounter = 0

while loopCounter < 6:
  user_input = input("Enter if you won or lost (W/L): ")
  if user_input == "W":
    winCounter += 1
  loopCounter += 1

if winCounter >= 5:
  print("1")
elif winCounter >= 3:
  print("2")
elif winCounter >= 1:
  print("3")
else:
  print("-1")