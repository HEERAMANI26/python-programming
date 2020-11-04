'''s="aabcddeeffggrr"
my_dict={i:s.count(i) for i in s}
print(my_dict)

s=input("enter some string from user:")
for i in range(0,len(s),3):
    print(s[i:i+3])


s=input("enter some string:")
l=[]
for i in s:
    if i in "aeiou":
        l.append(i)


print(l)
p={i:l.count(i) for i in l}
print(p)


s=["alok","suman","saurabh","gaurav","alok","suman","alok"]
p=[]
for i in s:
    if i not in p:
        p.append(i)
print(p)
my_dict={i:s.count(i) for i in s}
print(my_dict)

l=[1,2,3,4,5]
count=0
for i in l:
    count=count+i
print(count)


n=input("enter some string:")
r=n[::-1]
if n==r:
    print("this is palinmdrome")
else:
    print("not palimdrome")


n=input("enter some string:")
i=len(n)-1
l=[]
while i>=0:
    print(n[i])
    if i not in l:
        l.append(n[i])
    i=i-1
print(l)
j=" ".join(l)
print(j)


l=[1,2,3,1,2,3,4,5]
my_dict={i:l.count(i) for i in l}
print(my_dict)



n=int(input("enter some values"))
l=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10

if sum==l:
    print("armstrong number:")
else:
    print("not armstrong number:")

'''

l=[1,2,3,4,5,6]
i=len(l)-1
l1=[]
while i>=0:
    print(l[i])
    if i not in l1:
        l1.append(l[i])
        i=i-1
print(l1 )


