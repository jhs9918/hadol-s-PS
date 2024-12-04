import math

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

ts = 0

for i in range(6) :
    ts+=math.ceil(size[i]/t)

tp = 0
tq = 0
if (p>n) : 
    tq = n
else :
    tp=n//p
    tq=n-tp*p


print(ts)
print(f'{tp} {tq}')
