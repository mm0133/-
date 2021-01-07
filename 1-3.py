#백준 3190 뱀 / 1시간20분
N=int(input())
bo=[[0]*(N+2) for i in range(N+2)]
for i in range(N+2):
    for j in  range(N+2):
        if i==0 or i==N+1 or j==0 or j==N+1:
            bo[i][j]=-1


#0 빈공간 1뱀  2사과
K=int(input())
for _ in range(K):
    i,j=map(int,input().split())
    bo[i][j]=2

L= int(input())
Dlist=[]
for _ in range(L):
    x,y=input().split()
    x=int(x)
    Dlist.append((x,y))
bo[1][1]=1

dir=0 # 우0 하1 좌2 상3
log=[(1,1,0)]
hx,hy=1,1
leng=1
t=0

def go():
    global dir,leng,t
    global hx,hy

    if dir==0:
        if bo[hy][hx+1]==-1 or bo[hy][hx+1]==1:
            return False
        if bo[hy][hx+1]==0:
            bo[hy][hx+1]=1
            hx+=1
            log.append((hx, hy))
            bo[log[t-leng][1]][log[t-leng][0]]=0

            return True
        if bo[hy][hx+1]==2:
            bo[hy][hx + 1] = 1
            hx += 1
            leng+=1
            log.append((hx, hy))

            return True

    elif dir==1:
        if bo[hy+1][hx]==-1 or bo[hy+1][hx]==1:
            return False
        if bo[hy+1][hx]==0:
            bo[hy+1][hx]=1
            hy+=1
            log.append((hx, hy))
            bo[log[t - leng][1]][log[t - leng][0]] = 0

            return True
        if bo[hy+1][hx]==2:
            bo[hy+1][hx] = 1
            hy += 1
            leng += 1
            log.append((hx, hy))
            return True

    elif dir==2:
        if bo[hy][hx - 1] == -1 or bo[hy][hx - 1] == 1:
            return False
        if bo[hy][hx - 1] == 0:
            bo[hy][hx - 1] = 1
            hx -= 1
            log.append((hx, hy))
            bo[log[t - leng][1]][log[t - leng][0]] = 0

            return True
        if bo[hy][hx - 1] == 2:
            bo[hy][hx - 1] = 1
            hx -= 1
            leng += 1
            log.append((hx, hy))
            return True

    else:
        if bo[hy-1][hx]==-1 or bo[hy-1][hx]==1:
            return False
        if bo[hy-1][hx]==0:
            bo[hy-1][hx]=1
            hy-=1
            log.append((hx, hy))
            bo[log[t - leng][1]][log[t - leng][0]] = 0
            return True
        if bo[hy-1][hx]==2:
            bo[hy-1][hx] = 1
            hy -= 1
            leng += 1
            log.append((hx, hy))
            return True



a=0

while(1):

    if len(Dlist)>a:
        if Dlist[a][0]==t:
            if Dlist[a][1]=='D':
                if dir==3:
                    dir=0
                else:
                    dir+=1
            else:
                if dir==0:
                    dir=3
                else:
                    dir-=1
            a+=1
    t+=1
    if not go():
        break


print(t)

