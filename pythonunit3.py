#Write a program to create a simple class with 2 methods and execute both methods
'''

class student:
    def __init__(self):
        print("this is the constroctor method")
    def instan(self):
        print("this is the instance method")
    @classmethod
    def clas(self):
        print("this is the class method")
    @staticmethod
    def func():
        print("this is the static method")
s1=student()
s1.instan()
s1.clas()
s1.func()
'''
'''
#Write a program to create a class for student with RollNo, Name, Age, Gender and methods named AddStudent() and DisplayStudent()
class student:
    def addstudent(self,rollno,name,age,gender):
        self.rollno=rollno
        self.name=name
        self.age=age
        self.gender=gender
    def displaystudent(self):
        print(self.rollno)
        print(self.name)
        print(self.age)
        print(self.gender)
s1=student()
s1.addstudent(1,'gh',20,'male')
s1.displaystudent()
'''
'''
#write a program to make use of class method and instance method in python
class Employee:  
    
    salary = 25000  
    name='dharmesh'
    department='IT'
    def show(self):
       
        print('Name:', self.name, 'Department:', self.department, 'Salary:', Employee.salary)  
    @classmethod
    def change_salary(cls,salary):  
        cls.salary = salary  

obj = Employee()  
obj.show()
Employee.change_salary(45000) 
obj.show()  
'''
'''
# Write a program to make use of inner class
class It:
    def __init__(self):
        self.name = 'Software developer'
        self.den = self.devloper()
        
 
    def show(self):
        print('In outer class')
        print('Name:', self.name)
 
    # create a 1st Inner class
    class devloper:
        def __init__(self):
            self.name = 'Dharmesh'
            self.degree = 'MCA'
 
        def display(self):
            print("IN innner class")
            print("Name:", self.name)
            print("Degree:", self.degree)
outer = It()
outer.show()
d1 = outer.den
d1.display()
'''
'''
# Create a Temperature class. Create 2 methods named convertFarenheit() and convertCelsius().
class temperature:
    celsius=float(input("Enter the farenheit"))
    far=float(input("enter the celcious"))
    def convertfar(self):
        
        print("Farninhiet",(self.celsius *1.8)+32)
    def convertcel(self):
        print("celcious",((self.far - 39) * 5/9))
        
s1=temperature()
s1.convertfar()
s1.convertcel()
'''
'''
# Write a Python Program that creates a class and inherit into another class (Base Class : Student with rollno, name, gender, age) (Derived Class : Course with coursename, duration, fee)
class student:
    rollno=int(input("Enter your roll no"))
    name=input("Enter your name")
    gender=input("Enter your gender")
    age=int(input("Enter your age"))
    
class cource(student):
    courcename=input("Enter the name of cource")
    duration=float(input("Enter the duration in year"))
    fee=int(input("Enter fee of cource"))
  
    def __init__(self):
        print(self.rollno)
        print(self.name)
        print(self.rollno)
        print(self.rollno)
        print(self.courcename)
        print(self.duration)
        print(self.fee)
s1=cource()
'''

 #Use appropriate functions for each classWrite a program to display MRO using multiple inheritance. Multiple inheritance can be done as per your choice.
class a:
    def __init__(self):
        print("this is the super class a")
class b:
    def __init__(self):
        print("this is the super class b")
class c(a,b):
    def __init__(self):
        
        print("this is the base class c")
s1=c()
print(c.mro())

'''
# Write a program to create abstract class with one method.
# abstract base class work
from abc import ABC, abstractmethod

class a(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class b(a):

    # overriding abstract method
    def noofsides(self):
        print("This is the abstract example")
s=b()
s.noofsides()
'''
#Write a program to create interface and utilize the same in other class.