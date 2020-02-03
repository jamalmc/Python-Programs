Program 1:
"""Write a program, which will find all such numbers between 1000 and 3000 (both included) such that 
each digit of the number is an even number.The numbers obtained should be printed in a comma-separated 
sequence on a single line."""  

li=[]
for i in range(1000,3001):
    t=i
    flag=0
    while(t>0):
        
        r=t%10
        if r%2!=0:
            flag=1
            break
        else:   
            t=t//10
    if flag==0:
        li.append(i)
print(li)

Program 2:
"""Write a program that accepts a sentence and calculate the number of letters and digits.Suppose the 
following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""

l=0
d=0
str=input("Enter your string :")
for i in str:
    if i.isalpha():
        l+=1
    if i.isdigit():
        d+=1
print("Entered string is:",str)
print("LETTERS :",l)
print("DIGITS",d)


Program 3:
"""Write a program that accepts a sentence and calculate the number of upper case letters and 
lower case letters.Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""

u=0
l=0
str=input("Enter your string :")
for i in str:
    if i.isupper():
        u+=1
    if i.islower():
        l+=1
print("Entered string is:",str)
print("UPPER CASE :",u)
print("LOWER CASE",l)

Program 4:
"""Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106"""

a=int(input("Enter your number :"))
sum=0
t=a
for i in range(4):
    sum=sum+t
    t=t*10+a
print(sum)

Program 5:
"""Use a list comprehension to square each odd number in a list. The list is input by a sequence of 
comma-separated numbers.Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81"""

Solution 1:     
list1=[]
li=list(map(int,input("Enter your numbers :").split(',')))
for i in li:
    if i%2!=0:
        b=i**2
        list1.append(b)
list1=str(list1)[1:-1]
print(list1)

Solution 2: 
li=[]
list1=[]
n=int(input("Enter your limit:"))
print("Enter your numbers:")
for i in range(n):    
   a=int(input())
   li.append(a)
for i in li:
    if i%2!=0:
        b=i**2
        list1.append(b)
print(li)
print(list1)

Program 6:
"""Write a program that computes the net amount of a bank account based a transaction log from console 
input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""

Solution 1: 
y=1
sum=0
while(y):
    a=list(map(str,input("Enter your transaction :").split()))
    b=int(a[1])
    if a[0]=='D':
        sum=sum+b
    elif a[0]=='W':
            if sum<=0 or b>sum:
                print("Insufficient balance")
            else:
                sum=sum-b
    else:
        print("Invalid entry")
    c=input("Enter Y to continue or N to exit :")
    if c=='Y':
        y=1
    else:
        y=0
        print("SUM IS :",sum)

Solution 2: 
sum=0
y=1
while(y):
    a=input("Enter D for deposit and W for withdraw :")
    b=int(input("Enter your amount :"))
    if a=='D':
        sum=sum+b
    elif a=='W':
        if sum<=0 or b>sum:
            print("Insufficient balance")
        else:
            sum=sum-b
    else:
        print("Invalid entry")
    c=input("Enter Y to continue or N to exit :")
    if c=='Y':
        y=1
    else:
        y=0
        print("SUM IS :",sum)

Program 7:
"""A website requires the users to input username and password to register. Write a program to check 
the validity of password input by users.Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to 
the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example:
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""

u=l=d=c=0
Username=input("Enter your username :")
Password=list(map(str,input("Enter your password :").split(',')))
Password=Password[0]

if len(Password)<6 or len(Password)>12:
    print("Password must contain between 6 to 12 letters")
else:
    for i in Password:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        elif i.isdigit():
            d+=1
        else:
            c+=1
    if u==0 or l==0 or d==0 or c==0:
        print("Wrong password")
    else:
        print("Username :",Username)
        print("Password :",Password)

Program 8:    
"""You are required to write a program to sort the (name, age, height) tuples by ascending order where 
name is string,age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), 
('Tom', '19', '80')]"""

li=[]
y=1
while(y):
    a=tuple(map(str,input("Enter the details :").split(',')))
    li.append(a)
    c=input("Enter Y to continue or N to exit :")
    if c=='Y':
        y=1
    else:
        y=0
        li.sort()
        print(li)

