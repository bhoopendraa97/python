print ("welcome")
print("hello world")
print ("welcome to the world of python ")
print ("we are python devloper")

print ("Hello world")

#end parameter
# print ("welcome",end=" $ ")

print("to", end=" $ ")
print("python classes")
# sep parameter -----asign  string
print ("welcome", "to", "python", sep="$")

print ("welcome", "to", "python", sep=" ")
#to defiend block in puthon we use indent
#it is equivelent to {} in c++,
#python ----> indent

print ("left most corner\n")
print ("aaaaaaaa")
if True:
    print("if body")

#print("left more corner hchdfjkdhckkhvcvkhcxcj\hsdfdfd\
#jshfjskfsahhklsd\
#kkkdkhdldfldgjldlljkkhkskgkd")
# tarike alag alag hai
 
#print("left more corner hchdfjkdhckkhvcvkhcxcj\hsdfdfd"
#"jshfjskfsahhklsd"
#"kkkdkhdldfldgjldlljkkhkskgkd")

#     Topic:--  smalle             Tokans 
#print("welcome")   # 3  tocan

#import  keyword
#print(keyword.kwlist)
#print ("count", len (keyword.kwlist))


print ("welcome") #  3token

print(24%5)
print(5%24)
# Arthmatic operator------------------------------>
# Modulus---------------->
print(23%4)
# (//) floor division operator---------->
print(23/4)
print(23//4)
print(60//7)
print(60//6)
#exoponition operator------------->
print(4**5)  #4*4*4*4*4=1024 answer
#(Base) (power)
# Q2) comparsion operator------------------------>
print(23>45)
print(23>=45)
print(23<=45)
print(23!=45)
print(23==45)
# string comparision-------------
# basis of ASCI (American standerd code for Infomation Interchange)
#In lexicographical manner
print("apple" > "banana")  # A=65,a=97, 0=48 askvalue---------
#   a=   97    >    98  b=98

print("come" > "done")
print("oranGe" < "orange")
print("ABCD" < "ABC")  
# and operator------------>
print(True and True)
print(3>2 and 34<5)
# or operator--------------->
print(3>2 or 34<5)

#not operator------------>
print(not(24>56))
#mebership operator-------------->
# in operator----------------------->
string1="apple  is good 4 health"
print("is" in string1)
print("si" in string1)
print("apple   is" in string1)
print("health " in string1)
#not in---------------------------->
print("health " not in string1)#T
#identity oprerator -------------------->
#is operator gives True when we test for same object
#otherwise False


#Topic-------------------->
#varibles/refrence  and Data type in python------------>
num1=90
num2=100
num3=90
num1=900
print(id(num1))
print(id(num2))
print(id(num3))

number1=100
number2=200
number3=100
print(id(number1), id(number2), id(number3))
#print (number 1/2)
number1=98
print(id(number1), id(number2), id(number3))
number3=567    #gc garbase collector------->

name=input("enter name")
surname=input("enter surname")

print("Add", name+  "  "+  surname ) 

lis=[23,45,6,7,88]
# append----->
print(lis)
lis.append(10)
print(lis)


