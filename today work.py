'''lower =int(input("Enter lower range:"))
upper =int(input("Enter higher range:"))
for num in range(lower,upper+1):
    sum =0
    a =num
    while num >0:
        sum =sum+(num%10)**4
        num =num//10
    if a==sum:
        print(a)
# slicing
s ="durgasoftsolution"
print(s[1:4])
print(s[4:6])
print(s[1:])
print(s[:5])
print(s[1:-1])
print(s[4:-2])
print(s[:-2])
print(s[1:100])
print(s[1:100:2])
print(s[1:2:2])
print(s*2)
print(int(True))
print(int(False))
print(int(12.123))
print(int(10+20j))
print(complex(10))
print(complex(True))
print(complex(False))
print(int("10"))
print(int("10.05"))
x =[10,20,30,40,50,60]
print(bytes(x))
print(bytearray(x))
list =["durga",10,"true"]
print(list*2)
print(list)
print(type(list))
#tuple
t=("durga",10,"true")
print(type(t))
print(t[1:3])
print(t[1:5])
print(t[-1])
print(t[0:3])
print(t[:-1])
print(t*2)
r=range(10)
print(type(r))
s ={10,20,30,10,20,30}
print(s)
print(s[0])
print(s[1:])

lower =int(input("enter 1st number:"))
upper =int(input("enter 2nd number:"))

for num in range(lower,upper+1):
    rev =0
    a = num
    while num>0:
        rev =rev*10+(num%10)
        num = num//10
    if a == rev:
       print(a)
a =[1,2,3,4,5,6]
y =[ i for i in a if i%2 ==0]
print(y)
num1 =int(input("Enter number:"))
num2 =int(input("Enter 2nd number:"))
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
print("The L.C.M. is", compute_lcm(num1, num2)
list =[1,2,3,4,5,6]
h =iter(list)
for i in h:
    print(i)

lst =[1,2,3,4,5,6,7,8]
y =list(filter(lambda x: (x%2==0), lst))
print(y)

lst =[1,5,9,11,7,19]
y =list(map(lambda x:x**3,lst))
print(y)
lst =[4,6,8,12,10,18,20]
y=list(filter(lambda x: (x%2 == 0),lst))
print(y)
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: ((x%2 ==0) or (x%3 ==0)) , li))
print(final_list)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)


from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)

rows =int(input("Enter number of rows:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

n =int(input("Enter number of rows:"))
for i in range(n,1):
    for j in range(i,1):
        print("*",end="")
    print()
n =int(input("Enter number:"))
fac=1
for i in range(1,n+1):
    fac =fac*i
    i=+1
    
print(fac)

n =int(input("Enter number:"))
fac=1
while n>0:
    fac=fac*n
    n=n-1
print(fac)


p=[5,10,20,30,40,0,11,5,0,4,0]
for i in p:
  if i==0:
      print("pagal ho gya hain kya......how divide zero")
      continue
  print("100/{}={}".format(i,100/i))

p=[10,5,6,2,0,7,5,9]
for i in p:
    if i==0:
        print("how can divide zero...pagal ho gya kya....")
        break
    print("100/{}={}".format(i,100/i))
    
    
n =int(input("Enter any number which you want to check prime number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
    i=i+1
if count==2:
    print("prime number")
else:
    print("not prime number")
n =int(input("Enter number which you want to check prime:"))
count=0
i=1
while i<=n:
    if n%i==0:
        count =count+1
    i =i+1
if count==2:
    print("prime number")
else:
    print("not prime number")'''

'''s =input("Enter string:")
n=len(s)
i=n-1
while i>=0:
       print(s[i],end="")
       i=i-1
s=input("Enter string value:")
n=len(s)
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1
#membership operator
s =input("Enter string:")
print("d"in s)

s1 =input("Enter 1st string:")
s2 =input("enter 2nd  string:")
if s1 == s2:
    print("both string are equal")
elif s1 < s2:
    print("s1 smaller than s2 string")
else:
    print("s1 is bigger than s2 string")


l1=["A","B"]
l2=["A","B"]
l3=l2
print(l2 is l3)

print(id(l1))
print(id(l2))
print(l1 is l2)
print(l1==l2)


#count method
s ="aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbsssssssssssssssssssssssyyyyyyyyyyy"
print(s.count("a"))
print(s.count("s",18,len(s)))


#replace method
s ="aaaaaaaaaaaannnnnnnnnnnnnnnnnnbbbbbbbbbbbbbbsssssssssss"
print(s)
s1=s.replace("a","m")
print(s,"address is",id(s))
print(s1,"address is",id(s1))

#splitting of string
s ="durga soft solution"
l=s.split()
print(l)
for i in s:
    print(i)

s ="20-3-2020"
l=s.rsplit('-')
print(l)
for i in s:
    print(i)


s =input("enter some string")
output=""
previous=""
for i in s:
    if i.isalpha():
        output =output+i
        prevoius =i
    else:
        output =output+previous*(int(i)-1)
print(output)'''

#add or even position of string////////////////////////////////////////////////////////////////////

s =input("Enter some string:")
i=0
print("the even position of string:")
while i<len(s):
    print(s[i],end=',')
    i =i+2
i=1
print("the odd position of string:")
while i<len(s):
    print(s[i],end=',')
    i=i+2
#alphabets or numeric position


'''s =input("Enter some string")
s1=s2=output=""
for i in s:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i
for i in sorted(s1):
    output=output+i
for i in sorted(s2):
    output=output+i
    print(output)
'''

















































