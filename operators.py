Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthemaic
a=12
b=4
print(a+b)
16
print(a-b)
8
print(a*b)
48
]
print(a//b)
3
print(a/b)
3.0
print(a**b)
20736
print(a%b)
0

#assignment

a=6
b=2
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
8
a-=4
a
4
a*=2
a
8
a**=2
a
64
a/=2
a
32.0
a%=4
a
0.0
b+=a
b
2.0
b+=4
b
6.0
b-=2
b
4.0
b*=a
b
0.0
b**=2
b
0.0
b//=2
b
0.0
b/=2
b
0.0
b%=2
b
0.0

#comparision
a=8
b=4
a<b
False
aa>b
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    aa>b
NameError: name 'aa' is not defined. Did you mean: 'a'?
a>b
True
a<=b
False
a>=b
True
a!=b
True
a==b
False
a==b
False

#logical

a=10
b=40

#and
a<b and b>a
True
a<=b and b>=a
True
a!=b and b!=a
True

#or
a<b or b>a
True
a<=b or b>=a
True
a!=b or b!=a
True

#not
not True
False
not False
True


#identify

a=5
type
<class 'type'>
#is
type(a) is int
True
#is not
type(a) is not int
False
type(a) is not str
True
type(a) is not float
True
#is
a=12.1
type(a) is int
False
type(a) is float
True
type(a) is complex
False
type(a) is str
False
type(a) is bool
False

#is not
a=156.01
type(a) is not int
True
type(a) is not float
False
type(a) is not complex
True
type(a) is not str
True
type(a) is not bool
True

#membership

a=23456789012
10 in a
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    10 in a
TypeError: argument of type 'int' is not a container or iterable

a=2,3,4,5,6,7,8,10,9,13
11 in a
False
30 not in a
True

#bitwise
a=2
b=8
a&b
0
>>> bin(2)
'0b10'
>>> bin(8)
'0b1000'
>>> 
>>> a=2
>>> b=2
>>> a|b
2
>>> 
>>> a=2
SyntaxError: invalid syntax
>>> a=2
>>> ~a
-3
>>> 
>>> a=3
>>> b=2
>>> a^b
1
>>> 1
1
>>> a=5
>>> a<<2
20
>>> 
>>> a=2
>>> a>>3
0
>>> a=9
>>> a>>3
1
