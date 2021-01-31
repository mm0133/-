#백준 15684 / 3시간 36분
# 으아아아 시간초과지옥
# 귀찮더라도 큐쓸때는 deque import 반드시하고 .popleft()로  하고
# bfs할때 위에서 종료조건 체크하지말고 /큐에 집어넣기 전에 필터링하자


N,M,H =map(int, input().split())
from collections import deque
line=[]
for i in range(M):
    line.append(list(map(int,input().split())))

def check(li):
    t = [i for i in range(1, N + 1)]
    x = t[:]
    for i in li:
        x[i[1]-1], x[i[1]] = x[i[1]], x[i[1]-1]

    if t==x:
        return True
    else:
        return False

def check2(cl, ol):
    for i in ol:
        if cl[0]==i[0] and abs(cl[1]-i[1])<=1:
            return False
    return True

anw=-1
line.sort()
qu=deque([[line,0]])

while qu:
    cli,v=qu.popleft()
    if check(cli):
        anw=len(cli)- len(line)
        break
    else:
        if len(cli)-len(line) == 3:
            continue
        for i in range(v,(N-1)*H):
            tmp=[i//(N-1)+1,i%(N-1)+1]
            if check2(tmp,cli):
                nli = cli[:]
                n=[i // (N - 1) + 1, i % (N - 1) + 1]

                k=0
                while k<len(nli):
                    if nli[k]>n:
                        nli.insert(k,n)
                        break
                    k+=1
                if k == len(nli):
                    nli.insert(k, n)
                qu.append([nli,i+1])

print(anw)