#!/usr/bin/env python
# coding: utf-8

# Eduardo Baldo Chamorro
# 
# Homework 1

# Problem 1:

# https://www.hackerrank.com/domains/python/py-introduction codes in order

# Hello World:

# In[ ]:


if __name__ == '__main__':
    print("Hello, World!")


# If else:

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if 0 < n <= 100:
        if n % 2 == 1:
            print ('Weird')
        elif n % 2 == 0 and n >= 2 and n <= 5:
            print('Not Weird')
        elif n % 2 == 0 and n >= 6 and n <= 20:
            print('Weird')
        elif n % 2 == 0 and n >= 21:
            print('Not Weird')


# Operators:

# In[ ]:


if __name__ == '__main__':
    
    a = int(input())
    b = int(input())
    
    if 0 < a <= 10**10 and 0 < b <= 10**10:
        print(a+b)
        print(a-b)
        print(a*b)


# Division:

# In[ ]:


if __name__ == '__main__':
    
    a = int(input())
    b = int(input())
    print(int(a/b))
    print(a/b)


# Loops:

# In[ ]:


if __name__ == '__main__':
    
    n = int(input())
    i=0 
    if 0 < n < 21:
        while i < n:
            print(i**2)
            i += 1


# Write funcion:

# In[ ]:


def is_leap(year):
    leap = False
    
    if 1900 <= year <= 10**5:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        elif year % 4 == 0:
            leap = True
        else:
            leap = False 
    
    return leap


# Print Function

# In[ ]:


if __name__ == '__main__':
    
    n = int(input())
    i=1
    if 0 < n < 151:
        while i <= n:
            print(i, end = '')
            i += 1


# https://www.hackerrank.com/domains/python/py-basic-data-types codes in order
# 
# List comprehensions:

# In[ ]:


if __name__ == '__main__':
    
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    A = []
    for i in range(0,x+1):
            for j in range(0,y+1):
                    for k in range(0,z+1):
                        if i + j + k != n:
                            A.append([i,j,k])
                            
    print(A)


# Runner-up score

# In[ ]:


if __name__ == '__main__':
    
    n = int(input())
    arr = map(int, input().split())
    
    A = list(arr)
    S = max(A)
    R=-100
    if 2<= n <=10 and min(A) >-101 and max (A) < 101:
        for i in range(0, n):
            if -100 <= A[i] <= 100:
                if A[i] > R and A[i] < S:
                    R = A[i]
        print(R)


# Nested List

# In[ ]:


if __name__ == '__main__':
    x=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x.append([name,score])
    
    #select minimum
    if 2 <= len(x) <= 5:
        #select minimum
        m=min(x,key = lambda col:(col[1]))
        #remove all minimum
        b=[]
        for i in range(0,len(x)):
            if x[i][1] != m[1]:
                b.append(x[i])
        #order
        b.sort()
        #select second minimum score only
        sm=min(b,key = lambda col:(col[1]))[1]
        #remove values not equal to second minimum
        a=[]
        for j in range(0,len(b)):
            if b[j][1] == sm:
                print(b[j][0])               
    


# Percentage

# In[ ]:


if __name__ == '__main__':
    
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    x=student_marks[query_name]
    
    if 2<= n <= 10 and len(x)==3 and max(x) <=100 and min(x) >=0:
        m=0
        for i in range(0, len(x)):
            m=m+x[i]
        med=m/len(x)
        print(format(med, ".2f"))


# Lists

# In[ ]:


if __name__ == '__main__':
    
    N = int(input())
    l=[]
    x=[]
    for i in range(N):
        x=input().split(' ')
        if x[0] == 'insert':
            l.insert(int(x[1]),int(x[2]))
        elif x[0] == 'print':
            print(l)
        elif x[0] == 'remove':
            l.remove(int(x[1]))
        elif x[0] == 'append':
            l.append(int(x[1]))
        elif x[0] == 'sort':
            l.sort()
        elif x[0] == 'pop':
            l.pop()
        elif x[0] == 'reverse':
            l.reverse() 


# Tuples

# In[ ]:


if __name__ == '__main__':
    
    n = int(input())
    integer_list = map(int, input().split())
    
    print(hash(tuple(integer_list)))


