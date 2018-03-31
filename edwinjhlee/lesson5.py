# list comprehension
a = [3] * 3
a

a = [ [1,2,3] ] * 3 #把[1,2,3]这个软连接复制了三遍，但都指向一个内存
a
a[0] # 对a[0]操作也是对a操作
a[0].append(4)
a
a[1].append(5)
a
#----------------------

# list generator 
b = []
for i in xrange(3): b.append([1, 2, 3])

b
b[0].append(4) #实打实地对b[0]操作
b

def f(a = [1,2,3]): a.append(4); print(a)

f()
f()
f() #a默认为一个list[1,2,3]，函数结束时自动返回一个a作为全局变量，这个a会在程序再启动时被重新传进去

## 类似例子
def f(a,L=[]):
    L.append(a)
    print(L)

f(1)
f(2)
f(3)

## 等效上面那个例子
lst = []
def f(a,L=lst):
    L.append(a)
    return(L)

f(1)
f(2)
f(3)
#默认值是指向一个列表对象，程序开始的时候这个列表对象是空。而不是每次调用函数的时候新建一个空列表。

# generator comprehension
## iterate an generator
c = xrange(0,100)
c ## c是一个generator，只有要用时才生成
c = iter(c)
next(c)
next(c)
next(c)

## turn a generator into a list

a = [ (1) for i in xrange(3) ]
a
b = list((1) for i in xrange(3))
b ## a == b

d = [ i for i in xrange(3) ]
d

d = [ i for i in xrange(10) if i % 2 == 0 ]
d

d = [ i for i in xrange(10) if i % 2 == 0 ]
d


def f(n): 
  s = 1
  for i in xrange(1, n+1):
     s *= i
     
  return(s)

f(1)
f(2)
f(3)

# reduce会对参数序列中元素进行累积。
# reduce(function, iterable[, initializer])
  # iterable[, initializer] == [1,2,3]
  #用传给reduce中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# INIT[1,2,3,4,5]
# reduce(f,INIT[1,2,3,4,5]) == f(f(f(f(f(1,1),2),3),4),5)

reduce(lambda e, a: e*a, range(3), 1) # a *= 0*a

reduce(lambda e, a: e*a, range(1,3),1) # e=1,a=1*1; e=2,a=1*2
reduce(lambda e, a: e*a, range(1,3),2) # e=1,a=1*2; e=2,a=2*2
reduce(lambda e, a: e*a, range(1,3),3) # e=1,a=1*3; e=2,a=3*2


reduce(lambda e, a: e*a, range(1, 5), 1)
reduce(lambda e, a: e*a, iter(xrange(1, 5)), 1) #range(1,3)==[1,2]

reduce(lambda e, a: e*a, range(1, 11), 1)


def f(n): return reduce(lambda e, a: e*a, range(1, n+1), 1)

f(1)
f(2)
f(4)
f(6)
f(8)

a = [ f(i) for i in xrange(0, 10) if i % 2 == 0 ]
a #f(0),f(2),f(4),f(6),f(8)

#map(function,iterable,...) 会根据提供的函数对指定序列做映射。
  #第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

map(f, xrange(0, 10))
map(f, xrange(0, 10, 2))

#filter(function,iterable) 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
  #filter接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
map(f, filter(lambda e: e%2==0, xrange(0, 10) ) )

[ f(i) for i in xrange(0, 10) if i % 2 == 0 ]

### 复习generator

xrange(1000000) #python3里range = xrange
iter(xrange(1000000)) ￥rangeiterator object

a = iter(xrange(1000000))
next(a)
next(a)
next(a)

a = iter(range(1000))
next(a)
next(a)

#lazy reaction

f = lambda n: reduce(lambda e, a: e* a, xrange(1, n+1), 1)
f(3)

t = ( f(i) for i in xrange(10000) ) #t是一个tupple generator
t[0] #

a = iter(t)
next(a)
next(a)

t = ( f(i) for i in xrange(10000) )
t = iter(t)
next(t)
next(t)


