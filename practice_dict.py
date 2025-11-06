d={"name":"ayush","clg":"kiet","year":2}
e={"a":1,"b":2,"c":3}

print("dicts:",d,e)

print("keys",d.keys())
print("values",d.values())
print("items",d.items())

print("get",d.get("clg"))
print("get2",d.get("branch","none"))

d["branch"]="cse"
print("after add",d)

d["year"]=3
print("upd",d)

d.update({"city":"ghaziabad"})
print("after update",d)
d.pop("clg")
print("after pop",d)

e.popitem()
print("popitem",e)

print("check key",'name' in d)

x=d.copy()
print("copy",x)
print("len",len(d))

f=dict(a=10,b=20)
print("new dict",f)
for k in d:
    print(k,d[k])

print("clear test")
e.clear()
print(e)

print("done dict")
