
'''lis=[23,45,6,7,88]
# append---> 
print(lis)
lis.append(10)
print(lis)'''

#lis.append(["mango","banana"])
#lis.append("200/kg","50/dozen")
#print(lis)
#print(lis[6])
#print(lis[6][0])

#lis=[["mango","banana"],["200/kg","50/kg"],["satna","BHopal"]]
#lis [0].append("apple")
#lis[1].append("80/kg")
#lis[2].append("itarsi")
#print(lis)

#extend  lis.extend(squence)------------------>
#lis.extend(45)
#lis=["mango","banana","apple"]
#print(lis)

#lis.extend(["pinapple","orange"])
#print(lis)


#insert(index,element)
'''lis=["mango","banana","apple"]
print(lis)

lis.insert(1,"pineapple")
lis.insert(0,"khajure")
print(lis)


lis=["mango","banana","apple"]
print(lis)
# len(), max(), min(),sum()

lis1=[23,4,-5,6,77]
m=max(lis1)
print(m)  #77

m=max(lis)
print(m) #77 '''

#num =[2,43,45,56,7,8,9,-33,44]
#fruit=["apple","banana", "orange", "mango", "90"]

#Max
#a=max(fruit)
#print(a)

# mini
#a=min(fruit)
#print(a)

#sum
#a=sum(num)
#print(a)

#num =[2,43,45,56,7,8,9,-33,44]
#index, index(element, start,end)
#a=num.index(45)

#a=num.index(45,0,5)
#print(a)

#num =[2,43,78,56,7,8,9,-33,44,5,6,45,5,6]
#a=num.index(45,0)
#print(a)


'''nums =[2,43,78,45,7,8,9,45,44,45,5,6,45,5,6]
a=nums.index(45,0)
print(a)#3
b=nums.index(45,a+1)
print(b)
c=nums.index(45,b+1)
print(c)
d=nums.index(45,c+1)
print(d) '''

'''nums =[2,43,78,45,7,8,9,45,44,45,5,6,45,5,6]
  #count ----> return frequency
#a=nums.count(2)

nums.sort()
print(nums) '''

#       0 1  2     3     4  5  6   7     8  9 10
lis1=[12,3,44, 'danish',56,7,88,'ankur',33,4,5]
#    -11 -10 -9   -8    -7 -6 -5   -4    -3 -2 -1
a=lis1[7:2:-1]
print(a)
# a=lis1[-4:-9:-1]
# print(a)
# a= lis1[::-1]
# print(a)
# ######################################

# Topic:---slicing mathord--------->
lis2="we are here to learn python.and sliching is very helpful"
a=lis2[7:20]
print(a) # list ke under first value deleat kar deta hai and second value uski length hotee hai

a=lis2[32:]      
print(a)   # list mein starting se 32 number tak ke word ko kat kar deta hai and baki ko chodd deta hai

a=lis2[32]
print(a)  # list mein paticuler number starting se count karke 32 number wale letter ko kat kar deta hai--->

a=lis2[::-1]
print(a) # list main add all words ko reverse kar detaa hai----->

a=lis2[:21]
print(a)  #list mein starting se count karta hai 21 starting ki string ko print kar deta hai baaki ko kat kar deta hai 

a=lis2[21]
print(a) #list mein particuler word ko print karta hai 21main----

print(lis2[3:19:3])

print(lis2[:21] +" cpp "+lis2) # concaninate karta hai means
                                             #list main particuler point ke baad word ko jodd deta hai

# Topic Tupple-------------------------------------------------------------------------->

'''frurit=("apple", 20,100)
print(type(frurit))
#frurit[2]=200 #tuple immutable
print(id(frurit))
print(id(frurit[0]),id(frurit[1]),id(frurit[2]))'''

'''frurit=("apple", 20,100)
frurit=("apple",20,100)+("banana",999)
print(frurit)'''

'''number=(12,99)+(78,90)
number=number+(89,90)

print(number) #(12,99,78,90,89,90)
    #           0                  1
lis=[["ajay","aman"], (45,67)]
#        0         1           0   1
print(type(lis[1]))
#lis[1][0]=99----------> error (tuple)
lis.pop()
print(lis)

t=(34,55,[3,4,555])
print(t)
t[2][1]=999
print(t) 

lis=[["ajay","aman"],(45,[76,44])]
lis[1][1][0]=999
print(lis)

lis[1][1][1]=55
print(lis) '''


