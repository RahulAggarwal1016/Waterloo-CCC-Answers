"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2005 - Bananas
https://cemc.uwaterloo.ca/contests/computing/2005/stage1/juniorEn.pdf
"""

emptyList = []
loop = True
counter = 0

while loop:
  txt = input().upper()

  while "BAS" in txt or "ANA" in txt:
    txt = txt.replace("ANA", "A")
    txt = txt.replace("BAS", "A")
  
  emptyList.append(txt)
  
  listLen = len(emptyList)
  
  if txt == "X":
    loop = False

for number in range (1, listLen +1):
  temporary = emptyList[counter]
  if temporary == "A":
    temporary = "Yes"
  elif temporary == "X":
    temporary = "X"
  else:
    temporary = "No"
  print(temporary)
  counter += 1