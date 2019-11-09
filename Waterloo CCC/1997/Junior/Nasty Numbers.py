"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 1997 - Nasty Numbers
https://www.cemc.uwaterloo.ca/contests/computing/1997/stage1/1997CCCStage1Contest.pdf
"""

num_of_numbers = int(input())

numList = []
for i in range(1, num_of_numbers + 1):
    user_input = int(input())
    numList.append(user_input)

for i in numList:

    combinations = []

    for divisor in range(1, i + 1):
        
        if i % divisor == 0:
            
            pairList = []
            temp = i//divisor

            if divisor > temp:
                pairList.append(divisor)
                pairList.append(temp)
            else:
                pairList.append(temp)
                pairList.append(divisor)
            
            if pairList not in combinations:
                combinations.append(pairList)

    isNasty = False

    for x in combinations:
    
        difference = x[0] - x[1]

        master_location = combinations.index(x) + 1

        while master_location != combinations.index(x):
            
            if master_location > len(combinations) - 1:
                master_location = 0
            elif combinations[master_location][0] + combinations[master_location][1] == difference:
                master_location = combinations.index(x)
                isNasty = True
            else:
                master_location += 1
    
    if isNasty:
        print(i, "is nasty")
    else:
        print(i, "is not nasty")

