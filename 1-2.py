import copy

N=int(input())
bo = [[0] * N for _ in range(N)]
for i in range(N):
    for j, k in enumerate(input().split()):
        bo[i][j]=int(k)
#0123 -상하좌우 i행 j열

maxv=bo[0][0]

def dfs(x):
    if x[2]==5:
        return
    global maxv

    nbo = [[0] * N for _ in range(N)]
    if(x[1]==0):

        for j in range(0,N):
            tem = []
            for i in range(N):
                if x[0][i][j]!=0:
                    tem.append(x[0][i][j])
            a=0
            for k in range(len(tem)-1):
                if tem[k]==0:
                    continue
                elif tem[k]==tem[k+1]:
                    if tem[k]*2>maxv:
                        maxv=tem[k]*2
                    nbo[a][j]=tem[k]*2
                    a+=1
                    tem[k+1]=0
                else:
                    if tem[k]>maxv:
                        maxv=tem[k]
                    nbo[a][j] = tem[k]
                    a += 1
            if tem:
                if tem[-1]!=0:
                    nbo[a][j] = tem[-1]


        dfs((nbo,0,x[2]+1))
        dfs((nbo, 1, x[2] + 1))
        dfs((nbo, 2, x[2] + 1))
        dfs((nbo, 3, x[2] + 1))


    nbo = [[0] * N for _ in range(N)]
    if (x[1] == 1):
        for j in range(0, N):
            tem = []
            for i in range(N):
                if x[0][i][j] != 0:
                    tem.append(x[0][i][j])
            a = N-1
            tem.reverse()
            for k in range(len(tem) - 1):
                if tem[k] == 0:
                    continue
                elif tem[k] == tem[k + 1]:
                    if tem[k] * 2 > maxv:
                        maxv = tem[k]*2
                    nbo[a][j] = tem[k] * 2
                    a -= 1
                    tem[k + 1] = 0
                else:
                    if tem[k] > maxv:
                        maxv = tem[k]
                    nbo[a][j] = tem[k]
                    a -= 1
            if tem:
                if tem[-1]!=0:
                    nbo[a][j] = tem[-1]

        dfs((nbo, 0, x[2] + 1))
        dfs((nbo, 1, x[2] + 1))
        dfs((nbo, 2, x[2] + 1))
        dfs((nbo, 3, x[2] + 1))


    nbo = [[0] * N for _ in range(N)]
    if (x[1] == 2):

        for i in range(0, N):
            tem = []
            for j in range(N):
                if x[0][i][j] != 0:
                    tem.append(x[0][i][j])
            a = 0
            for k in range(len(tem) - 1):
                if tem[k] == 0:
                    continue
                elif tem[k] == tem[k + 1]:
                    if tem[k] * 2 > maxv:
                        maxv = tem[k]*2
                    nbo[i][a] = tem[k] * 2
                    a += 1
                    tem[k + 1] = 0
                else:
                    if tem[k] > maxv:
                        maxv = tem[k]
                    nbo[i][a] = tem[k]
                    a += 1
            if tem:
                if tem[-1]!=0:
                    nbo[i][a] = tem[-1]

        dfs((nbo, 0, x[2] + 1))
        dfs((nbo, 1, x[2] + 1))
        dfs((nbo, 2, x[2] + 1))
        dfs((nbo, 3, x[2] + 1))



    nbo = [[0] * N for _ in range(N)]
    if (x[1] == 2):

        for i in range(0, N):
            tem = []
            for j in range(N):
                if x[0][i][j] != 0:
                    tem.append(x[0][i][j])
            tem.reverse()
            a = N-1
            for k in range(len(tem) - 1):
                if tem[k] == 0:
                    continue
                elif tem[k] == tem[k + 1]:
                    if tem[k] * 2 > maxv:
                        maxv = tem[k]*2
                    nbo[i][a] = tem[k] * 2
                    a -= 1
                    tem[k + 1] = 0
                else:
                    if tem[k] > maxv:
                        maxv = tem[k]
                    nbo[i][a] = tem[k]
                    a -= 1
            if tem:
                if tem[-1]!=0:
                    nbo[i][a] = tem[-1]

        dfs((nbo, 0, x[2] + 1))
        dfs((nbo, 1, x[2] + 1))
        dfs((nbo, 2, x[2] + 1))
        dfs((nbo, 3, x[2] + 1))

dfs((bo, 0, 0))
dfs((bo, 1, 0))
dfs((bo, 2, 0))
dfs((bo, 3, 0))

print(maxv)

#1시간 32분