Program 9:
"""Define a class with a generator which can iterate the numbers, which are divisible by 7, 
between a given range 0 and n.
Hints:
Consider use yield"""

class Abc:
    def __init__(self):
        self.a=a
    def Gen(self):
        i=1
        while(i<=a):
            if i%7==0:
                yield i
            i+=1

n=int(input("Enter the number :"))
obj=Gen(Abc())
for i in obj:
    print(i)          

Program 10:                    
"""A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN,
LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps. Please write a program to compute the distance from current
position after a sequence of movement and original point. If the distance is a float, 
then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2"""

import math
x=0
y=0
n=1
li=[]
while(n):
    a=tuple(map(str,input("Enter the movement :").split()))
    b=int(a[1])
    li.append(a)
    if a[0]=='UP' or a[0]=='up':
        x+=b
    elif a[0]=='down' or a[0]=='DOWN':
        if x<=0:
            x+=b
        else:
            x-=b
    elif a[0]=='RIGHT' or a[0]=='right':
        y+=b
    elif a[0]=='left' or a[0]=='LEFT':
        if y<=0:
            y-=b
        else:
            y+=b
    else:
        print("Invalid input")
    c=input("Enter y to continue or n to exit :")
    if c=='y' or c=='Y':
        n=1
    else:
        n=0
        ab=math.sqrt(x**2+y**2)
        print(int(ab))

Program 11:
"""Write a program to compute the frequency of the words from the input. The output should output 
after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1"""

count=1
str1=input("Enter your sentence :").split()
str2=[]

for i in str1:
    if i not in str2:
        str2.append(i)
        
for i in range(len(str2)):
    count=str1.count(str2[i])
    print(str2[i],":",count)


Program 12:
"""Write a method which can calculate square value of number...
Python has many built-in functions, and if you do not know how to use it, you can read document 
online or find some books.But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function""""
    
    
    
Program 13:   
"""Define a class, which have a class parameter and have a same instance parameter."""

class 

Program 14:
"""Define a function that can convert a integer into a string and print it in console."""

def conv(n):
    print("Type of {} Before converting is :".format(n),type(n))
    n=str(n)
    print("Type of {} after converting is :".format(n),type(n))
conv(10)

Program 15:
"""Define a function that can receive two integral numbers in string form and compute their sum and 
then print it in console."""

def sum(a,b):
    a,b=int(a),int(b)
    sum=a+b
    print("The sum is :",sum)
sum('5','4')


Program 16:
"""Define a function that can accept two strings as input and concatenate them and then print it in 
console."""

def conc(a,b):
    c=a+b
    print("Concatenated string is :",c)

str1=input("Enter the first string :")
str2=input("Enter the second string :")

conc(str1,str2)


Program 17:
"""Define a function that can accept two strings as input and print the string with maximum length in 
console. If two strings have the same length, then the function should print all strings line by line."""

def maxstr(a,b):
    if len(a)>len(b):
        print(a)
    elif len(a)<len(b):
        print(b)
    else:
        print(a,'\n',b)
str1=input("Enter the first string :")
str2=input("Enter the second string :")

maxstr(str1,str2)


Program 18:
"""Define a function that can accept an integer number as input and print the "It is an even number" 
if the number is even, otherwise print "It is an odd number"."""

def odd_even(n):
    if n%2==0:
        print("It is an even number")
    else:
        print("It is an odd number")

num=int(input("Enter your number :"))

odd_even(num)


Program 19:
"""Define a function which can print a dictionary where the keys are numbers between 1 and 3 
(both included) and the values are square of keys."""

def square(n):
    for i in range(1,n+1):
        mydict[i]=i**2
    print(mydict)  
    
num=int(input("Enter your number :"))
mydict={}

square(num)


Program 20:
"""Define a function which can generate a dictionary where the keys are numbers between 1 and 20 
(both included) and the values are square of keys. The function should just print the values only."""

