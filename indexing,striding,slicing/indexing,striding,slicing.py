Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="he is dark knight"
a=(8)+a(10)+a(12)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=(8)+a(10)+a(12)
TypeError: 'str' object is not callable
a(8)+a(10)+a(11)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a(8)+a(10)+a(11)
TypeError: 'str' object is not callable
a[8]+a[10]+a[11]
'r k'
x= "vizag is a city of destiny"
x[-9]+x[-8]+x[-10]+x[-11]
'f o '
x[-15]+x[-14]+x[-13]+x[-12]
'city'
x[-27]+x[-26]+x[-25]+x[-24]+x[-23]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x[-27]+x[-26]+x[-25]+x[-24]+x[-23]
IndexError: string index out of range
a="simple is better than complex"
a[-33]+a[-32]+a[-31]+a[-30]+a[-29]+a[-28]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[-33]+a[-32]+a[-31]+a[-30]+a[-29]+a[-28]
IndexError: string index out of range
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'


#slicing
'
a="DARK KNIGHT"
a[0:1:2:3:4:5]
SyntaxError: invalid syntax
a[0:1:2:3:4]
SyntaxError: invalid syntax
a[0:1:2:3]
SyntaxError: invalid syntax
a[0:1]
'D'
a[0:1:2]
'D'
a="DARKKNIGHT"
a[0:1:2:3]
SyntaxError: invalid syntax
a[1:2]
'A'
a="work hard until you successed"
a[12:13]
't'
a[12:15]
'til'
a[0:5]
'work '
a[0:7]
'work ha'
a="time is very precious"
a[0:9]
'time is v'

a="I love python"
a[-1:-5]
''
a[-6:-1]
'pytho'
a[-6:0]
''
a[-6:1]
''
a[-6:]
'python'
a[-11:]
'love python'
a[-11:-7]
'love'

a="today is weekend"
a[-9:]
's weekend'
a[-10:]
'is weekend'
a="data science"
a[::1]
'data science'
>>> a[2::1]
'ta science'
>>> a[::2]
'dt cec'
>>> a="machine learning"
>>> a[::4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[::4]
'miln'
>>> a[::6}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[::6]
'men'
>>> a[::2]
'mcielann'
>>> a[1::2]
'ahn erig'
>>> a[5:]
'ne learning'
>>> a="cloud computing"
>>> a[2:14]
'oud computin'
>>> a[2:14:4]
'ocu'
>>> a[5:13:3]
' mt'
>>> a[4:12:2]
'dcmu'
>>> 
>>> 
>>> #negative striding
>>> 
