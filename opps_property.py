
'''
property
1) inheritance -----> parent,child relat
'''
   #Single Level Inhaitance-------------------->init hi consector hotaa hai------------>
'''class P:
     def __init__(self,p_name):
          self.x=p_name

     def p_properties (self,home,bank):
          self.h=home
          self.b=bank

class C(P):
     def c_prpperty(self,qualification):
          self.q=qualification
          print(self.x)
          print(self.h)
          print(self.b)
          print(self.q)
                    
obj=C("Neeraj")
obj.p_properties("Bhopal","Sbi")
obj.c_prpperty("M.Tech")'''


'''class sedan:
      def car_collection(self,hyundai,skoda):
          self.h=hyundai
          self.s=skoda

      def hachback(self,tata,mahindra):
          self.t=tata
          self.m=mahindra

class plane(sedan):
        def p_company(self,plane_name,dastination):
          self.p_n=plane_name
          self.d=dastination
          print(self.p_n)
          print(self.d)
          print(self.t)
          print(self.m)
          print(self.h)
          print(self.s)
obj=plane()
obj.car_collection("verna","silavia")
obj.hachback("crata","xuv700")
obj.p_company("indego", "america")'''


#Multi Level Inharitance-------------------------->
'''class Gf:
    def name(self,name):
        self.n1=name
class P(Gf):
    def __init__(self,P_name):
        self.x=P_name
    def p_properties(self,name,bank):
        self.n=name
        self.b=bank

class C(P):
    def c_property(self,qualification):
        self.q=qualification
        print(self.x)
        self.p_properties("Indore","SBI")
        print(self.n)
        print(self.b)
        
        print(self.q)
        self.name("Dada")
        print(self.n1)
obj=C("Neeraj") 
#obj.p_properties('bhopal','hdfc')
obj.c_property('B-Tech')'''

#Multiple Inharitance-------------------------->

'''class Father:
     def property(self,f_name,f_bank):
          self.n1="f_name"
          self.b="f_bank"
          print(self.n1)
          print(self.b)

class Mather:
     def property1(self,m_name,m_bank):
               self.n1="m_name"
               self.b="m_bank"
               print(self.n1)
               print(self.b)

class Son(Father,Mather):
      pass

obj=Son()
obj.property("rahul","sbi")
obj.property1("raj","sci")'''

'''class Father:
      def property(self,f_name, f_bank):
              self.n1=f_name
              self.b= f_bank
              print(self.n1)
              print(self.b)

class Mother:
       def property1(self,m_name,m_bank):
               self.n1=m_name
               self.b=m_bank
               print(self.n1)
               print(self.b)

class Son(Father,Mother):
         pass

obj=Son()
obj.property("raj","sbi")
obj.property1("meena","pnb")'''

#hybrid inharitance------------------->
'''class A:

class B(A):

class C:

class D(B,C)

class E(D):'''

# Hybrid Inharitance-------------------------------------------------->
class Bike:
      def company(self,hero,honda):
            self.h="hero"
            self.h1="honda"
            print(self.h)
            print(self.h1)

class Car(Bike):
         def company1(self,suzki,mahindra):
               self.s="suzki"
               self.m="mahindra"
               print(self.s)
               print(self.m)

class Bus:
       def company3(self,tata,eicher):
             self.t="tata"
             self.m="eicher"
             print(self.t)
             print(self.m)

class Plane(Car,Bus):
     def company4(self,indego,qatar):
            self.i="indego"
            self.q="qatar"
            print(self.i)
            print(self.q)

class Countary(Plane):
       def company5(self,india,england):
              self.i="india"
              self.e="england"
              print(self.i)
              print(self.e)

obj=Countary()
obj.company("splender","cd")
obj.company1("ciaz","thar")
obj.company3("gf","jh")
obj.company4("dr","fg")
obj.company5("se","sd")

            
                     















#Mathord overloding----------------------------------->
#polymorphisham same =function with different argument
#overloding ko avoid karne ke liye hum sing * ka use karte hai------


# overloding ------------------------->   
'''class A:
      def add(self,x,y):
           return x+y

      def add(self, x,y,z):
          return x+y+z

obj=A()
#obj.add(10,20,7)                         
x=obj.add(2,4,6)
print(x)'''

'''class A:
      def add(self,*n):
            sum=0
            for i in n:
                  sum=sum+i
            return sum

obj=A()
x=obj.add(10,20)
print(x)
y=obj.add(10,2,5)
print(y)''' 
   
























