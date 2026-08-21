class Parent:
    def show(self):
        print("parent")
class child(Parent):
    def display(self):
        print("child")  
c=child()
c.display()
c.show() 
class A: 
    def add(self,a,b):
        print(a+b)
class B(A):
    def sub(self,a,b):
        print(a-b)
class C(B):
    def mul(self,a,b):
        print(a*b)

b=B()
b.add(2,3)
d=C()
d.sub(5,4)
d.mul(4,2)

                                

