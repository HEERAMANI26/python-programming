'''l="We are at Ignite Solutions! Their email-id is careers@ignitesol.com"
p=l.split()
l1=[]
for i in p:
    if i not in l1:
        l1.append(i[::-1])
print(l1)

j=" ".join(l1)
print(j)'''
'''l="We are at Ignite Solutions! Their email-id is careers@ignitesol.com"
p=l.split()
l1=[]
i=len(p)-1
while  i>=0:
    if i not in l1:
        l1.append(p[i][::-1])
        i=i-1
print(l1)

l='one', 'two', 'three',' four', 'five', 'six'
p=list(l)
print(p)
l1=[]
i=0
while i<len(p):
    if i%2==0:
        l1.append(p[i])
    else:
        l1.append(p[i][::-1])
    i=i+1
print(l1)

s="abcdefghijk"
print(s.find('efg'))

sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

sampleList.pop(2)
print(sampleList)
aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [2 * x for x in aList]
print(pow2)
listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']
newList = listOne + listTwo
print(newList)
aList = ['a', 'b', 'c', 'd']

newList = aList.copy()
print(newList)
resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)
list1 = ['xyz', 'zara', 'PYnative']
print (max(list1))

sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])

l = [None] * 10
print(len(l))

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

aList = [5, 10, 15, 25]
print(aList[::-2])

sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])

sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)

First_List =[10, 20, 23, 11, 17]
Second_List =[13, 43, 24, 36, 12]
my_list=[]
for x in First_List:
    if x%2!=0:
        my_list.append(x)

for x in Second_List:

    if x%2==0:

        my_list.append(x)
print(my_list)

str1 = "P@#yn26at^&i5ve"
char_count=0
digit_count=0
symbol_count=0
for i in str1:
    if i.islower() or i.isupper():
        char_count+=1
    elif i.isdigit():
        digit_count+=1
    else:
        symbol_count+=1
print(char_count)
print(digit_count)
print(symbol_count)



list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
my_list=[i+j for i,j in zip(list1,list2)]
print(my_list)

aList = [1, 2, 3, 4, 5, 6, 7]
my_list=[x**2 for x in aList]
print(my_list)
my_dict={i:i*i for i in aList}
print(my_dict)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
my_list=[x+y for x in list1 for y in list2]
print(my_list)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
print(list1[2][1][2].extend(['h','i','j']))
list1 = [5, 10, 15, 20, 25, 50, 20]
list1[3]=200
print(list1)
list1.replace(20,200)
print(list1)

list1 =[5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if i==20:
        continue
    print(i)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict=dict(zip(keys,values))
print(my_dict)
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
my_dict3={**dict1, **dict2}
print(my_dict3)


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
d=sampleDict.replace("city","location")
print(d)

aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
list1=list(aTuple)
print(list1[1][1])
t=(50,)

aTuple = (10, 20, 30, 40)
a,b,c,d=aTuple
print(a)
print(b)

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1,tuple2=tuple2,tuple1
print(tuple1)
print(tuple2)

tuple1 = (11, 22, 33, 44, 55, 66)
list1=list(tuple1)
l=[]
for i in list1:
    if i==list1[3] and i==list1[4]:
        l.append(i)
print(l)
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:5]
print(tuple2)

str1 = "JhonDipPeta"
for i in range(len(str1)-1,4):
    print(i[3:6])
str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count(sub,4))
str1 = "My salary is 7000";
str2 = "7000"

print(str1.isdigit())
print(str2.isdigit())

str = "My salary is 7000";
print(str.isalnum())

strOne = str("pynative")
strTwo = "pynative"
print(strOne == strTwo)
print(strOne is strTwo)

print("John" > "Jhon")
print("Emma" < "Emm")

myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString)
print(stringList[1] is myString)

str1 = 'Welcome'
print (str1[:6] + ' PYnative')

str1 = "PYnative"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

aTuple = (100,)
print(aTuple * 2)

aTuple = (100, 200, 300, 400, 500)
aTuple.pop(2)
print(aTuple)

aTuple = ("Orange")
print(type(aTuple))

tuple1 = (1120, 'a')
print(max(tuple1))

aTuple = (100, 200, 300, 400, 500)
aTuple[1] = 800
print(aTuple)
'''
aTuple = (100, 200, 300, 400, 500)
print(aTuple[-2])
print(aTuple[-4:-1])

dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)


list=[10,20,30,40,50]
for index,element in enumerate(list):
    print("index",index,"element",element)


currentEmployee={1: 'Scott', 2: "Eric", 3:"Kelly"}
formerEmployee={2: 'Eric', 4: "Emma"}
d={**currentEmployee,**formerEmployee}
print(d)

ItemId = [54, 65, 76]
names = ["Hard Disk", "Laptop", "RAM"]
print(dict(zip(names,ItemId)))

list1=[10,20,30,40,50,60,70,80]
list2=[20,30,40,50]
list3=Diff(list1, list2)
print(list3)