

#question 1
""" Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
Consider use range(#begin, #end) method"""
list1=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
       list1.append(i)
print(list1)


#question 2
""" Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""
li=[1,2,3,4,5]
f=1
l1=[]
for i in li:
    f=f*i
    l1.append(f)
print(l1)
    
#question 3
"""With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()"""
dic={}
n=int(input("enter a number"))
for i in range(1,n+1):
    dic[i]=i*i
print(dic)

#question 4
""" Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple"""

li=[]
n=int(input("number"))
for i in range(0,n):
    i=int(input())
    li.append(str(i))
print(li)
t=tuple(li)
print(t)


#question 5
"""Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
Hints:
Use __init__ method to construct some parameters"""
class Str:
    def __init__(self):
        pass
    def getstring(self):
        self.b=str(input("Enter the string"))
    def printtring(self):
        print(self.b.upper())
      
obj=Str()
obj.getstring()
obj.printtring()




def cone(r,l,pi=3.1415):
    area=pi*r*(r+l)
    print('area of the cone',area)
    

cone(9,5)
import math

def persqr(x):
    sqr=math.sqrt(x)
    if sqr-math.floor(sqr)==0:
        print('given value is perfect squar',x)
    else:
        y=math.floor(math.sqrt(x))+1
        a=(y*y)
        b=(a-x)
        print('the number to be added ',b)
        print('the perfect square is ',a)
    print('the given value is ',x)       
persqr(10)

#Question 6

'''Write a function which takes one number as argumengt,if the 
number is prime then return the number otherwise return next prime number.'''

def prime(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
    if flag!=1:
        print(n)
    else:
        prime(n+1)
prime(14)

#Question 7
"""Write a function which takes four numbers as arguments,and return avg,
max and min"""
def avmin(a,b,c,d):
    w=a
    x=b
    y=c
    z=d
    avg=(w+x+y+z)/4
    mn=min(w,x,y,z)
    mx=max(w,x,y,z)
    print(avg)
    print(mn)
    print(mx)
avmin(3,4,5,6)

#Question 8
"""Write a function which takes one number as argument,if the number is perfect
square then return the number otherwise return which minimum number to be added to
get next perfect square"""
import math
def per(n):
    sqr=math.sqrt(n)
    if sqr-math.floor(n)==0:
        print(n," is a perfect square")
    else:
        a=math.floor(math.sqrt(n))+1
        b=a*a
        c=b-n
        print("The number to be added ",c)
        print("The next perfect square is ",b)
        print("The given value is ",n)
per(14)
            
#Question 9
"""Write function to find area of the cone with PI as default argument"""
#A=πr(r+h2+r2)
import cmath         
def cone(h,r):
    pi=3.14
    a=h
    b=r
    l=cmath.sqrt(b*b+a*a)
    Area=pi*b*(b+l)
    print(float(Area))
cone(2,3)

#Question 10
"""Write function to take three values as arguments then find whether it forms
the triangle,if it forms then return circumscribed circle,inscribed circle 
otherwise return 'with provided values triangle cannot be formed"""


import math
def tri(x,y,z):
    a=x
    b=y
    c=z
    if a+b>c and a+c>b and b+c>a:
        s=(a+b+c)/2
        r=math.sqrt((s-a)*(s-b)*(s-c)/s)
        cir=(a*b*c)/math.sqrt((a+b+c)*(b+c-a)*(a+b-c)*(a+c-b))
        print("Radius of circumscribed circle is: ",cir)
        print("Radius of inscribed circle is: ",r)
    else:
        print("with provided values triangle cannot be formed")
tri(15.6,20.4,22.5)
#radius	=abc /√(a+b+c)(b+c−a)(c+a−b)(a+b−c)

#Question 11:

"""Create a class employee with attributes I'd, name, city, salary,age, experience.
That class should have function "isheoverpaid" and it should return yes
if he paid more than 3*experience*100000 (for 1 to 5 years)
 2.5*experience *100000 for more than 5 years experience.  
 Otherwise it should return no"""


