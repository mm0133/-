#백준 14501 퇴사  44분
N=int(input())
dp=[0,0,0,0,0]
P=[0,0,0,0,0]
T=[1,1,1,1,1]
for i in range(N):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)

for i in range(N):
    tM = dp[i+4]
    for j in range(5):
        if 5-j==T[i+j+1]:
            cur=dp[i+5-(5-j)]+P[i+j+1]
            tM=max(tM,cur)
    dp.append(tM)

print(dp[N+4])