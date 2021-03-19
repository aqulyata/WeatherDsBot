#131
'''
N=int(input())
c=0

ma=0
num=0
for i in range(N):
    c+=1
    V,S = map(int, input().split())
    if S==1:
        if ma<V:
            num=c
            ma=V
if num==0:
    print(-1)
elif num>0:
    print(num)

#195
N, A, B = map(int,input().split())
print(A*B*2*N)

#233
N=int(input())
a=[int(input()) for i in range(N)]
const=437
for i in range(len(a)):
    if a[i]<=const:
        print(f'Crash {i+1}')
        break
else:
    print("No crash")
#263
N, i, j=map(int,input().split())
if j-i < N//2:
    print(j-i-1)
elif j-i >=N//2:
    print(N-j-i+1)
#264
N=int(input())
count=0
for i in range(N+1):
    gg=int(input())
    if gg>0:
        count += 1
        if count>const:
            const=count
    if gg<=0:
        const=count
        count=0
print(const)
#277 не решенно
from math import fabs
a, b, c = map(int,input().split())
if a>0 and b>1 and fabs(c)>1:
    print(f'{a}{b}x{c}y')
if a==0 and fabs(b)>1 and fabs(c)>1:
    print(f'{b}x{c}y')
if a>0 and b==1 and fabs(c)>1:
    print(f'{a}x{c}y')
if a>0 and b==0 and fabs(c)>1:
    print(f'{a}{c}y')
if a>0 and b>1 and fabs(c)>1:
    print(f'{a}{b}x{c}y')
#
N=input()
if N==str(N[::-1]):
    print("YES")
else:
    print("NO")
'''
a0, b0=map(int,input().split())
a1, b1=map(int,input().split())
counta=0
countb=0
while a1!=0:
    counta=a0
    counta+=1
    a1-=1
    if counta==24:
        counta=0
while b1!=0:
    countb=a0
    countb+=1
    b1-=1
    if countb==60:
        countb=0
        counta += 1
print(str(counta) + " : " + str(countb))




