# class Hospital:
#     def __init__(self,value1,value2):
#         self.name = value1
#         self.age = value2
    
#     def printName(self):
#         # new_patient = Hospital(self.name,self.age)
#         print("The new patient is",self.name,"with",self.age,"years")
        
# HospitalA = Hospital("John Smith",20)
# HospitalA.printName()

#alternatively

name="John Smith"
age = 20
status = "new"

print("The",status, "patient is",name,"with",age,"years")

#alternatively

name="John Smith"
age = 20
status = "new"

def patient(name,age,status):
    new=print("The",status, "patient is",name,"with",age,"years")
    return new
patient(name,age,status)

#alternatively if you were to input
name = input("Enter the new patients name: ")
age = input("Enter the age: ")

def patient(name,age):
    new=print("The new patient is",name,"with",age,"years")
    return new
patient(name,age)




