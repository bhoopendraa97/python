# input operration---------->

#number1=int (input("enter 1st number:")) 
#number2=  int (input("enter 2st number:"))

#print("Add",number1+number2)

#name=input("enter name")
#surname=input("enter surname")

#print("Add", name + surname)

name="shubham"
age=25
address="bhopal"

st_detail =[name,age,address]  # list [] --------representation
print(type(name))
print(type(age))
print(type(address))
print(type(st_detail))

st_detail=[name, age, address]
print (st_detail[0])
print(st_detail[2])
print(st_detail[1])

print (st_detail[-3])
print(st_detail[-2])
print(st_detail[-1])

st_detail_1=[name,age,address]
st_detail_2=["ajay", 34, "ujjain"]

print(st_detail_2)
st_detail_2[2]="indore"
print(st_detail_2)

print(st_detail_2)
st_detail_2[-1]="chhatarpur"
print(st_detail_2)
st_detail_2[-2]=55
print(st_detail_2)

#tuple--------------------------------->
st_detail_1=(name,age,address)
st_detail_2=("ajay", 34, "ujjain")

#emty list
#1
list=[]
#2
li=list()#
print(list)
print(li)
#print(lis)
#print(any(lis)) #False
lis=[56]
print(any(lis)) #True

lis=[23,45,6,7,88]
# append----->
print(lis)
lis.append(10)
print(lis)
