def square(n):
    for i in range(1,n+1):
        mydict[i]=i**2
    for x in mydict.values():
        print(x)
    
num=int(input("Enter your number :"))
mydict={}

square(num)


Program 21:
"""Define a function which can generate a dictionary where the keys are numbers between 1 and 20 
(both included) and the values are square of keys. The function should just print the keys only."""

def square(n):
    for i in range(1,n+1):
        mydict[i]=i**2
    for x in mydict.keys():
        print(x)
    
num=int(input("Enter your number :"))
mydict={}

square(num)



Program 22:
"""Define a function which can generate and print a list where the values are square of numbers 
between 1 and 20 (both included)."""

def squarelist(n):
    for i in range(1,n+1):
        li.append(i**2)
    print(li)
    
li=[]   
num=int(input("Enter your number :"))

squarelist(num)


Program 23:
"""Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print the first 5 elements in the list."""

def squarelist(n):
    for i in range(1,n+1):
        li.append(i**2)
    print(li[0:5])
        
li=[]   
num=int(input("Enter your number :"))

squarelist(num)


Program 24:
"""Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print the last 5 elements in the list."""

def squarelist(n):
    for i in range(1,n+1):
        li.append(i**2)
    print(li[-5:])
        
li=[]   
num=int(input("Enter your number :"))

squarelist(num)


Program 25:
"""Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print all values except the first 5 elements in the list."""

def squarelist(n):
    for i in range(1,n+1):
        li.append(i**2)
    print(li[5:])
        
li=[]   
num=int(input("Enter your number :"))

squarelist(num)


Program 26:
"""Define a function which can generate and print a tuple where the value are square of numbers 
between 1 and 20 (both included)."""

def squaretuple(n):
    for i in range(1,n+1):
        li.append(i**2)
    print(tuple(li))
        
li=[]
num=int(input("Enter your number :"))

squaretuple(num)


Program 27:
"""With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one 
line and the last half values in one line."""

tuple=(1,2,3,4,5,6,7,8,9,10)
li=list(tuple)
l1=[]
l2=[]
n=len(li)
for i in range(n):
    if i<n/2:
        l1.append(li[i])
    else:
        l2.append(li[i]) 
print(l1)    
print(l2) 


Program 28:
"""Write a program to generate and print another tuple whose values are even numbers in the given 
tuple (1,2,3,4,5,6,7,8,9,10)."""

tu=(1,2,3,4,5,6,7,8,9,10)
li=[]

for i in tu:
    if i%2==0:
        li.append(i)

print(tuple(li))

Program 29:
"""Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" 
or "Yes", otherwise print "No"."""

str=input("Enter your string :")
if str=="yes" or str=="YES" or str=="Yes":
    print("Yes")
else:
    print("No")


Program 30:
"""Write a program which can filter even numbers in a list by using filter function. 
The list is: [1,2,3,4,5,6,7,8,9,10]."""

li=[1,2,3,4,5,6,7,8,9,10]

l1=list(filter(lambda x:x%2==0,li))

print(l1)


Program 31:
"""Write a program which can map() to make a list whose elements are square of elements 
in [1,2,3,4,5,6,7,8,9,10]."""

li=[1,2,3,4,5,6,7,8,9,10]

l1=list(map(lambda x:x**2,li))

print(l1)


Program 32:
"""Write a program which can map() and filter() to make a list whose elements are square of 
even number in [1,2,3,4,5,6,7,8,9,10]."""

li=[1,2,3,4,5,6,7,8,9,10]

l1=list(map(lambda x:x**2,li))

l1=list(filter(lambda x:x%2==0,l1))

print(l1)


Program 32:
"""Write a program which can filter() to make a list whose elements are even number between 1 and 20 
(both included)."""

num=int(input("Enter your limit :"))
li=[]

for i in range(1,num+1):
    li.append(i)    

l1=list(filter(lambda x:x%2==0,li))

print(l1)


Program 33:
"""Write a program which can map() to make a list whose elements are square of numbers between 
1 and 20 (both included)."""

num=int(input("Enter your limit :"))
li=[]

for i in range(1,num+1):
    li.append(i)    

