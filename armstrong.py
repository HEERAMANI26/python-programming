'''num = int(input("Enter any number"))
sum = 0
a = num
while num > 0:
    dg = num %10
    sum+= dg*dg*dg
    num = num//10
if a == sum:
    print("this is armstrong number")
else:
    print("this is not armstrong number")'''

'''s =int(input("Enter string:"))
a = str(s)
rev = a[::-1]
if rev == a:
    print("palindrome")
else:
    print("not palindrome")
'''
'''s = input("Enter string:")
if s[::-1]:
    print("palindrome")
else:
    print("not palindrome")'''
'''for i in range(1,9):
    for j in range(1,i+1):
        print(i,end=' ')
    print()'''

'''num1 =int(input("Enter first number:"))
num2 =int(input("Enter second number:"))
for i in range(num1,num2):
    if (i % 2==0):
        print(i)'''
'''def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
     print(a)
     print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fib(5)'''



'''def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

    # Driver Program


print(Fibonacci(9))'''

'''def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
fib(10)'''

'''num =int(input("Enter any number"))
sum = 0
a = num
while num > 0:
    dg = num % 10
    sum+= dg*dg*dg
    num = num//10
if a == sum:
        print("armsstrong number")
else:
    print("not armstrong")
'''

'''num1 =int(input("Enter 1st number:"))
num2 =int(input("Enter 2nd number:"))
sum =0
for num in range(num1,num2+1):
    if num > 0:
        print(num)
        sum+=num
print(sum)'''
'''num1 =int(input("Enter 1st number:"))
num2 =int(input("Enter 2nd number:"))
sum =0
for num in range(num1,num2+1):
    if num % 2==0:
        print(num)
        sum+=num
print(sum,"total sum of even number",num1,num2)'''

'''num =int(input("Enter any number:"))
rev =0
while num>0:
    rev=rev*10 + num %10
    num=num//10
    print("reverse",rev)'''

'''n =int(input("Enter any number:"))
i=1
while i<=n:
    print(i)
    i =i+1'''
'''n =int(input("Enter any number:"))
i=10
while i>=1:
    print(i)
    i =i-1'''
'''n =int(input("Enter any number:"))
i =1
sum =0
while i<=n:
    print(i)
    sum+=i
    i =i+1
print(sum)'''

'''n =int(input("Enter any number:"))
i=n
sum=0
while i>=1:
    print(i)
    sum+=i
    i=i-1
print(sum)'''

'''n =int(input("Enter any number:"))
i=1
sum=0
while i<=n:
    print(i*i)
    sum+=i*i
    i=i+1
print(sum)'''
'''n =int(input("Enter any number:"))
i=n
sum=0
while i>=1:
    print(i**3)
    sum+=i**3
    i=i-1
print(sum)'''

'''n =int(input("Enter any number:"))
i=2
while i<=n:
        print(i)
        i=i+2'''

'''n =int(input("Enter any number:"))
i=1
sum=0
while i<=n:
    if i%2==0:
        print(i)
        sum+=i
    i=i+1
print(sum)'''

n =int(input("Enter number to find out the sum of digit:"))
sun=0
while (n>0):
    sum+= sum+ n%10
    n=n//10

print(sum)




