# https://www.hackerrank.com/domains/python/py-strings 
# 
# codes Tried in order
# 
# Text alignment, Capitalize

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

thickness = int(input())

if thickness % 2  == 1:
    width=thickness
    
    for i in range(1,width*2,2):
        H=i*'H'
        print (H.center(width*2,' '))

    for i in range(0,int(width + 1)):
        H=width*'H'
        S=(2*width-2)*' '
        print (H.center(width*2,' '),S,H.center(width*2,' '))

    for i in range(0,round(width*3/5)):
        H=width*'H'*5
        print(H.rjust(width*5+int((width*2-width)/2)))

    for i in range(0,int(width*6/5)):
        H=width*'H'
        S=(2*width-2)*' '
        print (H.center(width*2,' '),S,H.center(width*2,' '))

    for j in reversed(range(1,width*2,2)):
        R=j*'H'
        T=(4*width-1)*' '
        print (T,R.center(width*2,' '))


# In[ ]:


# Complete the solve function below.
def solve(s):
    
    if 0 < len(s) < 1000:
        
        names=(s.split())
        y=[]
        
        for i in range(0,len(names)):
            
            x=list(names[i])
            x[0]=x[0].swapcase()
            y.append(''.join(x))
            
        sol=' '.join(y)
        
        return sol
        
    else:
        return ''


# Code Solved in order
# 
# swap case

# In[ ]:


def swap_case(s):
    if len(s)<=1000:
        return s.swapcase()



# Split and join

# In[ ]:


def split_and_join(line):
    line.split(' ')
    x = line.split(' ')
    y = '-'.join(x)
    return y

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# Your name:

# In[ ]:


#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    lastb=[last,'!']
    lname=''.join(lastb)
    x=[first,lname]
    d=' '.join(x)
    return print('Hello', d,'You just delved into python.')


# Mutations

# In[ ]:


def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    x=''.join(l)
    return x


# Find String

# In[ ]:


def count_substring(string, sub_string):
    m=0
    for i in range(0,len(string)-len(sub_string)+1):
        if string[i:len(sub_string)+i]==sub_string:
            m += 1
    return m


# String Validators

# In[ ]:


if __name__ == '__main__':
    s = input()
    
an=0
a=0
d=0
l=0
u=0
for i in range(0,len(s)):
    if s[i].isalnum() is True:
        an += 1
for i in range(0,len(s)):
    if s[i].isalpha() is True:
        a += 1
for i in range(0,len(s)):
    if s[i].isdigit() is True:
        d += 1
for i in range(0,len(s)):
    if s[i].islower() is True:
        l += 1
for i in range(0,len(s)):
    if s[i].isupper() is True:
        u += 1
    
if an > 0:
    print(True)
else:
    print(False)
if a > 0:
    print(True)
else:
    print(False)
if d > 0:
    print(True)
else:
    print(False)
if l > 0:
    print(True)
else:
    print(False)
if u > 0:
    print(True)
else:
    print(False)


# Text wrap

# In[ ]:


def wrap(string, max_width):
    if len(string) < 1000 and max_width < len(string):
        return textwrap.fill(string,max_width)


# Designer Door mat

# In[ ]:


if __name__ == '__main__':
    n, m = map(int, input().split())  
    w='WELCOME'
    for i in range(1,n,2):
        H=i*'.|.'
        print (H.center(m,'-'))

    print (w.center(m,'-'))

    for j in reversed(range(1,n,2)):
            H=j*'.|.'
            print (H.center(m,'-'))


# String Formatting

# In[ ]:


def print_formatted(number):
    if 1 <= number <= 99:
        l=len(bin(number)[2:])
        for i in range(1,number+1):
            print(str(i).rjust(l,' '),oct(i)[2:].rjust(l,' '),hex(i)[2:].rjust(l,' ').swapcase(),bin(i)[2:].rjust(l,' '))
            


# The minion game

# In[ ]:


def minion_game(string):
    
    if 0 < len(s) <= 10**6:
        k = 0
        st = 0
        for i in range(0,len(s)):
            if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                k += len(s) - i
            else:
                st += len(s) - i

        if k > st:
            print('Kevin', k)
        elif k < st:
            print('Stuart', st)
        else:
            print('Draw')
    return ''