class Employee:
    def __init__(self):
        pass
    def isheoverpaid(self,salary,exp):
        ts=salary*exp
        if exp>=1 and exp<=5:
            limit=3*exp*100000
            if ts>limit:
                return True
            else:
                return False
        if exp>5:
            limit=2.5*exp*100000
            if ts>limit:
                return True
            else:
                return False
obj=Employee()
obj.isheoverpaid(300000,4)
  
#Question 12:      

"""Create class bank customer with attributes name,  age, salary, amount.
Functions credit and debit.  both functions should take credit or debit amount
as int, if invalid input is provided then it should ask for valid input for
5 times,  after that it should break saying u have reached max.
Amount of chances, please try afterwards.If input amount is valid then amount
attribute to be updated accordingly)"""
    

class Bank:
    def __init__(self):
        self.amount=0
    if type(self.n)==int:
        def account(n):
            s=input("c or d")
            if s=='c':
                def credit(self,n):
                    self.amount=self.amount+n
            elif s=='d':
                def debit(self,n):
                    self.amount=self.amount-n
    else: 
        a=1
        while a>5:
            account(n+1)

obj=Bank()
obj.account(1000)   

#Question 13:
"""Write a program that computes the net amount of a bank account based a 
transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""



"""n=int(input("Enter no of transactions"))
d=[]
w=[]
sum=0
dif=0
for j in n:
    s=input("d or w")
    for i in s:
        if s=="d":
            a=int(input("Enter your deposit"))
            sum=sum+a
            d.append(a)
        
        elif s=="w":
            b=int(input("Enter withdraw"))
            dif=dif+b
            w.append(b)
        
print(d)
print(w)"""

d=[]
w=[]
a=1
while a==1:
    s=input("d or w\n")
    if s=="d":
        b=int(input("Enter your deposit\n"))
        d.append(b)
    elif s=="w":
        c=int(input("Enter withdraw\n"))
        w.append(c)
    print("Do you want cotinue Y=1 or N=0\n",end="")
    a=int(input())
print("Net amount =",sum(d)-sum(w))

#Question 14:
"""Write a program that accepts a sentence and calculate the number of 
upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""
#1
n=str(input("Enter the word"))
small=0
capital=0
for i in n:
    if ord(i)>=97 and ord(i)<=123:
        small+=1
    elif ord(i)>=65 and ord(i)<=92:
        capital+=1
print("SMALL LETTERS",small)
print("CAPITAL LETTERS",capital)
#2
n=str(input("Enter the word"))
s=0
c=0
for i in n:
    if i.isupper():
        c+=1
        
    if i.islower():
        s+=1
        
print("SMALL LETTERS",s)
print("CAPITAL LETTERS",c)
print(n)
print(n.swapcase())

"""Identify the count of letters"""
str=input("Enter the string")

#Question 15:

"""-Define a class person and its two classes.
Define a class Person and its two child classes: Male and Female.All classes 
have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
Hints:Use Subclass(Parentclass) to define a child class."""
class Person:
    def __init__(self):
        pass
        self.male="male"
        self.female="female"
class Male(Person):
    #def __init__(self):
        #pass
    def getgender(self):
        print(self.male)
class Female(Person):
    #def __init__(self):
       # pass
    def getgender(self):
        print(self.female)
obj1=Male()
obj2=Female()
obj1.getgender()
obj2.getgender()


#Question 16:
"""Now a days, Ohani has become very expert in mathematics. Her teachers like her very much 
because of her excellent performance.One day, one of her teacher gave her a problem to solve. 
He will give Ohani a number N. This will represent a table of N rows.The first 
row contains number from 1 to N. Then the next line will contain N-1 numbers,
In the second row, the first number will be the summation of the first two numbers
(1 + 2 ) of the previous row, the second number will be the summation of the second two
numbers (2 + 3) of the previous row and so on. Row 3 will have N-2 numbers with 
same procedures. Same procedure follows for row 4, row 5, .... , row N. On the last row,
there will be only a single number. Ohani has to tell that only number of the Nth row.
For example: If N = 4, then the table is: 1   2   3   4  3    5    7     8   12      20  
So Ohani has to answer the last remaining number: 20. She can answer when N is small,
but can't when N is large.Can you help her?"""

