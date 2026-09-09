def sum(a,b,add):
    return add(a,b)
res=sum(10,20,lambda a,b: a+b)
print(res)