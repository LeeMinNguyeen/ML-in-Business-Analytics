'''
    Name: Le Minh Nguyenn
    Student ID: K224161829
'''

import random as rd

### Review List ###

list = []

for i in range(10):
    x = rd.Random().randint(0,100)
    list.append(x)
    
print("List: ", list)

print("Gia tri tai phan tu thu 2 = ", list[2])

### Loc cac so nguyen to ###

def isprime(x):
    '''
    Check if a number is prime.
    '''
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def listprime(list):
    '''
    Filter out prime numbers from a list.
    '''
    prime_list = []
    for i in list:
        if isprime(i):
            prime_list.append(i)
    return prime_list

print("List of prime numbers:", listprime(list))