l1=list(map(lambda x:x**2,li))

print(l1)


Program 34:
"""Define a class named American which has a static method called printNationality."""

class American:
    def __init(self):
        pass
    def PrintNationality(x):
        return x
    
American.PrintNationality("America")

Program 35:
"""Define a class named American and its subclass NewYorker."""

class American:
    def __init__(self):
        pass
    def PrintNationality(x):
        return x

class Newyork(American):
    def __init__(self):
        pass

Newyork.PrintNationality("America")


Program 36:
"""Define a class named Circle which can be constructed by a radius. The Circle class has a method 
which can compute the area."""

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 2*self.radius*3.14
    
obj=Circle(8)
obj.area()


Program 37:
"""Define a class named Rectangle which can be constructed by a length and width. The Rectangle class 
has a method which can compute the area."""

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    
obj=Rectangle(5,6)

obj.area()


Program 38:
"""Define a class named Shape and its subclass Square. The Square class has an init function which 
takes a length as argument.Both classes have a area function which can print the area of the shape 
where Shape's area is 0 by default."Please raise a RuntimeError exception.
Hints:
Use raise() to raise an exception."""

class Shape:
    def __init__(self,length):
        self.length=length
    def area(self):
        raise ValueError('Exception occured')
        


class Square(Shape):
    def __init__(self):
        pass
    def area(self):
        return 0

obj=Shape(6)
obj.area()
obj1=Square(6)
obj1.area() 
    

Program 39:
"""Write a function to compute 5/0 and use try/except to catch the exceptions."""

def divide(x,y):
    try:
        result=x//y
        print("Your answer is :",result)
    except:
        print("sorry! you are dividing by zero")

divide(5,0)



Program 40:
"""Define a custom exception class which takes a string message as attribute."""

class custom(Exception):
    def__init__(self,string):
        self.string=string
    

custom("error")


Program 41:
"""Assuming that we have some email addresses in the ""username@companyname.com"" format, 
please write program to print the company name of a given email address. Both user names and 
company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google"""

mail=list(map(str,input("Enter the mail :").split("@")))
li=mail[1].split(".")
print("Company name is :",li[0])


Program 42:
"""Write a program which accepts a sequence of words separated by whitespace as input to print the 
words composed of digits only."""


str=list(map(str,input("Enter your string :").split()))

for i in str:
    if i.isdigit():
        print(i)



Program 43:
"""Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
Write a special comment to indicate a Python source code file is in unicode."""

a='\x3cdiv\x3e'
print(a)

u=a.encode("utf-8")

unicode_string=u'\x3cdiv\x3e'

Program 44:
"""Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55"""

n=int(input("Enter your number :"))
sum=0

for i in range(1,n+1):
    sum=sum+i/(i+1)
    
print("sum is :",round(sum,2))


Program 45:
"""Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=0
with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
500"""

n=int(input("Enter your number :"))

def fib(a):
    if a==0:
        return 0
    elif a>0:
        return fib(a-1)+100

fib(n)


Program 46:
"""The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
13"""

n=int(input("Enter your number :"))

def fib(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    elif a>0:
        return fib(a-1)+fib(a-2)
    
fib(n)


Program 47:
"""The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated 
form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13"""

n=int(input("Enter your number :"))
li=[]

for i in range(n+1):
    if i==0 or i==1:
        li.append(i)
    
    elif i>1:
        c=li[i-1]+li[i-2]
        li.append(c)
    
print(str(li)[1:-1])


Program 48:
"""Please write a program using generator to print the even numbers between 0 and n in comma 
separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10"""

1)
n=int(input("Enter your number :"))

def even(a,b):
    
    while a<=b:
        if a%2==0:
            yield a
        a=a+1

even_numbers=even(0,n)       
for i in even_numbers:
    print(i)
    
    
2)   
n=int(input("Enter your number :"))

def even(b):
    a=0
    
    while a<=b:
        if a%2==0:
            yield a
        a=a+1

even_numbers=even(n)       
for i in even_numbers:
    print(i)
    

