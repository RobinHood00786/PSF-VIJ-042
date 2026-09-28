Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=24
type(a)
<class 'int'>
x="antony"
type(x)
<class 'str'>
a=23.9
type(a)
<class 'float'>
d=2+6j
type(d)
<class 'complex'>
a=True
type(a)
<class 'bool'>
B=False
type(B)
<class 'bool'>
f=7i
SyntaxError: invalid decimal literal
f=4j
type(f)
<class 'complex'>
l=j
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l=j
NameError: name 'j' is not defined
m="j
SyntaxError: unterminated string literal (detected at line 1)
m="j"
type(m)
<class 'str'>
#datatype conversions
#int
int(8)
8
int(00.7)
0
int("gipps")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int("gipps")
ValueError: invalid literal for int() with base 10: 'gipps'
int(2+65j)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(2+65j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(3)
3.0
float(007.000)
7.0
float(23+45j)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(23+45j)
TypeError: float() argument must be a string or a real number, not 'complex'
float("peace")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float("peace")
ValueError: could not convert string to float: 'peace'
float(True)
1.0
float(False)
0.0
#string
str(10)
'10'
str(7.0)
'7.0'
str("GHOST☠️☠️")
'GHOST☠️☠️'
str(2+45j)
'(2+45j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(2)
(2+0j)
>>> complex(124.00)
(124+0j)
>>> complex(12+32j)
(12+32j)
>>> complex("GHOST")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex("GHOST")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(2)
True
>>> bool(32.00)
True
>>> bool(12+45j)
True
>>> bool("GHOST are you here...")
True
>>> bool(True)
True
>>> bool(False)
False
