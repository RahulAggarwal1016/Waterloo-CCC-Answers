"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 1997 - Sentences
https://www.cemc.uwaterloo.ca/contests/computing/1997/stage1/1997CCCStage1Contest.pdf
"""

nouns = int(input())
verbs = int(input())
objects = int(input())

nounList = []
for i in range(1, nouns + 1):
    nounInput = input()
    nounList.append(nounInput)

verbList = []
for i in range(1, verbs + 1):
    verbInput = input()
    verbList.append(verbInput)

objectList = []
for i in range(1,objects + 1):
    objectInput = input()
    objectList.append(objectInput)

for n in nounList:

    for v in verbList:

        for o in objectList:

            print(n, v, o)
