
'''
opps :---------->
class:-class is a blue print of an object------>
object:--object intance of class------------->

properties of an object-----
variable :---1.
  intance variable
  static variable/class variable
  local variable

bahaviours/action of an object:--2.
    mathods:--
        intance mathod
        class mathod
        static mathod  
        self-current class ka current object ka address hold karega --------------------------->
        self is refrence variable the hodl is current class and 
Intance of intance variable
declertion of intance varible--------->        
1.in-side class:-------
      a.thought constructor
      b.thought intance mathod
2. outside class
      a.thought object

calling of intance varible:------------------>
1.in-side class
     a.used self
     b.instance mathord
2. out-side class
  a.use object                 

'''
# class  student:
#       "student information"
#       name="neeraj"
#       age=37
    

#       def add(a,b):
#           return a+b
#print(dir(student))   
#print(student,'__doc__')   
#print(student,'__dict__')   

# obj=student
# print(obj.name)
# print(obj.age)
# x=obj.add(5,6)
# print(x)

'''class  student:
      "student information"
      def __init__(self,name,age):
           self.name=name
           self.age=age
      def show_detail(self):
            print(self.name)
            print(self.age)
obj=student("neeraj",37)
obj.show_detail()
obj1=student("rahul",35)
obj1.show_detail()'''

#inside class decleartion and colling-------------->
class student:
      def __init__(self,name,age):
                self.name=name
                self.age=age       #declaration
                print(self.name)

      def     add(self,school):
              self.school=school    #declaration
              print(self.name)
      def show_detail(self):
              print(self.name)   #calling
              print(self.age)      #colling
              print(self.school)   #colling
              print(self.city)
obj=student("neeraj",37)
obj.add("shsc")
print(obj.name)   #calling
obj.city="bhopal"
obj.show_detail()               























