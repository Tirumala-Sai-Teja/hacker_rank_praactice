t=int(input())
for __ in range(t):
    a,b,c,d=map(int,input().split())
    m=max(a,b,c,d)
    if (d-(3*m-a-b-c))%3==0:
        print('YES')
    else:
        print('NO')
