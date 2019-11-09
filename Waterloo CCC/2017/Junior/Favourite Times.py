"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Junior 2017 - Favourite Times
https://cemc.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf
"""

hour = 12
minute = 0
time = int(input())
arithmetics = 0


for i in range(1, time+1):

    if i >= 60:
        remainder = i//60
        remainder2 = i - remainder*60
        hour += remainder
        minute += remainder2
        if hour >= 13:
            hour = hour - 12
    else:
        minute += i

    if minute < 10:
        new_minutes = ""
        new_minutes = str("0") + str(minute) 
        time = list(str(hour)) + list(new_minutes)
    else:
        time = list(str(hour)) + list(str(minute))

    if len(time) == 4: #Determining if Arithmetic for 4 Digits

        #Arithmetic from back to front
        container1 = int(time[3]) - int(time[2])
        container2 = int(time[2]) - int(time[1])
        container3 = int(time[1]) - int(time[0])

        #Arithmetic start to back
    
        container4 = int(time[0]) - int(time[1])
        container5 = int(time[1]) - int(time[2])
        container6 = int(time[2]) - int(time[3])

        if container1 == container2 and container1 == container3:
            arithmetics += 1

        elif container4 == container5 and container4 == container6:
            arithmetics += 1
    
    elif len(time) == 3:

        #Arithmetic from back to front
        container1 = int(time[2]) - int(time[1])
        container2 = int(time[1]) - int(time[0])

        #Arithmetic start to back
    
        container4 = int(time[0]) - int(time[1])
        container5 = int(time[1]) - int(time[2])

        if container1 == container2 or container4 == container5:
            arithmetics += 1

    hour = 12
    minute = 0

print(arithmetics)