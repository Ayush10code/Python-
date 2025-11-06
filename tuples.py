t=(3,5,2,5,7,2)
s=("sab","aam","kiwi","kela")
m=(1,2,3,("hi","bye","jaldi jaaye"),5)

print("tuples:",t,s,m)

print("len",len(t))
print("count",t.count(5))
print("index",t.index(2))
print("slice",t[1:4])
print("nested",m[3][1])
a=("kiet",)
b=(1,2,3)
print("concat",a+b)

c=t+b
print("new",c)

print("max",max(t))
print("min",min(t))

print("in?",5 in t)
print("not in?",9 not in t)

x=tuple("hello")
print("tuple from str",x)

y=list(t)
y.append(99)
t=tuple(y)
print("after change",t)

print("done tuple")
