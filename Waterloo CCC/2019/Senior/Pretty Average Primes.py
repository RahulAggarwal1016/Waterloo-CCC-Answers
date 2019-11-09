"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Waterloo CCC: Senior 2019 - Pretty Average Primes
https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/seniorEF.pdf
"""


def isPrime(num):
    if num <= 1:
        return False
    else:
        factorCounter = 0
        for i in range(1, num + 1):
            if num % i == 0:
                factorCounter += 1

        if factorCounter == 2:
            return True
        else:
            return False

def primeList(num2):
    temp_list = []
    for i in range (1,num2+ 1):
        if isPrime(i):
            temp_list.append(i)
    return temp_list

def average_primes(user_input):
    user_input*=2
    primes_to_user_input = primeList(user_input)

    temp_list = []

    for x in primes_to_user_input:
        y = user_input - x
        if x + y == user_input and isPrime(y):
            temp_list.append(x)
            temp_list.append(y)
            return temp_list

    if len(temp_list) != 2:
        return [0]

num_of_inputs = int(input())
user_input_list = []

for i in range(1, num_of_inputs + 1):
    value = int(input("Enter a value to check: "))
    user_input_list.append(value)

for i in user_input_list:
    print(average_primes(i))