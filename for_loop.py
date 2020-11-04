# for loop
'''n1 =int(input("Enter 1st number:"))
n2 =int(input("Enter 2nd number:"))
for i in range(n1,n2+1):
    print(i)'''

# prime number
'''n1 =int(input("Enter 1st number:"))
count =0
for i in range(1,n1+1):
    if (n1 % i == 0):
        count = count+1
    i = i-1
if count ==2:
    print(n1)
else:
    print("not prime number")'''

#print table
'''n =int(input("Enter number which you want to print:"))
a =0
for i in range(1,10+1):
    if i > 0:
        print(n*i)'''

#function related problem

'''def add():
    a =int(input("Enter 1st number:"))
    b =int(input("Enter 2nd number:"))
    c =a+b
    print(c)
add()'''
#without arguments
'''def fun():
    a =int(input("Enter 1st number:"))
    b =int(input("Enter 2nd number:"))
    sum=0
    i=1
    while i <=10:
        sum+=i
        print(sum)
        i=i+1
fun()'''

#with argument

'''def mulitplication(a,b):
    c =a*b
    print(c)
mulitplication(5,-1)'''

#odd even number without no arguments
'''def odd_even():
    n =int(input("Enter number:"))
    if n % 2==0:
        print("even")
    else:
        print("odd")
odd_even()'''

#odd even with arguments

'''def odd_even(n):
    if n % 2 ==0:
        print("even number")
    else:
        print("odd number")
odd_even(9)
'''
# NAWR
'''def add():
    a =int(input("Enter 1st number:"))
    b =int(input("Enter 2nd number:"))
    c =a+b
    return c
x =add()
print(x)'''

#WAWR

'''def sub(a,b):
    c=a-b
    return c
x=sub(5,-10)
print(x)'''

#WANR

'''def add(a,b):
    c=a+b
    print(c)
a =int(input("Enter 1st number:"))
b =int(input("Enter 2nd number:"))
add(a,b)'''
#default
'''def add(a,b,c=5):
    d=a+b+c
    print(d)
add(1,2)'''

'''def add(a=5,b,c=5):
    d=a+b+c
    print(d)
add(1,3,6)'''
#break
'''i=0
while i <=5:
    if (i==3):
        break
    print(i)
    i=i+1'''

#continue
'''i=0
while i<=5:
    i=i+1

    if(i==4):
        continue
    print(i)'''


#count vowel or consonant
'''a =input("enter your name:")
vowel=0
cons=0
for i in range(0,len(a)):
    if (a[i]!=''):
        if(a[i] =='a' or a[i] =='e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u' or a[i] =='A' or
                a[i] =='E' or a[i] == 'I' or a[i] == 'O' or a[i] =='U'):
            vowel = vowel+1
        else:
            cons = cons+1
print("total number of vowel",vowel)
print("total number of cons",cons)'''

'''a =["ram","shyam","radha","Geeta","seeta","ram"]
x =a.count("ram")
print(x)
'''

'''a=[]
for i in range(5):
    x = input("Enter item to add in list:")
    a.append(x)

y =input("Enter value whose frequency wants to count:")
f= a.count(y)
print(a,f)'''
#index
'''a =["ram","seeta","ram","geeta"]
y=a.index("geeta")
print(y)'''

'''a =[]
for i in range(5):
    x =input("Enter list which you wants to add:")
    a.append(x)
y =input("enter value which you wants to find index value:")
f =a.index(y)
print(a,f)'''
#count

'''a =[]
for i in range(5):
    x =input("Enter list which you wants to add:")
    a.append(x)
y =input("Enter value which you wants to insert: ")
f =a.insert(3,y)
print(a,f)
'''
'''num =int(input("Enter number:"))
count =0
while (num>0):
    count = count+1
    num =num//10
print(count)'''

'''num =int(input("Enter number:"))
count=0
for i in range(1,num+1):
    if num %i == 0:
        count=count+1
    i=i-1
if count==2:
    print("prime number",num)
else:
    print("not prime number",num)
'''

'''i =int(input("Enter number:"))
fac=1
while i>0:
    fac =fac*i
    i=i-1
print(fac)'''

num =int(input("Enter number:"))
x =0
y=1
z=0
sum =0
while num>0:
    sum=sum +