# Not solved: Alphabet Rangoli, Merge the tools!

# https://www.hackerrank.com/domains/python/py-sets 
# 
# Not Solved: Set Selections, Check Subset, Check Strict Subperset
# 
# Try again in order: No idea!, Set.discard/remove/pop, Captain's room
# 

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n, m = map(int, input().split())
    N = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if 1 <= n <= 10**5 and 1 <= m <= 10**5 and min(N)>0 and max(N) <= 10**9:
        a=0
        b=0

        for i in range(0,n):
            for j in range(0,m):
                if N[i] == A[j]:
                    a += 1
            for k in range(0,m):
                if N[i] == B[k]:
                    b += 1
        like=a-b

        print(like)


# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    x=[]
    n = int(input())
    s = set(map(int, input().split()))
        
    for _ in range(int(input())):
        x=input().split(' ')
        if x[0] == 'pop':
            s.pop()           
        elif x[0] == 'discard':
            s.discard(int(x[1]))
        elif x[0] == 'remove':
            s.remove(int(x[1]))
                
    print(sum(s))


# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    
    k = int(input())
    a = list(map(int, input().split()))
    b = list(set(a))
    
    for i in range(len(b)):
        if sum(a)-b[i] == (sum(b) - b[i])*k:
            print(b[i])


# Solved in order
# 
# Intro to sets

# In[ ]:


def average(array):
    if len(array)<= 100:
        return sum(list(set(array)))/len(list(set(array)))


# symmetric difference

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    M = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    b = set(map(int, input().split())
            )
    x = list(a.difference(b)) # Values which exist in a but not in b
    y = list(b.difference(a))
    z = x + y
    z.sort()

    for i in range(0,len(z)):
        print(z[i])


# Set.add()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    s=set()
    for _ in range(int(input())):
        country = input()
        s.add(country)
    
    print(len(s))


# Set.union()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    x=[]
    n = int(input())
    a= set(map(int, input().split()))
    
    m = int(input())
    b = set(map(int, input().split()))
    print (len(a.union(b)))


# set.intersesction()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    
    n = int(input())
    a= set(map(int, input().split()))
    
    m = int(input())
    b = set(map(int, input().split()))
    print (len(a.intersection(b)))


# Ser.difference()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    n = int(input())
    a= set(map(int, input().split()))
    
    m = int(input())
    b = set(map(int, input().split()))
    print (len(a.difference(b)))


# Set.symmetric_dif()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    n = int(input())
    a= set(map(int, input().split()))
    
    m = int(input())
    b = set(map(int, input().split()))
    print (len(a.symmetric_difference(b)))


# https://www.hackerrank.com/domains/python/py-collections
# 
# Try Again: DefaultDict Tutorial

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    n,m = map(int,input().split())
    A=[]
    B=[]
    for _ in range(n):
        x=input()
        A.append(x)

    for _ in range(m):
        y=input()
        B.append(y)

    for i in range(len(B)):


# Solved in order
# 
# Counter()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':

    n = int(input())
    size = input().split()
    su = 0
    
    for _ in range(int(input())):
        x = input().split(' ')
        if x[0] in size:
            su += int(x[1])
            size.remove(x[0])
    

    print(su)


# namedtuple()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

n= int(input())

Student = namedtuple('Student',input())
av = 0
for _ in range(n):
    info = list(input().split())
    i = Student(info[0],info[1],info[2],info[3])
    
    av += int(i.MARKS)
print(av/n)


# OrderedDict()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

l = {}

for _ in range(int(input())):
    
    info = input().split()
    n = ' '.join(info[:-1])
    p = int(info[-1])
    
    if n not in l:
        l[n] = int(p)
    else:
        l[n] += int(p)
    
for n, p in l.items():
    print(n, p)


# Word Order

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

l = []

for _ in range(int(input())):
    
    l.append(input())
    
a = list(Counter(l).values())

print(len(a))
print(*a)


