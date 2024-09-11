#yha me sare data types directly or second method unka constructor function bnakr use kr rha hu
#dircetly implecitly
a= "hello world"
#explicitly using constructor function
a=str("hello world")

b= 20
b=int(20)

c=20.5
c= float(20.5)

d=2+1j
d=complex(1j)

e= ["apple","banana","cherry"]
e=list(("apple",45,"mango"))

f=("apple","banana","cherry")
f=tuple(("apple","banana","cherry"))

g=range(10) #sirf ek hi tarika hai

h= {"name":"rishabh","age":20}
h=dict(name="rishabh",age=36)

i={"apple","banana","cherry"}
i=set(("apple","banana","cherry"))

j=frozenset({"apple","banana","cherry"})#ek hi way

k=True
k=bool(5)

l=b"Hello"
l=bytes(5)

m=bytearray(5) #ek hi way
n=memoryview(bytes(5))  #single way
o=None #single way 


# Using str() to explicitly convert the non-string types to strings for concatenation
print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e) + " " + str(f) + " " + str(list(g)) + " " + str(h) + " " + str(i) + " " + str(j) + " " + str(k) + " " + str(l) + " " + str(m) + " " + str(n) + " " + str(o))

# Or alternatively, separating variables by commas
print(a, b, c, d, e, f, list(g), h, i, j, k, l, m, n, o)
value=len(e)  #length of the list e
print(value)
