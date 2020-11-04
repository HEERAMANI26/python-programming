'''num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
if num1 > num2:
    print(num1)
else:
    print(num2)

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
if (a > b and a > c):
    print(a ,"is greater than", b ,"and",c)
elif (b > a and b > c):
    print(b, "is greater than",c ,"and",a)
else:
    print(c ,"greater than", b ,"and", a)

a = int(input("Enter any number:"))
if a > 0:
    print(a,"is positive number")
else:
    print(a,"negative number")

a = int(input("Enter any number:"))
if(a % 5 == 0):
    print(a, "is divisible by 5")
else:
    print(a, "not divisible by 5")

num = int(input("Enter any number:"))
if num % 2 ==0:
    print(num, "is an even number")
else:
    print(num , "is an odd number")

year =int(input("Enter year:"))
if year % 4 == 0 and year % 100!=0:
    print("{0} is leap year".format(year))
elif year % 100!= 0:
    print("{0} is not leap year".format(year))
elif year % 400:
    print("{0} is leap year". format(year))
else:
    print("{0} is not leap year". format(year))


ch = input("Enter alphabate:")
if ((ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z")):
    print(ch, "is alphabate")
else:
    print(ch, "is not  alphabate")
ch = input("Enter alphabate")
if (ch == "a" or ch =="e" or ch =="e" or ch =="i" or ch =="o" or ch =="u"):
    print("vowel", ch)
else:
    print("consonant", ch)
ch = input("Enter alphabate:")
if ch.isupper():
    print("this is upper case letter",ch)
else:
    print("this is lower case letter",ch)

num = int(input("Enter any number"))
for i in range(num):
    if num % 2 ==0:
        print("not prime number")
        break
else:
    print("prime no")'''

#while loop

'''i = 1
while i <= 100:
    print(i)
    i+=1'''
'''start =int(input("Enter start number"))
max = int(input("Enter max number"))
for i in range(start,max+1):
    if(i % 2 ==0):
        print(i,"even")
    else:
        print(i,"odd")'''
# sum of digit
'''num =int(input("Enter any number:"))
sum=0

while (num>0):
    sum =sum + (num%10)
    num =num//10
print(sum)'''

# sum of square of digit
'''num =int(input("Enter number:"))
sum=0
while num>0:
    sum = sum + (num%10)*(num%10)
    num = num//10

print(sum)'''

#sum of cube of digit
'''num =int(input("Enter any number:"))
sum=0
while num>0:
    sum = sum + (num%10)*(num%10)*(num%10)
    num = num//10
print(sum)'''

# check armstrong number:
'''num =int(input("Enter any number"))
a=num
sum=0
while num>0:
    sum = sum + (num%10)**3  # power = number of digit
    num = num//10
if a == sum:
    print("this is armstrong number")
else:
    print("this is not armstrong number")'''

#check palindrome...
num =int(input("Enter number to check palindrome or not:"))
x=num
rev=0
while num>0:
    rev = (rev*10) + num%10
    num = num//10
if x == rev:
    print("this is palindrome number")
else:
    print("not palindrome")

# check prime number
'''n =int(input("Enter number:"))
count=0
i=1
while i<=n:
    if (n%i==0):
        count = count +1
    i=i+1
if count == 2:
    print("this is prime number")
else:
    print("not a prime number")'''

#check factorial number:

'''n =int(input("Enter any number:"))
fac=1
while n>0:
    fac = fac*n
    n =n-1
print(fac)'''

n =int(input("Enter number"))
x=0
y=1
z=0
while z<=n:
    print(z)
    x =y
    y =z
    z =x+y


















