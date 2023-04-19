#1
#PATTERN
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(' ')
#2
#PATTERN
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(' ')
#3
#  PALINDROME
n=int(input())
t=n
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==t:
    print("Palindrome")
else:
    print('Not a Palindrime')
#4 AMSTRONG
n=int(input())
t=p=n
sum=0
count=0
while(n!=0):
    rem=n%10
    count+=1
    n=n//10
while(t!=0):
    rem=t%10
    sum=sum+(rem**count)
    t=t//10
if sum==p:
    print("Amstrong")
else:
    print("Not Amstrong")

# Area
l=int(input())
b=int(input())
if l==b:
    a_square=l*l
    print(f"Area of square : ({a_square})")
else:
    a_rect=l*b
    a_tri=0.5*l*b
    print(f"Area of Rectangle : {a_rect}")
    print(f"Area of Triangle : {a_tri}")

#Swap 3 nums in ascending 
a=int(input())
b=int(input())
c=int(input())
if a > c:
    a = a + c
    c = a - c
    a = a - c  
if a > b:
    a = a + b
    b = a - b
    a = a - b
if b > c:
    b = b + c
    c = b - c
    b = b - c

print(a,b,c)

