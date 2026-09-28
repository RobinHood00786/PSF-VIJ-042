Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
b="black pearl"
len(b)
11
c=""
len(c)
0
d=" "
len(d)
1

#count
a="captain can u hear cpatain on your left"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("captain")
1
a.count("c")
3
a.count("  ")
0
a.count(" ")
7

#find a string

a="DareDevil"
a.find("d")
-1
a.find("D")
0
a[4]
'D'

#escape sequences
#\n -> newline
#\t -> tab space
a="name\tmobilenumber\ncollege\tbranch\tmailid"
print(a)
name	mobilenumber
college	branch	mailid
b="jack\t9874786887\ncollege of priates\tCaptian\tCaptian@mail.com
SyntaxError: unterminated string literal (detected at line 1)
b="jack\t98842372247\ncollege of pirates\tCaptain\tCaptian@mail.com"
print(b)
jack	98842372247
college of pirates	Captain	Captian@mail.com
x="name\nplace\nDOB\t"
print(x)
name
place
DOB	

#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'

a.replace("wait","die")
'die until you succeed'


#upper()
a="jack sparrow"
a.upper()
'JACK SPARROW'
a.upper(J)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.upper(J)
NameError: name 'J' is not defined
a.upper("j")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.upper("j")
TypeError: str.upper() takes no arguments (1 given)
a.upper()
'JACK SPARROW'
a.upper('j')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.upper('j')
TypeError: str.upper() takes no arguments (1 given)
a[0].upper()
'J'

#lower()
a="JACK"
a.lower()
'jack'

#capitalize()
a="blackpearl"
a.capitalized()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.capitalized()
AttributeError: 'str' object has no attribute 'capitalized'. Did you mean: 'capitalize'?
a.title()
'Blackpearl'
a.capitalize()
'Blackpearl'


#conditions

a=messie
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a=messie
NameError: name 'messie' is not defined
a="messie"
a.isupper()
False
a.isupper(1)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.isupper(1)
TypeError: str.isupper() takes no arguments (1 given)
a.lower()
'messie'
a.islower()
True

a.isalpha()
True

b="123434"
b.isupper()
False
b.isanum()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    b.isanum()
AttributeError: 'str' object has no attribute 'isanum'. Did you mean: 'isalnum'?
b.isadigit()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    b.isadigit()
AttributeError: 'str' object has no attribute 'isadigit'. Did you mean: 'isdigit'?
b.isdigit()
True

f="peter@2000"
f.isalnum()
False
f.isalalpha
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    f.isalalpha
AttributeError: 'str' object has no attribute 'isalalpha'. Did you mean: 'isalpha'?
f.isalalpha()
Traceback (most recent call last):]
  File "<pyshell#83>", line 1, in <module>
    f.isalalpha()
AttributeError: 'str' object has no attribute 'isalalpha'. Did you mean: 'isalpha'?
f.isaldigit
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    f.isaldigit
AttributeError: 'str' object has no attribute 'isaldigit'. Did you mean: 'isdigit'?



#strip()
#lstrip -> leftstrip
#rstrip -> Rightstrip

a="   strange    "
a.strip()
'strange'
a.lstrip()
'strange    '

a.rstrip()
'   strange'
True
True

#concatination
a="dare"
d="devil"
print(a+b)
dare123434
print(a+b)
dare123434
print(a+d)
daredevil

fname="sparrow"
lname="k"
print(fname+lname)
sparrowk
print(fname+ "" +lname)
sparrowk
print(fname+" "+lname)
sparrow k

#split

a="teamcaptain teamtony fantastic4 xmen"
a.split()
['teamcaptain', 'teamtony', 'fantastic4', 'xmen']

s="greatest battels are  with closet people"
s.split()
['greatest', 'battels', 'are', 'with', 'closet', 'people']

#join

a="ned","wong","alprade"
"".join(a)
'nedwongalprade'
" ".join(a)
'ned wong alprade'
"|".join(a)
'ned|wong|alprade'
"1".join(a)
'ned1wong1alprade'

s="boogyman"
"1".join(s)
'b1o1o1g1y1m1a1n'

#formating

a=31
b=20
print(a+b ,a-b)
51 11
print("the result is:-" , a+b)
the result is:- 51


#formate mehod
a="john"
b="gipps"
print("Hello Mr{} {} ".formate(a,b))
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    print("Hello Mr{} {} ".formate(a,b))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
print("Hello Mr{} {} ".format(a,b))
Hello Mrjohn gipps 

print("hello {} and {}".formate(a,b),title())
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    print("hello {} and {}".formate(a,b),title())
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
print("hello {} and {}".formate(a,b).title())
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    print("hello {} and {}".formate(a,b).title())
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
print("hello {} and {}".format(a,b),title())
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    print("hello {} and {}".format(a,b),title())
NameError: name 'title' is not defined. Did you mean: 'tuple'?
print("hello {} {}".formate(a,b),title())
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    print("hello {} {}".formate(a,b),title())
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> KeyboardInterrupt
>>> print("hello {} {}".formate(a,b).title())
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    print("hello {} {}".formate(a,b).title())
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> print("hello {}  {}".format(a,b).title())
Hello John  Gipps
>>> 
>>> #fstring
>>> a="pepper"
>>> b="pods"
>>> print(f"hello {a}{b}")
hello pepperpods
>>> print(f"hello {a} {b}")
hello pepper pods
>>> print(f"hello {a} hello{b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"hello {a} hello{b}")
...       
hello pepper hellopods
>>> 
>>> a=2
...       
>>> b=10
...       
>>> print(f"{a}*{b}")
...       
2*10
>>> print(f"{a*b}")
...       
20