# dequel()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    from collections import deque
     
    d = deque()
    
    for i in range(int(input())):
        x=input().split(' ')
        if x[0] == 'append':
            d.append(int(x[1]))
        elif x[0] == 'appendleft':
            d.appendleft(int(x[1]))
        elif x[0] == 'pop':
            d.pop()
        elif x[0] == 'popleft':
            d.popleft()
            
    for i in range(len(d)):
        print(d[i], end = ' ')


# Company logo

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = list(input())
    
    s.sort()

    a = Counter(s)

    m = a.most_common(3)

    for i in m:
        print(i[0], i[1])


# Pilling up

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    
    n = int(input())
    
    a = list(map(int,input().split()))
    
    l = 0
    r = len(a)-1
    pc = float('inf')
    
    s = 0
    
    while l <= r and s == 0:
        if a[l] >= a[r] and a[l] <= pc:
            pc = a[l]
            l += 1

        elif a[l] < a[r] and a[r] <= pc:
            pc = a[r]
            r -= 1
        else:
            s = 1
        
    if s == 0:
        print('Yes')
    else:
        print('No')


# https://www.hackerrank.com/domains/python/py-date-time
# 
# Solved in order
# 
# Calendar Module

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':


    import calendar

    m, d, y = map(int,input().split())
    weekd=['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    wk = calendar.weekday(y, m, d)


    print(weekd[wk])


# Time Delta

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    import calendar
    a = t1.split()
    ah = a[4].split(':')

    b = t2.split()
    bh = b[4].split(':')
    

    mon = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


    datet1 = calendar.datetime.datetime(int(a[3]), mon[a[2]], int(a[1]), int(ah[0]), int(ah[1]), int(ah[2]))
    datet2 = calendar.datetime.datetime(int(b[3]), mon[b[2]], int(b[1]), int(bh[0]), int(bh[1]), int(bh[2]))


    if int(a[5]) >= 0:
        tzone1 = calendar.datetime.timedelta( minutes = (int(a[5])//100)*60 + int(a[5]) % +100 )
    else:
        tzone1 = calendar.datetime.timedelta( minutes = (int(a[5])//100)*60 - int(a[5]) % -100 )

    rt1 = datet1 - tzone1

    if int(b[5]) >= 0:
        tzone2 = calendar.datetime.timedelta( minutes = (int(b[5])//100)*60 + int(b[5]) % +100 )
    else:
        tzone2 = calendar.datetime.timedelta( minutes = (int(b[5])//100)*60 - int(b[5]) % -100 )

    rt2 = datet2 - tzone2

    return(round(abs(rt1-rt2).total_seconds()))

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)


# https://www.hackerrank.com/challenges/exceptions
# 
# Solved

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    for _ in range(int(input())):
        a,b =input().split()

        try:
            print(int(int(a)/int(b)))
        except ZeroDivisionError:
            print ('Error Code:', 'integer division or modulo by zero')
        except ValueError as f:
            print ('Error Code:', f)


# https://www.hackerrank.com/challenges/zipped
# 
# Solved

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    n, sub = map(int,input().split())
    X=[]
    
    for _ in range(sub):
        
        A = [float(x) for x in input().split()]
        X += [A]
        
    m = zip(*X)

    for item in m:
        
        print(sum(item)/len(item))


# https://www.hackerrank.com/challenges/python-sort-sort
# 
# Solved

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    n, m = map(int,input().split())
    X=[]
    
    for _ in range(n):
        
        A = [float(x) for x in input().split()]
        X += [A]
        
    k=int(input())
    
    x = sorted(X, key=lambda X: X[k])


    for item in x:
        a = list(item)
        for i in range(len(a)):
            print(int(a[i]), end=' ')
        print('')


# https://www.hackerrank.com/challenges/ginorts
# 
# Solved

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    x = input()

    st = list(x)

    l = []
    u = []
    o = []
    e = []

    for i in range(len(st)):

        if st[i].islower() and st[i].isalpha():
            l.append(st[i])
        elif st[i].isupper() and st[i].isalpha():
            u.append(st[i])
        elif st[i].isdigit() and int(st[i]) % 2 == 0:
            o.append(st[i])
        elif st[i].isdigit() and int(st[i]) % 2 == 1:
            e.append(st[i])

    l.sort()
    u.sort()
    o.sort()
    e.sort()

    f = l + u + e + o

    F = ''.join(f)

    print(F)


# https://www.hackerrank.com/challenges/map-and-lambda-expression
# 
# Solved

# In[ ]:


cube = lambda x: x**3 

def fibonacci(n):

    fi=[]
    
    if n == 1:
        fi = [0]
    elif n == 0:
        fi = ''
    elif n == 2:
        fi = [0,1]
    else:
        fi = [0,1]
        for i in range(2, n):
            fi.append(fi[i-2]+fi[i-1])
        
    return fi


# https://www.hackerrank.com/domains/python/py-regex
# 
# Solved in order
# 
# Floating point number

# In[ ]:


if __name__ == '__main__':
    x=[]
    for _ in range(int(input())):
        name = input()
        x.append((name))
    if 0 < len(x) < 11:
        for i in range(0,len(x)):
            if x[i].count('.')>0:
                try:
                    float(x[i])
                    print(True)
                except ValueError:
                    print(False)
            else:
                print(False)
        


# split()

# In[ ]:


regex_pattern = r"[.,]"	# Do not delete 'r'.


# Group(), Groups()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    s = input()
    if 0 < len(s) < 100:
        x=[]
        for i in range(1,len(s)):
            if s[i-1].isalnum() is True:
                if s[i] == s[i-1]:
                    x.append(s[i-1])
        if len(x) == 0:
            print(-1)
        else:
            print(x[0])


# findall() finditer()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':


    import re

    S = input()

    m = re.finditer(r'(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])', S)
    x = 0

    for s in m:
        print(s.group())
        x = 1

    if x == 0:
        print('-1')


# start() end()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':


    import re

    S = input()
    k = input()

    m = re.finditer(f'(?=({k}))', S)

    if re.search(f'(?=({k}))',S) is not None:
        for s in m:
            x=[]
            x.append(s.start())
            x.append(s.end()+ len(k)-1) 
            print(tuple(x))
    else:
        print('(-1, -1)')


# Substitution

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

    
if __name__ == '__main__':
    
    import re

    n = int(input())

    p = r'(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)'

    for _ in range(n):
        line = input()
        m = re.sub(p, lambda x: 'and' if x.group() == '&&' else 'or', line)
        print(m)


# Roman numerals

# In[ ]:


regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.


# Phone numbers

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    import re
    
    for _ in range(int(input())):
        s = input()
        
        if re.match(r'^[789]\d{9}$', s):
            print('YES')
        else:
            print('NO')


# Email addresses

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    import email.utils
    import re
    p=r'^[a-zA-Z][\w\.\-\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

    for _ in range(int(input())):

        s = input()

        k= email.utils.parseaddr(s)

        if re.search(p, k[1]) is not None:
            print(s)


# Color code

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    import re

    p = r'#[0-9a-fA-F]{3}(?=\W|$)|#[0-9a-fA-F]{6}(?=\W|$)'

    x = 0

    for _ in range(int(input())):

        s = input()

        a = re.findall(p, s)

        if x == 1:
            for b in a:
                print(b)
        
        if re.search(r'\{',s) is not None:
            x = 1
        elif  re.search(r'\}',s) is not None:
            x = 0


# Html part 1

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    from html.parser import HTMLParser

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print ('Start :', tag)
            for i in attrs:
                print('->', i[0], '>', i[1])
        def handle_endtag(self, tag):
            print ('End   :', tag)
        def handle_startendtag(self, tag, attrs):
            print ('Empty :', tag)
            for i in attrs:
                   print('->', i[0], '>',i[1])

    p = MyHTMLParser()

    for  _ in range(int(input())):
        s = input()
        p.feed(s)


# Html part 2

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    from html.parser import HTMLParser

    class MyHTMLParser(HTMLParser):
        def handle_data(self, data):
            if data != '\n':
                print (">>> Data")
                print(data)
        def handle_comment(self, data):
            if '\n' not in data:
                print (">>> Single-line Comment")
                print(data)
            else:
                print('>>> Multi-line Comment')
                print(data)

    p = MyHTMLParser()
    ht = ''
    for _ in range(int(input())):
        ht += input()
        ht += '\n'

    p.feed(ht)


# Tags, attributes, values

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    from html.parser import HTMLParser

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print (tag)
            for i in attrs:
                print('->', i[0], '>', i[1])
                
    p = MyHTMLParser()

    for  _ in range(int(input())):
        s = input()
        p.feed(s)


# Valid uid

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    import re
    
    for _ in range(int(input())):
        
        u = input()
        
        if len(re.findall(r'[A-Z]', u)) < 2 or len(re.findall(r'[0-9]', u)) < 3 or u.isalnum() is False or len(u) != 10 or len(set(u)) != 10:
            print('Invalid')
        else:
            print('Valid')


# credit cards

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    import re

    for _ in range(int(input())):

        n = input()
        d = n.replace('-', '')
        if not re.match(r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$', n) or not re.match(r'^\d{16}$', d) or re.search(r'(\d)\1{3,}', d):
            print('Invalid')
        else:
            print('Valid')


# Postal codes

# In[ ]:


regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	# Do not delete 'r'.



# Matrix

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
mess=''
    
for i in range(m):
    for j in range(n):
        mess += matrix[j][i]

t = re.sub(r'(\b)(\W)+(\b)',' ',mess)

print(t)
          


# https://www.hackerrank.com/domains/python/xml 
# 
# Not Solved: XML2
# 
# Solved: XML1

# In[ ]:


def get_attr_number(node):
    d=0
    for item in node.iter():
        d += len(item.attrib)
    return d



# https://www.hackerrank.com/domains/python/closures-and-decorators
# 
# Solved in order
# 
# Mobile Numbers

# In[ ]:


def wrapper(f):
    def fun(l):
        a =[]
        for i in l:
            b = ['+91',i[-10:-5],i[-5:]]
            a.append( " ".join(b))
        f(a)
    return fun



# Name directory

# In[ ]:


def person_lister(f):
    def inner(people):
        s = sorted(people, key=lambda x: int(x[2]))
        return (f(people) for people in s)
    return inner


# https://www.hackerrank.com/domains/python/numpy
# 
# Solved in order
# 
# Arrays

# In[ ]:


def arrays(arr):
    list(arr)
    a = numpy.array(list(arr),float)
    return numpy.flip(a)


# Shape reshape

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

s=list(map(int,input().split()))

change_array = numpy.array(s)
change_array.shape = (3, 3)
print(change_array)    


# Transpose Flatten

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

n,m = map(int, input().split())
s = []

for _ in range(n):
    a = list(map(int,input().split()))
    s.append(a)
    
my_array = numpy.array(s)
print (numpy.transpose(my_array))


my_array = numpy.array(s)
print(my_array.flatten())


# Concatenate

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

n,m,p  = map(int, input().split())

a1 = []
a2 = []

for _ in range(n):
    r1 = list(map(int,input().split()))
    a1.append(r1)
    
    
for _ in range(m):
    r2 = list(map(int,input().split()))
    a2.append(r2)
print(numpy.concatenate((a1, a2), axis = 0))  


# Zeros and ones

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

s = list(map(int, input().split()))

print(numpy.zeros(s, dtype = int))
print(numpy.ones(s, dtype = int))


# Eye identity

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy
numpy.set_printoptions(legacy='1.13')
n,m = map(int, input().split())
print (numpy.eye(n, m, k = 0) ) 


# Mathematics

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

n,m = map(int, input().split())

a = []
b = []


for _ in range(n):
    a.append(list(map(int,input().split())))

for _ in range(n):
    b.append(list(map(int,input().split())))

a = numpy.array(a)
b = numpy.array(b)
    
    
print (a + b)                     

print (a - b)                    

print (a * b)         

print (a // b)                    

print (a % b)                     

print (a**b)               


# Floor ceil rint

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy
numpy.set_printoptions(legacy='1.13')

my_array = numpy.array(list(map(float, input().split())))

print (numpy.floor(my_array))         

print (numpy.ceil(my_array))          

print (numpy.rint(my_array))


# Sum Prod

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

n,m =map(int, input().split())
a = []
for _ in range(n):
    
     a.append(list(map(int, input().split())))

my_array = numpy.array(a)
s=numpy.sum(my_array, axis = 0)

print (numpy.prod(s)) 


# Min Max

# In[ ]:


import numpy

n,m =map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

a = numpy.array(a)
mi = numpy.min(a, axis = 1)

print(numpy.max(mi))


# Mean Var std

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

n,m =map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

my_array = numpy.array(a)
print (numpy.mean(my_array, axis = 1))
print (numpy.var(my_array, axis = 0))
print (round(numpy.std(my_array, axis = None), 11)) 


# Dot Cross

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

n = int(input())

a = []
b = []


for _ in range(n):
    a.append(list(map(int,input().split())))

for _ in range(n):
    b.append(list(map(int,input().split())))

a = numpy.array(a)
b = numpy.array(b)


print (numpy.dot(a, b))


# Inner outer

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

a = list(map(int,input().split()))

b = list(map(int,input().split()))

A = numpy.array(a)
B = numpy.array(b)

print(numpy.inner(A, B))
print(numpy.outer(A, B))


# Polynomials

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

a = list(map(float,input().split()))
A = numpy.array(a)
x = int(input())

print(numpy.polyval(A, x))   


# Linear algebra

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

n =input()

a = []
for _ in range(int(n)):
    a.append(list(map(float, input().split())))

A = numpy.array(a)

print(round(numpy.linalg.det(A),2))


# Problem 2:
# 
# Solved in order

# https://www.hackerrank.com/challenges/birthday-cake-candles

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
      if 1 <= len(candles) <= 10**5 and max(candles) <= 10**7 and min(candles) >= 1:
        a=max(candles)
        r=candles.count(a)
        return r
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# https://www.hackerrank.com/challenges/kangaroo

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if 1 <= v1 <= 10**4 and 1 <= v2 <= 10**4 and 0 <= x2 <= 10**4 and 0 <= x1 <= 10**4:

        if x1 > x2 and v1 >= v2:
            return('NO')

        if x1 < x2 and v1 <= v2:
            return('NO')
            
        if x1 > x2 and v1 < v2:
            while x1 > x2:
                x1 += v1
                x2 += v2
            if x1 == x2:
                return('YES')
            else:
                return('NO')
                
        if x1 < x2 and v1 > v2:
            while x1 < x2:
                x1 += v1
                x2 += v2
            if x1 == x2:
                return('YES')
            else:
                return('NO')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# https://www.hackerrank.com/challenges/strange-advertising

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    if 0 < n < 51:
        
        f = 5
        like = 0

        for i in range(0,n):
            like = math.floor(f/2) + like
            f = math.floor(f/2)*3
        return like

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# https://www.hackerrank.com/challenges/recursive-digit-sum

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    if 1 <= len(n) <= 10**100000 and 1 <= k <= 10**5:

        lin0=[eval(i) for i in n]
        r=sum(lin0)*k
        p = str(r)
        while len(p) != 1:
            lin = [eval(i) for i in p]
            p = str(sum(lin))
        return(p)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# https://www.hackerrank.com/challenges/insertionsort1

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    if 1 <= n <= 10**3 and max(arr) <= 10000 and min(arr) >= -10000:

    
        v = arr[-1]
        i = n-2
        while arr[i] > v and i >= 0:
            arr[i+1] = arr[i]
            i -= 1
            for j in range(0,n):
                print(arr[j],end=' ')
            print()
            
        arr[i+1]=v

        for j in range(0,n):
            print(arr[j],end=' ')
            
        return ''

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# https://www.hackerrank.com/challenges/insertionsort2

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
        
    if 1 <= n <= 10**3 and max(arr) <= 10000 and min(arr) >= -10000:

    
        for k in range(0,n-1):
            if arr[k] < arr[k+1]:
                for j in range(0,len(arr)):
                    print(arr[j],end=' ')
                print('')   
            else:
                v=arr[k+1]
                i = k
                while arr[i] > v and i >= 0:  
                    arr[i+1] = arr[i]
                    i -= 1

                arr[i+1]=v

                for j in range(0,len(arr)):
                        print(arr[j],end=' ')
                print('')
    return ''

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


# Problem 3 in https://awsacademy.instructure.com/courses/60381

# In[ ]:




