
# Q.1) given the following structure------------>
'''data=[10,[2.5, "apple"], (3,4)]
print(data[1][1])  # "apple"------------>

#Q.2)  given the following structure------------>
mixed=[[1,2],  (3.5, "grape"), [4,5,6]]
print(mixed[1][0]) # 3.5

#Q.3)  given the following structure------------>

elements=[100, (200, 300), ["a", "b", "c"]]
print(elements[2][1]) # b

#Q.4)  given the following structure------------>
data=[[10,20], (30,40, 50)]
print(data[0][0]) # 10

#Q.5)  given the following structure------------>
values=[(1.5, 2.5), [3, 4], 5]
print(values[0][1])  # 2.5

#Q.6)  given the following structure------------>
numbers=[[5, 10], (15, 20)]
print(numbers[1][1]) # 20

#Q.7)  given the following structure------------>
shapes=["circle", (5, 10), [15, 20, 25]]
print(shapes[2][0]) # 15

#Q.8)  given the following structure------------>
matrix=[[1, 2,3], [4,5,6], [7,8,9]]
print(matrix[1][2]) # 6

#Q.9)  given the following structure------------>
data=[(1,2,3), [4,5,6]]
data[0][1]=10
print(data)  # "tuple" object not support item assignment

#Q.10)  given the following structure------------>
data=[[1,2], (3.5, 4.5)]
data[1][0]=7.5
print(data) # "tuple" object not support item assignment'''

# Topic:---slicing mathord--------->

#       0 1  2     3     4  5  6   7     8  9 10
'''lis1=[12,3,44, 'danish',56,7,88,'ankur',33,4,5]
#    -11 -10 -9   -8    -7 -6 -5   -4    -3 -2 -1

a=lis1[7:] #index number 7 and 7 ke baad wale number bhi print karyega----->
print(a)

b=lis1[2:]
print(b)

c=lis1[7:2:-1]
print(c)

#a=lis1[7:2:-1]
#print(a)
# a=lis1[-4:-9:-1]
# print(a)
# a= lis1[::-1]
# print(a)'''

#dictionary

'''d={1: "mom", 2: "tue", 3: "wed"}
d.update({4:"thus"})
d[5]="fri"
print(d)'''

#
'''d={1:["ajay", 23, "bhopal"] ,2:["danish", 23, "ujjain"]}
d[2][2]="indore"
print(d)

d={1:["ajay", 23, "bhopal"] ,2:["danish", 23, "ujjain"]}
print(d)
print(d[1])
print(d[1][2])

#d.update ({2: ["ajay",23, "indore"]})
#d[2][2]="indore"
#print(d)'''


'''d1={101: {"name": "ajay", "age":23, "city": "bhopal"},102: {"name": "danish", "age":23, "city":" indore"}}
d1[102]["city"]="ujjain"
print(d1)
d1[102].update({"city": "ujjain"})
print(d1)'''

d={1: "mon",-2:"tue", 3: "wed"}
# key()
keys=sorted(d.keys()) # keys only keys deti hai----------
print(keys)
# values()
values=d.values() # value only value deta hai-----
print(type(values))

#items
items=d.items()
print(items)  #items key and value dono deta hai------typeof se data type operation use karte hai



sorted_keys=sorted(d.keys()) #
print(keys,type(keys))































