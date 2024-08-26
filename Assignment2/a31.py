#example of init and self 
class Student:
    def __init__(self,f,l):
        self.fname=f
        self.lname=l
a=Student("Sandesh",'Subedi')
print(a.fname)
print(a.lname)
b=Student("Suikriti","Timilsina")
print(b.fname)
print(b.lname)