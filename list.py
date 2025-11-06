a=[3,1,7,2,9]
b=["apple","kiwi","banana","mango"]
c=[1,"kiet",3.5,True,"package"]

print("lists:",a,b,c)

a.append(5)
b.append("orange")
c.append(10)
print("after append",a,b,c)

a.insert(2,6)
b.insert(1,"grape")
c.insert(3,"yes")
print("insert",a,b,c)

a.extend([11,4])
b.extend(["pear","melon"])
c.extend(["ai",False])
print("extend",a)
print(b)
print(c)

a.remove(1)
b.remove("kiwi")
c.remove(True)
print("remove",a)
print(b)
print(c)

a.pop()
b.pop(2)
c.pop(1)
print("pop",a)
print(b)
print(c)

print("index:",a.index(2),b.index("banana"))
print("count:",c.count("ai"))

a.sort()
b.sort()
print("sort",a)
print(b)

a.reverse()
b.reverse()
print("rev",a)
print(b)

x=a.copy()
y=b.copy()
z=c.copy()
print("copies kr lo ",x,y,z)

print("lenght kya ha pata kare",len(a),len(b),len(c))

print("slice",a[1:4])
print(b[:3])
print(c[2:])

a.clear()
b.clear()
c.clear()
print("clr",a,b,c)
