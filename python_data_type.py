'''a = {1,2,3,4,5}
print(type(a))
b = {1,6,7}
a.difference(b)
print(a)
a.difference_update(b)
print(a)
a.union(b)
set1={"apple","orange","banana"}
set1.update("pineapple")
print(set1)
set1.update("ram")
set1=[1,3,4,5,6,7]
print(list1[1:3])
print(list1[2:4])
print(list1[ :-2])
print(list1[1:])'''
####
'''ch = input("Enter alphabet:")
if (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u") :
    print("This is vowel:", ch)
else:
    print("this is consonants", ch)

'''
###
'''ch = input("Enter any alphabet or numerics and symbolics :")
if (ch >= "a" and ch <="z") or (ch >="A" and ch <= "Z"):
    print("this is alphabet", ch)
elif (ch >= "0" and  ch <= "9"):
    print("this is numaric value", ch)
else:
    print("this is symbolics value", ch)'''

'''num = int(input("Enter two digit no:"))
if (num >=0 and num <= 9):
    print("one digit number:",num)
elif (num > 9 and num<= 99):
    print("two digit no")
elif (num >= 99 and num <= 999):
    print("three digit", num)
else:
    print("four digit no", num)'''
#################
'''f = input("Enter any alphabet:")
if (f.isupper())== True:
    print("this is upper case leter")
else:
    print("this is lower case", f)'''

'''string =input("enter any sentence:")
newstring =" "
count1 = 0
count2 = 0
count3 = 0
for a in string:
    if (a.isupper()) == True:
        count1+=1
        newstring+=(a.lower())
    elif(a.islower()) == True:
        count2+=1
        newstring+=(a.upper())
    elif(a.isspace()) == True:
        count3+=1
        newstring+=a


print("In original String : ")
print("Uppercase -", count1)
print("Lowercase -", count2)
print("Spaces -", count3)
print("After changing cases:")
print(newstring)'''

##########################################

'''a = input("Enter sides of first:")
b = input("Enter side of second:")
c = input("Enter side of third:")
if ((a + b > c) and  (b+c > a) and  (a+c > b)):
    print("valid side of triangle",a,b,c)
else:
    print("invalid side of triangle")'''

'''a = input("Enter side of triangle:")
b = input("enter side of triangle:")
c = input("enter side of triangle:")
if a == b ==c:
    print("this is an equilateral triangle", a,b,c)
    +
elif a == b or a==c or c==b:
    print("this is isolateral triangle:",a,b,c)
else:
    print("this is scalable triangle:",a,b,c)'''


'''num = int(input("enter any number:"))
def factorial(num):
    if num == 1:
         return num
    else:
        return  num * factorial(num-1)
if num <= 0:
    print("negative number is not allowed:",num)

else:
    print("factorial of: ", num, "is:", factorial(num))'''

'''num = int(input("Enter any number:"))
if (num %2 == 0):
    print("this is an even number",num)
else:
    print("this is an odd num:", num)'''

'''num1 = float(input(" Please Enter the Actual Product Price: "))
num2 = float(input(" Please Enter the Sales Amount: "))
amount = ""
if (num1 > num2):
    amount = num1 - num2
    print("Total Loss Amount " , amount)
elif (num2 - num1):
    amount = num2 - num1
    print("Total Profit ",amount)
else:
    print("No Profit No Loss!!!")'''

#average related problem

print("All students marks:")
a = int(input("math marks:"))
b = int(input("sci marks:"))
c = int(input("bio marks:"))
d = int(input("social sci marks:"))
total = a+b+c+d
print("total is:", total)
per = float(total) * (100/400)
print("percentage is:", per)
if per >= 95:
    print("Grade A+")
elif per >=90:
    print(" Grade A")
elif per >= 80:
    print("Grade B+")
elif per >= 70:
    print("Grade B")
elif per >=60:
    print("Grade C+")
elif per >=50:
    print("Grade C")
elif per >=40:
    print("Grade D")
elif per >=30:
    print("Grade F ")







