Program 49:
"""Please write a program using generator to print the numbers which can be divisible by 5 and 7 
between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70"""

n=int(input("Enter your number :"))

def even(b):
    a=0
    
    while a<=b:
        if a%5==0 and a%7==0:
            yield a
        a=a+1

even_numbers=even(n)       
for i in even_numbers:
    print(i)


Program 50:
"""Please write assert statements to verify that every number in the list [2,4,6,8] is even."""

li=[2,4,6,8]

for i in li:
    assert i%2==0,"list is not fully even"
    
print("List is fully even")



Program 51:
"""Please write a program which accepts basic mathematic expression from console and print the 
evaluation result.
Example:
If the following string is given as input to the program:
35+3
Then, the output of the program should be:
38"""

from functools import reduce
str=input("Enter your expression :")
if '+' in str:
    li=str.split("+")   
    for i in range(len(li)):
        li[i]=int(li[i])
    print(sum(li))
    
elif '-' in str:
    li=str.split("-")
    for i in range(len(li)):
        li[i]=int(li[i])
    lis=print(reduce(lambda x,y:x-y,li))
    
elif '*' in str:
    li=str.split("*")
    for i in range(len(li)):
        li[i]=int(li[i])
    print(reduce(lambda x,y:x*y,li))
    
elif '/' in str:
    li=str.split("/")
    for i in range(len(li)):
        li[i]=int(li[i])
    print(reduce(lambda x,y:x/y,li))
    
    
Program 52:
"""Please write a binary search function which searches an item in a sorted list. The function 
should return the index of element to be searched in the list.
Hints:
Use if/elif to deal with conditions."""

def search(x):
    for i in li:
        if i==x:
            print(li.index(i))
        else:
            continue
        

li=[9,8,7,5,6,1,4,2]
li.sort()
k=int(input("Enter the key wants to be searched :"))   
search(k)


Program 53:
"""Print a unicode string "hello world"."""


str=u"Hello world!"
print(str)



Program 54:
"""Please generate a random float where the value is between 10 and 100 using Python math module."""

import random
print(random.uniform(10,100))


Program 55:
"""Please generate a random float where the value is between 5 and 95 using Python math module."""
import random
print(random.uniform(5,95))


Program 56:
"""Please write a program to output a random even number between 0 and 10 inclusive using random 
module and list comprehension."""

import random

li=[x for x in range(0,10) if x%2==0 ]

list=random.choice(li)
print(list)


Program 57:
"""Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 100 
inclusive using random module and list comprehension."""

import random

li=[x for x in range(0,100) if x%5==0 and x%7==0]

list=random.choice(li)
print(list)

Program 58:
"""Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive."""

import random

li=[x for x in range(100,200)]

list=random.choices(li,k=5)
print(list)


Program 59:
"""Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive"""


import random

li=[x for x in range(100,200) if x%2==0]

list=random.choices(li,k=5)
print(list)


Program 60:
"""Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7,
between 1 and 1000 inclusive."""

import random

li=[x for x in range(1,1000) if x%5==0 and x%7==0]

list=random.choices(li,k=5)
print(list)

Program 61:
"""Please write a program to randomly print a integer number between 7 and 15 inclusive."""

import random

list=random.randint(7,15)
print(list)


Program 62:
"""Please write a program to compress and decompress the string ""hello world!hello world!hello world!
hello world!""."""

import zlib
a="Hello world"

comp=zlib.compress(a.encode())
print(comp)

decomp=zlib.decompress(comp)
print(decomp)


Program 63:
"""Please write a program to print the running time of execution of "1+1" for 100 times."""

import time
def prin(n):
    strat_time=time.time()
    for i in range(100):
    
        b=1+1


    end_time=time.time()        
    return end_time-start_time

print(prin(100))

Program 64:
"""Please write a program to shuffle and print the list [3,6,7,8]."""

from random import shuffle

li=[3,6,7,8]

shuffle(li)

print(li)


Program 65:
"""Please write a program to generate all sentences where subject is in [""I"", ""You""] and 
verb is in [""Play"", ""Love""] and the object is in [""Hockey"",""Football""].
Hints:
Use list[index] notation to get a element from a list."""

