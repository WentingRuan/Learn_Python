# list comprehension
 a = [3] * 3

In [2]: a
Out[2]: [3, 3, 3]

In [3]: a = [ [1,2,3] ] * 3

In [4]: a
Out[4]: [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

In [5]: a[0]
Out[5]: [1, 2, 3]

In [6]: a[0].append(4)

In [7]: a
Out[7]: [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

In [8]: a[1].append(5)

In [9]: a
Out[9]: [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

In [10]: b = []

In [11]: for i in xrange(3): b.append([1, 2, 3])

In [12]: b
Out[12]: [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

In [13]: b[0].append(4)

In [14]: b
Out[14]: [[1, 2, 3, 4], [1, 2, 3], [1, 2, 3]]

In [15]: [1,2,3]
Out[15]: [1, 2, 3]

In [16]: list(1,2,3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-86b0f2b7ea1f> in <module>()
----> 1 list(1,2,3)

TypeError: list() takes at most 1 argument (3 given)

In [17]: def f(a = [1,2,3]): a.append(4); print(a)

In [18]: f()
[1, 2, 3, 4]

In [19]: f()
[1, 2, 3, 4, 4]

In [20]: f()
[1, 2, 3, 4, 4, 4]

In [21]: a =
#generator comprehension

In [1]: a = [ (1) for i in xrange(3) ]

In [2]: a
Out[2]: [1, 1, 1]

In [3]: a = [ i for i in xrange(3) ]

In [4]: a
Out[4]: [0, 1, 2]

In [5]: a = [ i for i in xrange(10) if i % 2 == 0 ]

In [6]: a = [ i for i in xrange(10) if i % 2 == 0 ]

In [7]: def f(n): s = 1; for i in xrange(1, n+1): s *= i; return s
  File "<ipython-input-7-ee478d6fde2b>", line 1
    def f(n): s = 1; for i in xrange(1, n+1): s *= i; return s
                       ^
SyntaxError: invalid syntax


In [8]: def f(n): s = 1; for i in xrange(1, n+1): s *= i; return s
  File "<ipython-input-8-ee478d6fde2b>", line 1
    def f(n): s = 1; for i in xrange(1, n+1): s *= i; return s
                       ^
SyntaxError: invalid syntax


In [9]: reduce(lambda e, a: e*a, range(10), 1)
Out[9]: 0

In [10]: reduce(lambda e, a: e*a, range(1, 11), 1)
Out[10]: 3628800

In [11]: sum(3, lambda e, a: e*a)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-e526ce5cd6a3> in <module>()
----> 1 sum(3, lambda e, a: e*a)

TypeError: 'int' object is not iterable

In [12]: dir(sum)
Out[12]:
['__call__',
 '__class__',
 '__cmp__',
 '__delattr__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__le__',
 '__lt__',
 '__module__',
 '__name__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__self__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__']

In [13]: reduce(lambda e, a: e*a, range(1, 11), 1)
Out[13]: 3628800

In [14]: def f(n): return reduce(lambda e, a: e*a, range(1, n+1), 1)

In [15]: a = [ f(i) for i in xrange(0, 10) if i % 2 == 0 ]

In [16]: a
Out[16]: [1, 2, 24, 720, 40320]

In [17]: map(f, xrange(0, 10))
Out[17]: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

In [18]: map(f, xrange(0, 10, 2))
Out[18]: [1, 2, 24, 720, 40320]

In [19]: map(f, filter(lamda e: e%2==0, xrange(0, 10)))
  File "<ipython-input-19-f4204bbee1e9>", line 1
    map(f, filter(lamda e: e%2==0, xrange(0, 10)))
                        ^
SyntaxError: invalid syntax


In [20]: map(f, filter(lamda e: e%2==0, xrange(0, 10)))
  File "<ipython-input-20-f4204bbee1e9>", line 1
    map(f, filter(lamda e: e%2==0, xrange(0, 10)))
                        ^
SyntaxError: invalid syntax


In [21]: filter(lambda e: e%2 == 0, xrange(10))
Out[21]: [0, 2, 4, 6, 8]

In [22]: map(f, filter(lamda e: e%2==0, xrange(0, 10)))
  File "<ipython-input-22-f4204bbee1e9>", line 1
    map(f, filter(lamda e: e%2==0, xrange(0, 10)))
                        ^
SyntaxError: invalid syntax


In [23]: map(f, filter(lambda e: e%2==0, xrange(0, 10) ) )
Out[23]: [1, 2, 24, 720, 40320]

In [24]: [ f(i) for i in xrange(0, 10) if i % 2 == 0 ]
Out[24]: [1, 2, 24, 720, 40320]

In [25]: xrange(1000000)
Out[25]: xrange(1000000)

In [26]: iter(xrange(1000000))
Out[26]: <rangeiterator at 0x63583f0>

In [27]: iter(xrange(1000000))
Out[27]: <rangeiterator at 0x63587b0>

In [28]: a = iter(xrange(1000000))

In [29]: next(a)
Out[29]: 0

In [30]: next(a)
Out[30]: 1

In [31]: next(a)
Out[31]: 2

In [32]: a = iter(range(1000))

In [33]: next(a)
Out[33]: 0

In [34]: next(a)
Out[34]: 1

In [35]:

#lazy reaction

>>> f = lambda n: reduce(lambda e, a: e* a, xrange(1, n+1), 1)
>>> f(3)
6
>>> t = ( f(i) for i in xrange(10000) )
>>> t[0]

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t[0]
TypeError: 'generator' object has no attribute '__getitem__'
>>> a = iter(a)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = iter(a)
NameError: name 'a' is not defined
>>> a = iter(t)
>>> next(a)
1
>>> next(a)
1
>>> next(a)
2
>>> next(a)
6
>>> next(a)
24
>>> t = ( f(i) for i in xrange(10000) )
