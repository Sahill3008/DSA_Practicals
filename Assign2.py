"""
To create ADT that implements the "set" concept. a. Add (new Element) -Place a value into the set ,
b. Remove (element) Remove the value c. Contains (element) Return true if element is in collection,
d. Size () Return number of values in collection Iterator () Return an iterator used to loop over
collection, e. Intersection of two sets , f. Union of two sets, g. Difference between two sets, h. Subset
"""
setA=set()
setB=set()
n=int(input("enter the limit of setA:"))
m=int(input("enter the limit of setB:"))
def add():
    for i in range(n):
       ele=input("enter element for setA:")
       setA.add(ele)
       print(setA)
def add1():
    for i in range(m):
        ele=input("enter element for setB:")
        setB.add(ele)
        print(setB)
def remove():
    ele=input("enter element to remove:")
    setA.remove(ele)
    print(setA,"\n")
def contain():
    contains = 7 in setA
    print("7 present is setA:")
    print(contains)
def union():
    print("union of sets:")
    print(setA|setB,"\n")
def intersection():
    print("Intersections:")
    print(setA.intersection(setB),"\n")
def difference():
    print("difference of sets:")
    print(setA-setB,"\n")
def length():
    print("Lenth of setA:")
    print(len(setA))
    print("Lenth of setB:")
    print(len(setB))
def subset():
    print(setB.issubset(setA))
add()
add1()
remove()
contain()
union()
intersection()
difference()
length()
subset()