subject=["I","You"]
verb=["Play","Love"]
object=["Hockey","Football"]


for i in subject:
    for j in verb:
        for k in object:
            print(i,end=" ")
            print(j,end=" ")
            print(k)
        print()


Program 66:
"""Please write a pgm to print the list after removing delete even numbers in [5,6,77,45,22,12,24]"""

li=[5,6,77,45,22,12,24]

for i in li:
    if i % 2 == 0:
       li.remove(i)
    
print(li)


Program 67:
"""By using list comprehension, please write a program to print the list after removing numbers 
which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
Hints:
Use list comprehension to delete a bunch of element from a list."""

li=[12,24,35,70,88,120,155]

div=[x for x in li if x%5!=0 or x%7!=0]

print(div)


Program 68:
"""By using list comprehension, please write a program to print the list after removing the 0th, 
2nd,4th,6th numbers in [12,24,35,70,88,120,155].
Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple."""

li=[12,24,35,70,88,120,155]

lis=enumerate(x for x in li,2)

print(list(lis))


Program 69:
"""By using list comprehension,please write a pgm generate a 3*5*8 3D array whose each element is 0"""


def Threed(a,b,c):
    li=[[['0' for i in range(a)] for j in range(b)] for k in range(c)]
    print(li)

Threed(3,5,8)


Program 70:
"""By using list comprehension, please write a program to print the list after removing the 0th,4th,
5th numbers in [12,24,35,70,88,120,155].
Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple."""

li=[12,24,35,70,88,120,155]

list=[x for x in li if enumerate(li)!=0]

lis=[x for x in li if li.index(x)!=0]
lis=[x for x in li if li.index(x)!=4]
lis=[x for x in li if li.index(x)!=5]

Program 71:
"""With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list 
whose elements are intersection of the above given lists."""

list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
list=[]

for i in list1:
    if i in list2:
        list.append(i)
        
print(list)


Program 72:
"""With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after 
removing all duplicate values with original order reserved."""

li=[12,24,35,24,88,120,155,88,120,155]
lis=[]

for i in li:
    if i not in lis:
        lis.append(i)

print(lis)


Program 73:
"""Define a class Person and its two child classes: Male and Female. All classes have a method 
"getGender" which can print "Male" for Male class and "Female" for Female class."""

class Person:
    def __init__(self):
        pass
    def getGender(self):
        pass
        
class Male(Person):
    def getGender(self):
        print("Male")
class Female(Person):
    def getGender(self):
        print("Female")

obj1=Male()
obj2=Female()

obj1.getGender()
obj2.getGender()

Program 74:
"""Please write a pgm which count&print the numbers of each character in a string input by console."""

str=input("Enter your string :")
str1=[]
count=0

for i in str:
    if i not in str1:
        str1.append(i)
        
for i in str1:
    count=0
    for j in str:
        
        if i==j:
            count+=1
    print(i,"->",count)

    
    
    
Program 75:
"""Please write a program which accepts a string from console and print it in reverse order.
Example:
If the following string is given as input to the program:
rise to vote sir
Then, the output of the program should be:
ris etov ot esir"""

str=input("Enter your string :")
result=""

for i in str:
    result=i+result
    
print(result)

print(str[::-1])


Program 76:
"""Please write a program which accepts a string from console and print the characters that have 
even indexes."""

str=input("Enter your string :")

for i in range(0,len(str),2):
    print(str[i],end="")



Program 77:
"""Please write a program which prints all permutations of [1,2,3]"""

li=[]
n=int(input("Enter your limit :"))
 
for i in range(n):
    b=int(input())
    li.append(b)
    


Program 78:
"""Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many 
chickens do we have?
Hint:
Use for loop to iterate all possible solutions."""

head=int(input("Enter the number of heads :"))
legs=int(input("Enter the number of legs :"))

for i in range(1,legs+1):
    if i*4+(head-i)*2==legs:
        print("Count of rabbits = ",i)
        n=i
  
print("Count of chickens = ",head-n)

