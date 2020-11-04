'''import copy
l1=[10,20,[30,40],50]
l2=copy.copy(l1)
l2[2][1]="alok"
print(l2)
print(l1)
##############################333
l1[0]=999
print(l1)
print(l2)
####################
l2[2][1]="heera"
print(l1)
print(l2)
#deepcopy
l1=[1,2,3,[4,5],6]
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l1[3][0]="musskan"

print(l2)
print(l1)

t=(1,2,3)
p=len(t)
print(p)
print(t[2])
count=0
for i in t:
    count=count+1
print(count)
l=list(t)
print(l)
print(l[0])
l.append(7)
print(l)
t1=tuple(l)
print(t1)
my_dict={x:t.count(x) for x in t}
print(my_dict)



l=[50,60,70,(10,20,30)]
x=list(l[3])
x[1]=100
l[3]=tuple(x)
print(l)
t=(10,20,[30,40,50])
l=list(t)
l[2][2]=1000
t=tuple(l)
print(t)
l="hello world"
i=len(l)-1
p=[]
while i>=0:
    print(l[i])
    p.append(l[i])
    i=i-1
print(p)
t=''.join(p)
str=str(t)
print(str)


l=[3,2,3,4,5,6,1,3]
l.pop(1)
print(l)

l=[1,2,3,{},True,[20,30]]
print(len(l))
l="heeramani"
p=l[::-3]
print(p)
print (type(type(int)))



s="my name is heera i belong to pune maharashtra i did my be in"
q=s.split()
my_dict={x:q.count(x) for x in q}
print(my_dict)


my_dict={x:x**2 for x in [1,2,3,4,5,6]}
print(my_dict)


l=[1,2,3,4,5,6,6,4,8,2]
my_dict=[i for i in l if i%2==0]
print(my_dict)
my_dict=set([i for i in l if l.count(i)>1])
print(my_dict)

def cube(y):
    return y*y*y

print(cube(5))
a=10
x=lambda i:i**3
print(x(2))


x=list(filter(lambda i:(i%2!=0),l))
print(x)
x=list(map(lambda i:(i**2),l))
print(x)
x=list(filter(lambda i:(i%5==0),l))

print(x)
from functools import reduce
x=reduce((lambda y,z:y+z),l)
print(x)


s="hello world"
output=""
i=len(s)-1

while i>=0:
    output=output+s[i]
    i=i-1
print(output)


s="hello world"
s1=s.split()
print(s1)
sum=[]
i=len(s1)-1
while i>=0:
    print(s1[i])
    i=i-1
print(sum)

s="Python is a general purpose high level programming language"
s1=s.split()
i=len(s1)-1
l=[]
while i>=0:
    if i not in l:
        l.append(s1[i][::-1])
        i=i-1
print(l)

for ch in s1:
    if ch not in l:
        l.append(i[::-1])

print(l)  

print(l)'''

f=open("python.py","r")
#print(f.read())
f.close()
print(f.closed)
#print(f.readline())
#print(f.readlines())
with open("python.py","r") as f:
    
    p=f.readlines()
    print(p)




