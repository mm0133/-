#백준 14888 연산자 끼워넣기 /34분
#pypy3 41등/736명
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[-1]*(N-1)
maxv=-1000000000
minv=1000000000

def dfs(x):
    if x==N-1:
        global maxv, minv
        cur = calculate()
        maxv = max(cur, maxv)
        minv = min(cur, minv)
        return

    for i in range(4):
        if B[i]>0:
            C[x]=i
            B[i]-=1
            dfs(x+1)
            B[i]+=1

def calculate():
    res=A[0]
    for k,i in enumerate(C):
        if i==0:
            res=res+A[k+1]
        elif i==1:
            res=res-A[k+1]
        elif i==2:
            res=res*A[k+1]
        else:
            if res<0:
                res=-((-res)//A[k+1])
            else:
                res=res//A[k+1]
    return res

dfs(0)

print(maxv)
print(minv)