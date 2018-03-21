def w1(a):
    print("w1(): " + str(a))

w1(1)

def w2(a):
    print("w2(): " + str(a))

w2(1)

def w3(a):
    print("w3(): " + str(a))

w3(1)

ws = [w1,w2,w3]

for w in ws:
    w(1)

wd = {
    "method1": w1,
    "method2": w2,
    "method3": w3
}

wd["method1"](1)

     



