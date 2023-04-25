'''def add():
    try:#to raise exception when non integers are given as inputs
        a=int(input())
    except ValueError as err:
        print(err)
    try:
        b=int(input())
    except ValueError as err:
        print(err)
    print(a+b)

#add() '''
 
 
'''def fabinocci(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a," ",b)
    else:
        print(a,b,end=" ")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
n=int(input())
if n<=0:
    print('Invalid argument')
else:
    fabinocci(n)'''


#LCM & HCF

def d(n):
    if n<=5:
        return
    d(n-1)
    print(n)
    d(n-1)
    print(n)

#d(8)

#25th
#nth Fabinocci number using recursion
def fabi(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    
    return fabi(n-1)+fabi(n-2)

#print(fabi(int(input())))


#SUM OF 1st 'n' fabinocci numbers
def sumfab(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    
    a=0
    b=1
    c=a+b
    sum=c+1
    a=b
    b=c
    
    sumfab(n-1)
    print(sum)
sumfab(10)

#using Reursion
