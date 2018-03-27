name="wenting"

print("hello "+name)

import math
math.trunc(3.64)
math.floor(3.64)
math.ceil(3.64)
round(3.64)

# If

day="Monday"

def Day(day):
    if day=="Monday":
        return "Workday"
    else:
        return "Not Monday"

Day(day)

# For and While
a=[1,2,"12"]
def console():
    for e in a:
        print(e)

console()

def plus():
    i = 0
    while i<len(a):
        print(a[i])
        i = i+1

plus()

def factorial(n):
    ret = 1
    while n>=1:
        ret *= n
        n -= 1
    return ret

factorial(3)

def Sum(n):
    ret = 0
    while(n>0):
        ret += factorial(n)
        n -= 1
    return ret

Sum(3)

def facSum(n):
    s = 0
    f = 1
    i = 1
    while(n>0):
        f = i*f
        s = s+f
        i += 1
        n -= 1
    return s 

facSum(3)






