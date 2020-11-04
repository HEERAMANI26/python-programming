dict = {1:'heera',2:'alok',3:'abhi', 4:'manoj'}
print(dict)
print(dict[1])
print(dict[4])
print(dict[2])
print(dict.get(1))
print(dict.get(5,'monika'))
print(dict.get(8,'not found'))

'''keys =['heera','alok','prem']
values = [25,32,21]
data = dict(zip(keys,values))
print(data)'''

k1 ={'alok':32,'heera':26,'manoj':30,'rahul':['python','java','js'],'manshi':{'mehul':57,'govind':5}}
print(k1['alok'])
print(k1["manshi"])
print(k1['rahul'])
print(k1['rahul'][2])
print(k1["manshi"]['mehul'])
print(k1['manshi']['govind'])

#k2 =24 & 25
#print(~k2)
import math
x = 5.8
print(math.floor(x))
print(math.ceil(x))
x = 25
print(math.sqrt(x))
print(math.pow(5,2))
print(math.pow(9,2))
print(math.pow(7,3))
import math as m
print(m.sqrt(9))

#for i in range(11,21,2):
  #  print(i)
for i in range(15,20):
    if(i % 5!=0):
     print(i)


num = int(input("Enter any number"))
for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break
else:
        print("prime no")



