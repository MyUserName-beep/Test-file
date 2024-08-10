#!/usr/bin/python3
#multiple inheritance
class A:
    def usr1(self):
        print('Hello one')

class B():

    def usr2(self):
        print('Hello two')
        
class C(A,B):
    
    def usr3(self):
        print('Hello three')        

x = C()
x.usr1()
x.usr2()
x.usr3()