"""n=int(input("Enter the limit"))
while n<=0:
    for i in range(1,n+1):
        print(i)
        n-=1



n=int(input("Enter the limit"))
a=n
c=0
sum=0
for i in range(1,n+1):
    for j in range(i,a+1):
        c=c+1
        for s in range(i,j):
            sum=(c+(c+1))
        #print(c,end="")
        n=n-1
    print()
print("sum=",sum)"""


n=int(input("Enter the limit"))
c=0
s=1
sum=0
for i in range(n,0,-1):
    #for j in range(0,s):
        #print(" ",end="")
    #s+=1
    for k in range(0,i):
        c+=1
        #print(" ",c,end="")
        sum=sum+(i-1)
print("sum=",sum)
  
#Question 17:  
"""write a program to find the GCD or HCF of any number."""
a=int(input("Enter first number"))
b=int(input("Enter second number"))
x=1
if a>b:
    n=a
else:
    n=b
for i in range(1,n+1):
    if a%i==0 and b%i==0:
        if i>x:
            x=i
print(x)

#Question 18:

"""print all the prime number"""
n=int(input("Enter the limit"))
a=2
for i in range(2,n):
    if a<=n:
        if a%i!=0:
            print(i)
    a+=1

n=int(input("Enter the limit"))
a=2
while a<=n:
    for i in range(2,a):
        flag=0
        if a%i!=0:
            flag=1
        if flag==1:
            print(a)
        a+=1

#Question 19:

"""write a program that computes the values of a+aa+aaa+aaaa with a given digit as value of a."""
a=int(input("Enter your number"))
sum=0
total=0
for i in range(1,5):
    sum=sum*10+a
    total=total+sum
print(total)

#Question 20:
Average of n numbers

n=int(input("no"))
a=[]
for i in range(0,n):
    b=int(input())
    a.append(b)
avg=sum(a)/n
print(avg)

#Question 21:
Swapping without using temp variables

print("Numbers before swapping")
a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
a=a+b
b=a-b
a=a-b
print("After swapping {} and {}".format(a,b))

#Question 21:
To reverse a given number

n=int(input("Enter your no:"))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("Reverse of the numberis :",rev)
    
#Question 22:
Pgm to print odd numbers in given range

a=int(input("Enter first no:"))
b=int(input("Enter your limit:"))
for i in range(a,b+1):
    if i%2!=0:
        print(i)

#Question 23:
To find sum of digits

n=int(input("Enter your no:"))
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print("sum of digits",sum)

#Question 24:
Print all numbers in a range divisible by a given number

a=int(input("Enter first no:"))
b=int(input("Enter your limit:"))
n=int(input("Enter your divisible no:"))
print("Your numbers are:")
for i in range(a,b+1):
    if i%n==0:
        print(i)
 
#Question 25:       
Find smmalest divisor of a number

n=int(input("Enter your no:"))
print("smallest divisor is:")
for i in range(2,n):
    if n%i==0:
        print(i)
        break

a=[]
n=int(input("Enter your no:"))
print("smallest divisor is:")
for i in range(2,n+1):
    if n%i==0:
        a.append(i)
    a.sort() 
print(a[0])

#Question 26:
To count the number of digits in a number

n=int(input("Enter your no:"))
count=0
while n>0:
    n=n//10
    count+=1
print("Number of digits:",count)

#Question 27:
To check a number is palindrome or not

n=int(input("Enter your no:"))
a=n
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if sum==a:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")

#Question 28:
To read a number and print 1+2+...+n= series

n=int(input("Enter your no:"))
sum=0
for i in range(1,n+1):
    print(i,end="")
    sum=sum+i
    for j in range(0,1):
        print("+",end="")
       
