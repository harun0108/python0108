# n=input("enter yor name")
# print ("your name is", n  )

# n="hello world"
# print(n)
# print( type(n))
# c=False
# print(c)
# print(type(c))
# n=int(input())
# print(n)
# s='today'
# print(5*s,sep="today")

# n=int(input())
# x=int(input())
# if n>x:
#     print("n is larger than x")
# else:
#     print("n is smaller than x")
#     print("hello")
# n=int(input("enter your number"))
# if n%3==0:
#     print("zero")
# elif n%3==1:
#     print("one")
# else:
#     print("two")

# for i in range(1,20,2):
#     print(i)
# n=int(input("any no"))
# sum=0
# for i in range(1,n+1) :
#     sum +=i
# print("sum is :", sum)
# n=int(input("any no"))
# sum=0
# for i in range(1,n) :
#     sum =sum*i
# print('factorial is :', sum)
# n=int(input("any no"))
# val=1
# for i in range(1,n+1) :
#     val=val*i
# print (val)

# n=int(input('enter your number'))
# if n%3==0 and n%15==0:
#     print("FizzBuzz")
# elif n%5==0:
#     print("Buzz")
# elif n%3==0:
#     print("Fizz ")
# else:
#     print("error")

#calculator


# a=int(input('1st no'))
# b=int(input('2nd no'))
# c=input('operator')
# if c=='+' :
#     print(a+b)
# elif c=='a-b' :
#     print(a-b)

#leap year, must be divisible by 4...skip 100th year unless divisible by 400


# n=int(input('enter the year'))

# if n%100==0 and n%400==0:
#     print('leap year')
# elif n%100==0:
#     print('not a leap year')
# elif n%4==0:
#     print('leap year')
# else:
#     print('not a leap year')

# python loop
# for i in range(2,10,2):
#     print(i,end=' ')
#     i=i+1

# take a number from the user and print the table of that number

# # n=int(input('enter your number'))
# for n in range(n,n*10+1,n):
#     print(n)


# for n in range(19,0,-2):
#     print(n)

# n=int(input('enter your no'))
# for n in range(0,n+1,1):
#       c=(n*(n+1)/2)
# print(c)


# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# n=int(input())
# sum=1
# for i in range(1,n+1):
#     sum=sum*i 
# print(sum)


# Nested loop

# for i in range(5):
#     for j in range(i):
#         print(i,end='')
#     print()

# 1. star pattern
# n=5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# n=int(input())
# for i in range(n):
#     for j in range(n-i):
#        print("*",end='')
#     print()
#     n=3
#         ***
#         **
#         *

# Break and continue statements

# for i in range(10):
#    if i==5:
#       break
#    print(i)

# for i in range(10):
#    if i%2==0:
#       continue #skipping statement
#    if i==7:
#       break# loop exiting statement
#    print(i)

# check whether a number is prime or not

# n=int(input())
# for i in range(2,n):
#    if n%i==0:
#       print('not a prime number')
#       break 
# else:
#       print('prime number')

# n=int(input('enter any number'))
# for i in range(n):
#    if i>=50:
      
#       break
#    print(i)
   



# print('hello')
i=1
while i<10:
   print(i)
   i=i+1
   

# n=int(input('no'))
# for i in range(2,n):
#    if i%2==0:
#       continue
#    print(i)


# n=int(input('no'))
# i=1
# while i<n:
#    print('hell',i)
#    i+=1

# strip() :-it removes spaces from the start and end of the string
# split() :-it splits the string on the basis of the character provided in the ' '



# s= ' i want to learn python ' 
# print(s)
# print(s.strip())
# print(s.split('a'))



