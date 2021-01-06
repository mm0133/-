from itertools import combinations
N = int(input())

A=[]

for i in range(N):
    input()
    A.append(input().split())

def dis(a,b):
    cnt=4
    for i in range(4):
        if a[i]==b[i]:
            cnt-=1
    return cnt




for i in range(0, N):
    if len(A[i])>47:
        print(0)

    else:
        mind=12
        B = list(combinations(A[i], 3))
        for j in B:
            cur=dis(j[0],j[1])+dis(j[1],j[2])+dis(j[2],j[0])
            mind=min(mind,cur)
        print(mind)