print("=",sum)

#Question 29:
To read a number and print summation by each row

n=int(input("Enter your no:"))
sum=0
if n==1:
    print(n,"=",sum+n)
else:
    for i in range(1,n+1):
        sum=sum+i
        for j in range(1,i+1):        
            print(j,end="")            
            for k in range(0,1):
                if j<i:
                    print("+",end="")
        print("=",sum)   

#Question 30:        
To print identity

n=int(input("Enter your no:"))
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print("1",end="")
        else:
            print("0",end="")
    print()
    
#Question 31:
To print inverted pattern pf star

n=int(input("Enter your no:"))
for i in range(n,0,-1):
    print("*"*i)
    
n=int(input("Enter your no:"))
for i in range(1,n+1,1):        
    #s=0
    for s in range(0,i):
        print(" ")
        #s+=1
    print("*"*i)
    
    
#Question 32:    
To print pyramid

n=int(input("Enter your no:"))
for i in range(1,n+1):
    s=0
    for s in range(0,i):
        print(" ")
        
        for j in range(i,s+1):
            print("*",end="") 
        s+=1
    print()
    
    
#Question 33:
To find leap year
n=int(input("Enter your no:"))
if n%4==0 and n%100!=0 or n%400==0:
    print(n," is a leap year")
else:
    print(n," is not a leap year")

#Question 34:    
Prime factor

n=int(input("Enter your no:"))
while i<=n:
    k=0
    if n%i==0:
       j=1
       while(j<=i):
           if i%j==0:
               k+=1
           j+=1
       if k==2:
           print(i)
       i+=1
    
    
    
    
for i in range(2,n):
    if n%i==0:
        print(i)
        n=n/i
print(int(n))
    
#Question 35:
To generate all the divisor of an integer

n=int(input("Enter your no:"))
print("Divisors are :")
for i in range(1,n+1):
    if n%i==0:
        print(i)

#Question 36:
Print largest even and largest odd number in list

n=int(input("Enter your no of elements:"))
a=[]
b=[]
for i in range(0,n):
    c=int(input())
    if c%2==0:
        b.append(c)
    else:
        a.append(c)
a.sort()
b.sort()
count=0
count1=0
for j in a:
    count+=1
for k in b:
    count1+=1
print("Largest odd number is :",a[count-1])
print("Largest even number is :",b[count1-1])

#Question 37:
To print table of a number

n=int(input("Enter your no :"))
for i in range(1,11):
    print(i,"*",n,"=",n*i)

#Question 38:
Check armstrong or not

n=int(input("Enter your no :"))
temp=n
sum=0
while n>0:
    r=n%10
    sum+=r**3
    n=n//10
if temp==sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
 
#Question 39:  
Perfect number or not

n=int(input("Enter your no :"))
temp=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if temp==sum:
    print("Number is Perfect")
else:
    print("Number is not Perfect")

#Question 40:
Strong number or not

"""n=int(input("Enter your no :"))
temp=n
sum=0
while n>0:
    r=n%10
    f=1
    for i in range(1,r+1):
        f=f*i
    sum+=f
if temp==sum:
    print("Number is strong")
else:
    print("Number is not strong")"""
    
    
n=int(input("Enter your no :"))
temp=n
sum=0
while n:
    r=n%10
    f=1
    i=1
    while i<=r:
        f=f*i
        i=i+1
    sum+=f
    n=n//10
if temp==sum:
    print("Number is strong")
else:
    print("Number is not strong")

#Question 41:
To find LCM of 2 numbers

a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
if a>b:
    c=a
else:
    c=b
while 1:
    if c%a==0 and c%b==0:
        print("LCM is :",c)
        break
    c=c+1
    
#Question 42:
Prime or not

