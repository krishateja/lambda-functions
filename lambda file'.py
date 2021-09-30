#funtions are two types:1)built in function 2)user defined functions
#1)built in functions:nothing but predefined functions like len(),id()
#2)user defined funtion:in this type function classified into two types
#i)traditional function:def keyword  eg:
#def m1():
    #print("this is from m1 class and now we discuss lambda functions")
#m1()
#ii)lambda function(anonymous function):lambda keyword
# syn:     var=lambda<input sequence>:<output sequence>
var=lambda a:a*a
print(var)#it will give object of the lambda function
print(var(7))#it will return value lambda function always return only one value
print((lambda a,b:a*b)(10,20))#directly we print without print function
v=lambda :"we are dicussing lambda functions"
print(v())
print((lambda :"we are dicussing lambda functions")())
print((lambda a:a**2)(5))#squaring of number
print((lambda a:a**3)(5))#cube of number
#we can use lambda function in list
print([(lambda a:a**2)(5),(lambda a:a**3)(5)])
list=[lambda a:a**2,lambda a,b :a+b, lambda a,b:a*b]
print(list[0](5),list[1](12,12),list[2](45,54),sep="\n")
#we can use lambda function in dictinories
d1={ "a":lambda a:a*a,
     "b":lambda a,b:a+b,
     "c":lambda a,b,c:a+b+c,
     "d":lambda a,b:a*b}
print(d1["a"](5))
print(d1["b"](10,20))
print(d1["c"](10,20,30))
print(d1["d"](10,20))
d2=lambda a=10,b=20,c=30:a+b+c
print(d2())
d3=lambda a=10,b=20,c=30:a+b+c
print(d3(15,25))#latest value will be added
#lambda function with condition:whenever we use single condition(true\false) we can't give only if condition ,we have to give without if condition
a1=lambda x,y:x>y
print(a1(10,20))
a2=lambda x,y:x<y
print(a2(10,20))
#lambda funtion with if else condition in that number will be printed
a1=lambda x,y:x if x>y else y
print(a1(10,20))
a2=lambda x:"ur eligible for voting" if x>=18 else "not eligible for voting"
print(a2(19))
a3=lambda a,b,c:a if a>b and a>c else b if b>c else c#nested if codition
print(a3(10,20,30))
#assignment
a1=lambda des:"hike=18%" if des=="pm" else "hike=16%" if des=="tm" else "dev=14%" if des=="dev" else "tester=12%" if des=="tester" else "no hike"
print(a1("pm"))
#lambda function with print
print((lambda m:[i for i in range(1,m)])(11))
print((lambda m:[print(i) for i in range(1,m)])(11))
print((lambda m:[print(i*5) for i in range(1,m)])(11))
print((lambda m:[print(i*j) for i in range(2,m) for j in range(1,11)])(5))
#lambda function with for loop
x=lambda a:a*a
for i in range(1,11):
    print(x(i))#lambda function with in for loop we can't write for loop in lambda function because lambda fuction gives only value
#if u want give for loop in lambda function we have to create for loop within list
a1=lambda a:[i for i in range(1,a)]
print(a1(10))
#nested lambda
x=lambda a=200,b=300:    lambda c=300:a+b+c
print(x)
print(x())
y=x()
print(y)
print(y())
x=lambda a,b:lambda c:a+c+b
print(x)
print(x(100,200))
y=x(100,200)
print(y(300))
# traditional function
def sqr(n):
    s=n*n
    return s
r=sqr(5)
print(r)

li=[2,4,6,8]
def sqr(n):
    s=n*n
    return s
r=sqr(li[0])
print(r)
r=sqr(li[3])
print(r)
r=sqr(li[2])
print(r)
r=sqr(li[1])
print(r)
for i in li:
    r=sqr(i)
    print(r)
for i in li:
    print(sqr(i))
#the main use of lambda function is input to the higher order functions:map(),filter(),reduce()
#using map function:map(<fun>,<interable>)in map function we can't impliment conditions but we can impliment in lambda function
#map funcion gives output  values same as how many values in input
li=[2,4,6,8]
def sqr(n):
    r=n*n
    return r
m=map(sqr,li)#it gives itarate m
print(m)#it gives objects
for i in m:
    print(i)
l1=[2,4,6,8]
def sq(n):
    r=n*n
    return r
print(list(map(sq,l1)))
m=list(map(sq,l1))
print(m)
#using lambda function with map function
l1=[1,2,3,4]
m=list(map(lambda n:n*n,l1))
print(m)
m1=list(map(lambda a:a**3,[1,2,3,4]))
print(m1)
m2=list(map(lambda a,b:a+b,[1,2,3,4],[4,3,2,1]))
print(m2)
m3=list(map(lambda a,b,c:a+b+c,[1,2,3,4],[4,3,2,1],[5,5,5,5]))
print(m3)
l2=["india","uk","us","france","russia"]
m4=list(map(lambda a:len(a),l2))
print(m4)
m5=list(map(lambda a:a.upper(),l2))
print(m5)
m6=list(map(lambda a:len(a)>3,l2))#it gives true or false
print(m6)
#filter:it is the same as map but it will gives values less than or equal to input values
list1=list(range(1,11))
print(list1)
f=filter(lambda a:a*a,[3,4,5,6])
print(f)
for i in f:
    print(i)
f=filter(lambda x:x%2==0,list1)
print(list(f))
l1=list("india")
print(l1)
f1=filter(lambda a:a=="i",l1)
print(list(f1))
#filter,lambda,range
f3=filter(lambda x:x%2==0,range(1,11))
print(list(f3))
#filter ,lambda,range,map
f3=list(map(lambda x:x*x,range(1,11)))
print(list(f3))
f4=filter(lambda x:x<100 and x>50,list(map(lambda x:x*x,range(1,11))))
print(list(f4))
str1= "HelElo All.. Welcome INDIA to Python O Tutorial"
v=["a","e","i","o","u"]
strlist=list(str1)
f5=filter(lambda x:x in v,strlist)
print(list(f5))
f5=filter(lambda x:x.lower() in v,strlist)
print(list(f5))
#reduce:same as map&filter but it gives only one value
import functools
def add(a,b):
    return (a+b)
f=functools.reduce(add,[2,4,3,5])
print(f)
from functools import reduce
def mul(a,b):
    return(a*b)
f=reduce(mul,[2,3,4,5])
print(f)
f1=reduce(lambda x,y:x+y,[2,3,4,5])
print(f1)
f2=reduce(lambda x,y:x*y,[2,3,4,5])
print(f2)
f3=reduce(lambda x,y:x if x>y else y ,[2,3,4,5])
print(f3)
f3=reduce(lambda x,y:x if x<y else y ,[2,3,4,5])
print(f3)




