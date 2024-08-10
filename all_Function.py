#!/usr/bin/python3

# normal function 
def normal():
    print("I am a normal function.")

normal()

#function with parameters 
def parameters (a,b):
    print(a-b)
    
parameters(10,5)

#function with return value 
def back(a):
    return a
    
b=back("I am back") 
print(b)   

#function with unknown value
def unknown(*no):
    print(no[0],no[1])
    
unknown(3,5)    

#Arbitrary Keyword Arguments, **kwargs
def kwargs(**kwrg):
    return kwrg["city"], kwrg["name"]
    
info=kwargs(name="good",age=20,city="Dhaka")    
print(info)


#default value 
def default(city="dhaka"):
    print(city)
    
default("york")
default()
default("California")

#Keyword Arguments
def keyword(c3,c2,c1):
    print(c1)
    
keyword(c1="ami",c2="you",c3="everyone")    


#function with values
def value(v1,v2,/):
    return v1 + v2 % v2
    
v = value(4,6) #can't give key with value 
print(v)

#function with key: value
def keyvalue(*,k1,k2):
    return k1**k2
    
ke = keyvalue(k1=5,k2=3)
print(ke)    
    
#key value and value at the same time
def sametime(t1,t2,/, *, name, city):
    return t1 + t2, name, " and I am from", city
    
     
you = sametime("i","am",name="bill",city="buro")
print(you)     

#function with pass
def nothing(hehee):
    pass

#lmabda function anonymous   
sum = lambda a: a*a;

print(sum(5))        