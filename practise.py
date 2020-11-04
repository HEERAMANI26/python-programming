#n =int(input("Enter number which you wants to inserted:"))
'''a=[]

for i in range(5):
    x =int(input("Enter list which you wants to add:"))
    a.append(x)
    y=len(a)
avg=sum(a)/y
print(avg)'''

#lambda
'''x=lambda x,y,z:x*y*z
print(x(2,4,6))
x=lambda a,b:a+b
print(x(5,2))
x=lambda x,y:x**y
print(x(2,2))
a=20   #GLOBAL VARIABLE
def f1():
    global a
    a=10#LOCAL VARIABLE
    print(10)
def f2():#IF LOCAL VARIABLE WILL NOT AVAILABLE THAN CALLED GLOBAL VARIABLE
    print(a)
f1()
f2()'''
#convert digit to words
'''n =input("Enter number in words:")
if n =="zero" :
    print("0")
elif n =="one":
    print("1")
elif n =="two":
    print("2")
elif n =="three":
    print("3")
elif n =="four":
    print("4")
elif n=="five":
    print("5")
elif n =="six":
    print("6")
elif n=="seven":
    print("7")
elif n =="eight":
    print("8")
elif n=="nine":
    print("9")
else:
    print("plz enter digit only 0 to 9")

list =["zero","one","two","three","four","five","six","seven","eight","nine"]
n =int(input("Enter number from 0 to 1:"))
print(list[n])
n =input("Enter in words:")
list =[0,1,2,3,4,5,6,7,8,9]
print(list[n])

num =int(input("Enter number:"))
a=num
sum=0
while (num >0):
    sum = sum +(num%10)*(num%10)*(num%10)
    num = num//10
if a == sum:
    print("armstrong number",num)
else:
    print("not armstrong number")'''

'''lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    a = num
    while num > 0:
        sum =sum+(num%10)**4
        num =num//10

    if a == sum:
        print(a)'''

'''for i in range(1,6):
    for j in range(1,i+1):
     print(i,end="")
    print("\n")'''

l1 =[1,2,3,4,5,6,7,8,9,10]
l2 =[5,6,7,8,9,10,11]
l3 =list(map(lambda x,y:x*y,l1,l2))
print(l3)

l3 =list(map(lambda x,y:x-y,l1,l2))
print(l3)
l3 =list(map(lambda x:x*2,l1))
print(l3)