#tuple function-------------------------------------------------------->
'''
len(), max(), min(),sum(), index(),count()
'''

'''t=(9,44,5,3,9)
a=t.count(9)
print(a)
# sorted()------return 
t=(9,44,5,9,3,9)
a=t.sorted(t)
print(a) '''

'''t=(23,)
print(type(t))  #tuple-------------

t1=("abcd")  #tuple mein agar single value hai to vaha comma lagana hai   
print(type(t1))

t=(23)
print(type(t))     

t2=1,2,3,4,5
print(type(t2))     #using function ayega   tuple-----------

# empty tuple.
t=()
#
t1=tuple()
print(t,t1) '''

'''record=("ajay", 101, 23, 9090344567)
record=list(record)
record[3]=92345678923
print(record)
record=tuple(record)
print(record)

a=9
b=7
a,b=100, 900 
print()'''                     #list , set , disnaray mutable--------------->

# Topic string--------------------> immutable data type positve negative slising are possible

#msg="string is a immutable data-type"
#print(msg[12:21])
#msg[3]="y"


'''msg="apple is good 4 health"
# capitalize()
a=msg.capitalize()
print(a)
# upper()
b=msg.upper()
print(b)
# lower()
c=msg.lower()
print(c)
msg="APPLE IS"
# isupper()----> return boolean output
a=msg.isupper()
print(a)

msg="APpLE IS"
a=msg.isupper()
print(a)'''

'''msg="aaa a bb"
a=msg.isupper()
print(a)
b=msg.islower()
print(b)
msg="a123453" # slove karna hai 

# isdigit()------------->
msg="Aaa Babb" 
b=msg.isalpha()
print(b)

msg="AaaBabb" 
b=msg.isalpha()
print(b)
msg2="123453 455664"
b=msg.isdigit()
print(b) '''

# replace(old value, new_value)
'''s="we are here to learn c++, it is a high level lang"
s1=s.replace("c++", "python")
print(s1)
s2=s.replace("a", "b",2)
print(s2)
s3=s.replace(s,"new")
print(s3)

# split() function return list karta hai--------------------------> return list katna hua 
s="we are here to learn c++, it is a high level lang"
s1=s.split()
print(s1)
s1=s.split('a')
print(s1)
s2=s.split("here")
print(s2)
s2=s.split("here",1)# here ko ek baar hi katega
print(s2)

#join() function--------------------->return string
lis=["apple","banana", "pineaple", "orange"]
lis2=["pppp","qqqqqq"]
s=" ".join(lis)
print(s)
s=", ".join(lis)
print(s)
s=", ".join(lis) +" , "+ "  ,".join(lis2)
print(s)'''

'''s1="its now or never"  # reverse string----------->
#s1="sti.won.ro.reven"
s=s1.split()
print(s)
a=s[0][::-1]  #slice mathord------>
b=s[1][::-1]
c=s[2][::-1]
d=s[3][::-1]
s=[a,b,c,d]
print(s) '''


# replace (old,new)-----> return string
s="apple" "Banana"
'''a=s[5:]  # list mein index 5 tak count karta hai [5:] : aage ki word/number ko print karta hai-->
a=s[:5]  #list mein index 5 tak count ksrta hai [:5]  : piche ki  word/number ko print kata hai-->
print(a)
b=s[::-1] #list ke undar string ko reverse karta hai
print(b)'''
c=s[6:]+" "+s[:5]
print(c)

#disnaray mutable datatype 
'''d={"one":"monday","two": "tuesday","three":"wednesday","one":"jan"}
print(d)

d={"one":"monday","two":"thusday","three":"wednesday", "one":"fevb"}
d["one"]="friday" #disnarey nwe data ko assien kar sakte hai--->
d.update({"four": "march"})#disnaray mein naw data ko insert karta hai----> 
d1={"five":"jaily"}#disnaray mein naw data ko insert karta hai----> 
d.update(d1)
print(d)'''


#print(d["two"])
'''d["four"]="thursday"
d["five"]="friday"
d["one"]="friday"
d.update({"six":"saturday"})
d1={"saven":"sunday"}
d.update(d1)
print(d)'''















































































































































