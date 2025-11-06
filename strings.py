s="hello world"
t="  python is fun but little tough   "
u="kiet123"

print("orig:",s,t,u)

print("upper",s.upper())
print("lower",s.lower())
print("title",s.title())
print("cap",s.capitalize())
print("swap",s.swapcase())
print("strip",t.strip())
print("rstrip",t.rstrip())
print("lstrip",t.lstrip())
print("replace",s.replace("world","python"))
print("find",s.find("o"))
print("index",s.index("e"))
print("count",s.count("l"))

print("split",s.split())
print("join",'-'.join(["hi","there","gdg"]))

print("startswith",s.startswith("he"))
print("endswith",s.endswith("ld"))

print("isalpha",u.isalpha())
print("isdigit",u.isdigit())
print("isalnum",u.isalnum())

a="kiet"
b="college"
print("concat",a+" "+b)

print("slice",s[1:5])
print("rev",s[::-1])
print("len",len(s))

x="python"
y=x.replace("p","P")
print("new:",y)
z="HELLO"
print("check",z.isupper())
print("mix",z.lower().capitalize())
print("done")
