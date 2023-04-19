#PATTERN
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(' ')
#PATTERN
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(' ')
#5
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