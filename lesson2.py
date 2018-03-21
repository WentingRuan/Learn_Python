# string

a = "123456789"
a[0:3]
a[2:3]
print(a[0:3]+ a[2:3])

#slice(stop) or slice(start,stop,step)
a[sclice(3)]
a[slice(0,9,3)]

print("abc"+"a")
print(123 + int(a))

#
a = [1,2,3]
a * 3
a = ["123","345"]
a * 3

'''
# numpy.repeat
import numpy as np
np.repeat(a,3,0) # array()

b = np.array([[1,2],[3,4]])
np.repeat(b,[2,2],axis = 0)
np.repeat(b,[2,2],axis = 1)
'''

# string search

a = "a3a3a3a3"

a.find("3")
a.find("3",3) # find(string,start_index)

a.startswith("a")
a.endswith("3")

a.index("3",0)
a.index("a",3)

# 查看对象的方法(属性)
dir(a)

""""
 oop object-oriented programming
"""

''' failed constructor
class Person(name,age):
    def name(name):
        print ("my name is" + name)
    
    def age(age):
        print (name + "is" + age + "years old")

wt = Person()
wt.name("wenting")
wt.age(14)
'''

class Person:
    def __init__ (self, name, age): #__ini__ has two _ _
        self.name = name
        self.age = age

    def profile(self):
         print ("my name is " + str(self.name))
         print ("my age is " + str(self.age) + "years old")


wt = Person("wenting", 24)
wt.profile()
el = Person("edwinjhlee",28)
print(el.age)

# String <=> number

a = 123
type(a)
type(a) is int
type(a) is str

str(a) # change a into string
a = "123"
int(a) # change a into integer

# 进制转换
## 16 <-> 10

hex(19) # 16
oct(13) # 8
bin(3) # 2
int("0xF",16)
int("123",10) # 默认10进制
int("100000",2)

# array

a = np.array([1,2,3])

p = {
    "b": 3,
    "t":{
        "t1":1
    },
    "e": 1,
    "3":1
}

