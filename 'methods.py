def func():
    print("I am Divyansh")
func()
def add(a,b):
    print(a+b)
add(6,7)
def check(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")
check(23)
def naturalsum(n):
    sum=0
    for i in range(0,n+1):
        sum+=i 
    print(sum)
naturalsum(5) 
def fac(n):
    f=1
    for i in range(1,n+1):
       f=f*i  
    print(f)    
fac(6)