a=int(input("Enter first no:"))
k=0
for i in range(2,a//2+1):
    if a%i==0:
        k=k+1
if k<=0:
    print("prime")
else:
    print("not prime")

#Question 43:
Print prime numbers in given range

r=int(input("Enter first no:"))
#b=int(input("Enter second no:"))

for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if a%i==0:
            k=k+1
    if k<=0:
        print(a)


n=int(input("Enter your number"))

sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum is:",sum)

#Question 44:
find sum of series 1+x^2/2+x^3/3+...+x^n/n

n=int(input("Enter your number"))
x=int(input("Enter value for x:"))
sum=1
for i in range(2,n+1):
    s=(x**i)/i
    sum=sum+s
print("sum is :",round(sum,2))

#Question 45:   
To search the number of times a particular number occured in list

n=int(input("Enter your number of elements"))
print("Enter your elements")
a=[]
count=0
for i in range(0,n):
    b=int(input())
    a.append(b)
c=int(input("Enter the number to be searched"))
for i in a:
    if c==i:
        count+=1
print("Number of times",c,"appeared is :",count)

#Question 46:
Replace the letter a with $ in a string
str=input("Enter your string :")
str1=str.replace('A','$')
str1=str.replace('a','$')
print(str1)

#Question 47:
Remove the nth character from a non empty string

def remove(a,n):
    f=a[:n]
    l=a[n+1:]
    return f+l
a=input("Enter your string:")
n=int(input("Enter the value of index to be removed:"))
print(remove(a,n))

#Question 47:
Two strings are anagram or not

a=input("Enter your first string:")
b=input("Enter your second string:")
if sorted(a)==sorted(b):
    print("anagram")
else:
    print("not anagram")

#Question 48:
To find the count of vowels

str=input("Enter your string")
count=0
for i in str:
    if i=='a' or i=='A' or i=='e' or i=='E' or i=='o' or i=='O' i=='i' or i=='I' or i=='u' or i=='U':
        count=count+1
print("Number of vowels is:",count)

#Question 49:
Take a string and replace every blank with hyphen

str=input("Enter your string:")
str1=str.replace(' ','-')
print(str1)

#Question 50:
Count length of string

str=input("Enter your string:")
count=0
for i in str:
    count+=1
print("Length of string is :",count)

#Question 51:
Remove the characters of odd index values in a string

def modify(str):
    final=""
    for i in range(len(str)):
        if i%2==0:
            final=final+str[i]
    return final
str=input("Enter your string:")
print(modify(str))

#Question 52:
To count number of digits and letters in string

str=input("Enter your string:")
count=0
count1=0
for i in str:
    if i.isdigit():
        count+=1
    else:
        count1+=1
print("Number of digit is:",count)
print("Number of characters are :",count1)

#Question 53:
Occurance of word in string

str=input("Enter your string:")
word=input("Enter your word:")
a=[]
count=0
a=str.split(" ")
for i in range(0,len(a)):
    if word==a[i]:
        count+=1
print("The",word,"occurs in",str,"is:",count,"times")

#Question 54:
Fibanocci using reccursion

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter no of terms"))
for i in range(n):
    print(fib(i)) 
    
#Question 55:
Factorial using reccursion
def fact(n):
    if n<=1:
        return n
    else:
        return (n*fact(n-1))
n=int(input("Enter your number"))
print(fact(n))

#Question 56:
Reverse a string using reccursion

def rev(str):
    if len(str)==0:
        return str
    else:
        return rev(str[1:])+str[0]
    
n=input("Enter your string:")
print(rev(n))



#Question 57:
Binary search

def binarysearch(list1,key):
    first=0
    last=len(list1)-1
    
    found=False
    while first<=last and not found:
        mid=(first+last)//2
        if key==list1[mid]:
            found=True
        elif key<list1[mid]:
            last=mid-1
        else:
            first=mid+1
    if found==True:
        print("Key is found:")
    else:
        print("Key is not found:")
n=int(input("Enter number of elements:"))
list1=[int(input()) for i in range(n)]
list1.sort()
key=int(input("Enter your key:"))
binarysearch(list1,key)












    