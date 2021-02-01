#백준 15683 감시 / 1시간 23분
# 디버깅오래걸림 실행시간 너무높음
from copy import deepcopy

N, M= map(int, input().split())
ma=[[6]*(M+2)]

for i in range(N):
    ma.append([6]+list(map(int,input().split()))+[6])
ma.append([6]*(M+2))

#시계방향순(동남서북)
d=[
    [],
    [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
    [[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],
    [[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]],
    [[1,0,1,1],[1,1,0,1],[1,1,1,0],[0,1,1,1]],
    [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],
   ]

anw=64
def dfs(n,m,nma):
    global N,M

    if n==N+1:
        cnt=0
        for i in range(1,N+1):
            for j in range(1,M+1):
                if nma[i][j] == 0:
                    cnt+=1
        global anw
        anw=min(anw,cnt)
        return
    v=nma[n][m]
    if 0<v<6:

        for i in range(4):
            nxma = deepcopy(nma)
            if d[v][i][0]:
                x=m+1
                while(nxma[n][x]!=6):
                    if nxma[n][x]==0:
                        nxma[n][x]=7
                    x+=1


            if d[v][i][1]:
                y = n + 1
                while (nxma[y][m] != 6):
                    if nxma[y][m] == 0:
                        nxma[y][m] = 7
                    y += 1

            if d[v][i][2]:
                x = m - 1
                while (nxma[n][x] != 6):
                    if nxma[n][x] == 0:
                        nxma[n][x] = 7
                    x -= 1

            if d[v][i][3]:
                y = n - 1

                while (nxma[y][m] != 6):
                    if nxma[y][m] == 0:
                        nxma[y][m] = 7
                    y -= 1
            if m == M:
                dfs(n + 1, 1, nxma)
            else:
                dfs(n, m + 1, nxma)


    else:
        if m==M:
            dfs(n+1,1,nma)
        else:
            dfs(n,m+1,nma)
cma=deepcopy(ma)
dfs(1,1,cma)
print(anw)