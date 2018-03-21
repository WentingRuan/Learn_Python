a = [1,2,3] # list
print(a)
print(a[1])


b = { "a": 24, "b": 25, "c": 3, "1c": 3 }
b = {
    "a": 3,
    "b": 5
}

print(b)

def f(n):
    if n==1:
        return 1
    else:
        return f(n-1) * n

def f1(n):
    ret = 1
    for i in range(1, n+1, 1):
        ret *= i
    return ret

def f2(n):
    ret = 1
    i = 1
    while i < n+1:
        ret *= i
        i += 1
    return ret

f3 = f2

print("10!=" + str(f(10)) ) 
print("10!=" + str(f1(10)) ) 
print("10!=" + str(f2(10)) ) 
print("10!=" + str(f3(10)) ) 

a = list(range(10))
print(str(a) + " --- " + str(a[3:5]) )

b = "0123456789" #"".join(map(str, a))
print(b + " --- " + b[3:5])


global_v = 3

def ff():
    global_v = 6
    global_v += 1
    print(global_v)

ff()
print(global_v)


